import subprocess
import re
import os
import time

# --- CONFIGURATION ---
LLAMA_CLI_PATH = "./bin/llama-cli"  
# Make sure to point this to the model you are testing!
MODEL_PATH = "../../qwen2.5-3b-instruct-q4_k_m.gguf?download=true" 
PROMPT_FILE = "temp_prompt.txt"
OUTPUT_FILE = "temp_output.txt"

# --- EXTREME THERMAL CONTROL SETTINGS ---
# Alpaca generation is incredibly heavy. The device MUST rest after every single prompt.
BATCH_SIZE = 1           
# Increased to 3 full minutes to allow 10nm chips to dump sustained generation heat
COOLDOWN_SECONDS = 180   

# --- THE 5 CALIBRATED ALPACA PROMPTS ---
ALPACA_PROMPTS = [
    # 1. C++ / GUI Code Generation
    "Write a C++ function that takes a reference to a std::string containing markdown formatted text and returns a std::string containing html formatted text.",
    
    # 2. Advocacy & Persuasive Writing (Long-form generation)
    "I am trying to win over a new client for my writing services and skinny brown dog media to as as a ghost writer for their book Unbreakable Confidence. Can you help me write a persuasive proposal that highlights the benefits and value of having a editor/publisher",
    
    # 3. Advanced STEM Reasoning (AP Physics ceiling test)
    "Why don't people like the many-worlds interpretation of quantum mechanics?",
    
    # 4. Automation & Calculus (AP Calculus AB + Scripting)
    "can you please create a python script that outputs a derivative using The Average Rate of Change Formula A(x) = f(b)-f(a) /(b-a) when x is user input",
    
    # 5. Strict Formatting (Memory exhaustion test)
    "I run a website about merchant navy studies. What are some subniches I should be tackling with my content. Give me the results as a table with the sub niche a number between 1 and 100 to indicate the sub niche popularity."
]

def format_alpaca_prompt(instruction):
    """Formats the instruction into a standard task-completion prompt."""
    prompt_text = "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n"
    prompt_text += f"Instruction:\n{instruction}\n\n"
    prompt_text += "Response:\n"
    return prompt_text

def run_llama_inference(prompt):
    with open(PROMPT_FILE, "w", encoding="utf-8") as f_prompt:
        f_prompt.write(prompt)

    command = [
        LLAMA_CLI_PATH,
        "-m", MODEL_PATH,
        "-f", PROMPT_FILE,    
        "-n", "1024",          # MASSIVE INCREASE: 512 tokens to allow for long code/essay generation
        "-t", "4",            
        "-c", "4096",         
        "--temp", "0.1",      # Slight bump to 0.1 to allow natural language flow for essays 
        "--log-disable"       
    ]
    
    # Run the inference, piping /exit so it doesn't hang
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
        subprocess.run(command, stdout=f_out, stderr=subprocess.DEVNULL, text=True, input="/exit\n")
        
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f_in:
        raw_output = f_in.read()
        
    return raw_output

def main():
    total_questions = len(ALPACA_PROMPTS)
    print(f"Starting Single-Fire AlpacaEval benchmark on {total_questions} prompts...\n")
    print(f"WARNING: Strict thermal controls engaged. {COOLDOWN_SECONDS}s cooldown after EVERY prompt.\n")
    
    for i, instruction in enumerate(ALPACA_PROMPTS):
        print(f"--- Processing Prompt {i+1}/{total_questions} ---")
        prompt = format_alpaca_prompt(instruction)
        
        raw_output = run_llama_inference(prompt)
        
        # 1. Strip ANSI color codes
        clean_output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', raw_output)
        
        # 2. Isolate the AI's response
        split_phrase = "Response:\n"
        if split_phrase in clean_output:
            ai_text = clean_output.split(split_phrase)[-1]
        else:
            ai_text = clean_output
            
        # Chop off timing metrics and exit commands
        ai_text = ai_text.split("[ Prompt:")[0]
        ai_text = ai_text.split(">")[0]
        ai_text = ai_text.split("/exit")[0]
        
        generated_response = ai_text.strip()
        
        print("\nINSTRUCTION:")
        print(instruction)
        print("\nMODEL GENERATED RESPONSE:")
        print(generated_response)
        print("==================================================\n")

        # --- EXTREME THERMAL COOLDOWN LOGIC ---
        if (i + 1) != total_questions:
            print(f"[THERMAL CONTROL] Prompt {i+1} complete.")
            print(f"Pausing for {COOLDOWN_SECONDS} seconds to prevent thermal runaway...")
            time.sleep(COOLDOWN_SECONDS)
            print("Resuming inference...\n")
    
    # Clean up
    if os.path.exists(PROMPT_FILE): os.remove(PROMPT_FILE)
    if os.path.exists(OUTPUT_FILE): os.remove(OUTPUT_FILE)
    print("AlpacaEval Benchmark complete!")

if __name__ == "__main__":
    main()
