import subprocess
import pandas as pd
import re
import os
import time

# --- CONFIGURATION ---
LLAMA_CLI_PATH = "./bin/llama-cli"  
MODEL_PATH = "../../Llama-3.2-3B-Instruct-Q4_0.gguf" # Change to your current model
DATASET_PATH = "train.csv" 
PROMPT_FILE = "temp_prompt.txt"
OUTPUT_FILE = "temp_output.txt"

# Thermal Control Settings
BATCH_SIZE = 3           # Number of prompts to process before resting
COOLDOWN_SECONDS = 60    # How long to rest the device (in seconds)

def format_samsum_prompt(row):
    """Formats the SAMSum row into a text-completion prompt."""
    dialogue = row['dialogue']
    
    prompt_text = "The following is a conversation between several people.\n\n"
    prompt_text += f"Conversation:\n{dialogue}\n\n"
    prompt_text += "Summarize the conversation in a few concise sentences.\n"
    prompt_text += "Summary:\n"
    
    return prompt_text

def run_llama_inference(prompt):
    # Write the prompt to a physical file
    with open(PROMPT_FILE, "w", encoding="utf-8") as f_prompt:
        f_prompt.write(prompt)

    command = [
        LLAMA_CLI_PATH,
        "-m", MODEL_PATH,
        "-f", PROMPT_FILE,    
        "-n", "128",          # INCREASED: We need more tokens to write a full summary!
        "-t", "4",            
        "-c", "4096",         # Keep at 4096 to ensure the whole chat log fits
        "--temp", "0.0",      
        "--log-disable"       
    ]
    
    # Run the inference, piping /exit so it doesn't hang
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
        subprocess.run(command, stdout=f_out, stderr=subprocess.DEVNULL, text=True, input="/exit\n")
        
    # Read the physical output file back into Python
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f_in:
        raw_output = f_in.read()
        
    return raw_output

def main():
    print(f"Loading SAMSum dataset: {DATASET_PATH}...")
    
    # Load the dataset and grab exactly the first 7 rows
    df = pd.read_csv(DATASET_PATH)
    samsum_test = df.head(7).to_dict('records')
    
    total_questions = len(samsum_test)
    print(f"Starting staggered SAMSum benchmark on {total_questions} prompts...\n")
    
    for i, row in enumerate(samsum_test):
        print(f"--- Processing Prompt {i+1}/{total_questions} ---")
        prompt = format_samsum_prompt(row)
        
        raw_output = run_llama_inference(prompt)
        
        # 1. Strip ANSI color codes
        clean_output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', raw_output)
        
        # 2. Isolate EXACTLY what the AI summarized
        # We chop off the prompt:
        split_phrase = "Summary:\n"
        if split_phrase in clean_output:
            ai_text = clean_output.split(split_phrase)[-1]
        else:
            ai_text = clean_output
            
        # We chop off the timing metrics and interactive garbage at the end:
        ai_text = ai_text.split("[ Prompt:")[0]
        ai_text = ai_text.split(">")[0]
        ai_text = ai_text.split("/exit")[0]
        
        generated_summary = ai_text.strip()
        expected_summary = row['summary'].strip()
        
        print("\nEXPECTED SUMMARY:")
        print(expected_summary)
        print("\nMODEL GENERATED SUMMARY:")
        print(generated_summary)
        print("==================================================\n")

        # --- THERMAL COOLDOWN LOGIC ---
        if (i + 1) % BATCH_SIZE == 0 and (i + 1) != total_questions:
            print(f"[THERMAL CONTROL] Batch of {BATCH_SIZE} complete.")
            print(f"Pausing for {COOLDOWN_SECONDS} seconds to allow passive heat dissipation...")
            time.sleep(COOLDOWN_SECONDS)
            print("Resuming inference...\n")
    
    # Clean up the temporary files
    if os.path.exists(PROMPT_FILE): os.remove(PROMPT_FILE)
    if os.path.exists(OUTPUT_FILE): os.remove(OUTPUT_FILE)
    print("Benchmark complete!")

if __name__ == "__main__":
    main()
