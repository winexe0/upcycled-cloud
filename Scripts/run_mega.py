import subprocess
import pandas as pd
import re
import os
import time

# --- CONFIGURATION ---
LLAMA_CLI_PATH = "./bin/llama-cli"  
MODEL_PATH = "Llama-3.2-3B-Instruct-Q4_0.gguf" # Change to your current model
DATASET_PATH = "mega.csv" 
PROMPT_FILE = "temp_prompt.txt"
OUTPUT_FILE = "temp_output.txt"

# Thermal & Power Control Settings
BATCH_SIZE = 1           # Number of prompts to process before resting
IDLE_TEMP = 310          # Target idle temperature (e.g., 350 = 35.0°C depending on sysfs scale)

def get_temperature():
    """Reads the current battery/device temperature."""
    try:
        with open("/sys/class/power_supply/battery/temp", "r") as f:
            return int(f.read().strip())
    except Exception as e:
        print(f"[WARNING] Could not read temperature: {e}")
        return 0

def get_battery_level():
    """Reads the current battery percentage."""
    try:
        with open("/sys/class/power_supply/battery/capacity", "r") as f:
            return int(f.read().strip())
    except Exception as e:
        print(f"[WARNING] Could not read battery level: {e}")
        return 100 # Default to 100 to prevent infinite loops if file is missing

def handle_battery_low():
    """Pauses the script and prompts the user to charge the phone."""
    print("\n[BATTERY NOTICE] The phone needs to be charged (40% or below).")
    while True:
        ans = input("Is the phone charged? (Yes/no): ").strip().lower()
        if ans in ['yes', 'y']:
            current_batt = get_battery_level()
            if current_batt > 40:
                print(f"Battery is at {current_batt}%. Resuming script...")
                break
            else:
                print(f"Battery is still at {current_batt}%. Please charge it past 40%.")
        else:
            print("Waiting for the phone to be charged...")
            time.sleep(2)

def run_llama_inference(prompt):
    # Write the prompt to a physical file
    with open(PROMPT_FILE, "w", encoding="utf-8") as f_prompt:
        f_prompt.write(prompt)

    command = [
        LLAMA_CLI_PATH,
        "-m", MODEL_PATH,
        "-f", PROMPT_FILE,    
        "-n", "1024",          # Needs enough tokens for AlpacaEval coding tasks
        "-t", "4",            
        "-c", "4096",         
        "--temp", "0.0",      
        "--log-disable"       
    ]
    
    # Retry loop in case the prompt gets killed due to low battery
    while True:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
            process = subprocess.Popen(
                command, 
                stdout=f_out, 
                stderr=subprocess.DEVNULL, 
                text=True, 
                stdin=subprocess.PIPE
            )
            
            # Pipe /exit so it doesn't hang
            try:
                process.stdin.write("/exit\n")
                process.stdin.close()
            except Exception:
                pass

            was_killed = False
            
            # Polling loop to monitor battery while inference is running
            while process.poll() is None:
                if get_battery_level() <= 40:
                    process.kill()
                    process.wait()
                    was_killed = True
                    print("\n[WARNING] Active prompt killed due to low battery.")
                    handle_battery_low()
                    break # Break out of polling loop to restart the prompt
                
                time.sleep(1) # Check battery every 1 second
                
        if was_killed:
            print("Retrying the interrupted prompt...")
            continue # Restart the inference loop for this prompt
        else:
            break # Inference completed successfully

    # Read the physical output file back into Python
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f_in:
        raw_output = f_in.read()
        
    return raw_output

def main():
    print(f"Loading Mega dataset: {DATASET_PATH}...")
    
    # Load the mega dataset (process all rows)
    df = pd.read_csv(DATASET_PATH)
    mega_test = df.to_dict('records')
    
    total_questions = len(mega_test)
    print(f"Starting Mega benchmark on {total_questions} randomized prompts...\n")
    
    for i, row in enumerate(mega_test):
        task_type = row['task_type']
        prompt = row['formatted_prompt']
        expected_output = str(row['expected_output']).strip()
        
        print(f"--- Processing Prompt {i+1}/{total_questions} [{task_type}] ---")
        
        raw_output = run_llama_inference(prompt)
        
        # 1. Strip ANSI color codes
        clean_output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', raw_output)
        
        # 2. Isolate EXACTLY what the AI generated dynamically based on the task
        if task_type == "SAMSum":
            split_phrase = "Summary:\n"
        elif task_type == "AlpacaEval":
            split_phrase = "Response:\n"
        elif task_type == "SQuAD_2.0":
            split_phrase = "Answer:\n"
        else:
            split_phrase = prompt[-20:] # Fallback just in case
            
        if split_phrase in clean_output:
            ai_text = clean_output.split(split_phrase)[-1]
        else:
            ai_text = clean_output
            
        # 3. Chop off the timing metrics and interactive garbage at the end:
        ai_text = ai_text.split("[ Prompt:")[0]
        ai_text = ai_text.split(">")[0]
        ai_text = ai_text.split("/exit")[0]
        
        generated_summary = ai_text.strip()
        
        print(f"\nEXPECTED OUTPUT ({task_type}):")
        print(expected_output)
        print(f"\nMODEL GENERATED OUTPUT ({task_type}):")
        print(generated_summary)
        print("==================================================\n")

        # --- THERMAL COOLDOWN LOGIC ---
        if (i + 1) % BATCH_SIZE == 0 and (i + 1) != total_questions:
            print(f"[THERMAL CONTROL] Batch of {BATCH_SIZE} complete.")
            print(f"Pausing until device temperature drops to {IDLE_TEMP}...")
            
            while True:
                # Check battery during cooldown
                if get_battery_level() <= 40:
                    handle_battery_low()
                
                current_temp = get_temperature()
                if current_temp <= IDLE_TEMP:
                    print(f"Target temperature reached ({current_temp}). Resuming inference...\n")
                    break
                
                # Sleep briefly before checking temp/battery again
                time.sleep(5)
    
    # Clean up the temporary files
    if os.path.exists(PROMPT_FILE): os.remove(PROMPT_FILE)
    if os.path.exists(OUTPUT_FILE): os.remove(OUTPUT_FILE)
    print("Mega Benchmark complete!")

if __name__ == "__main__":
    main()
