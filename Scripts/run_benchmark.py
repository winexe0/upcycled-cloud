import subprocess
import pandas as pd
import re
import os

LLAMA_CLI_PATH = "./bin/llama-cli"  
MODEL_PATH = "../../Ministral-3-3B-Instruct-2512-Q4_0.gguf" 
DATASET_PATH = "test-00000-of-00001.parquet" 
PROMPT_FILE = "temp_prompt.txt"
OUTPUT_FILE = "temp_output.txt"

def format_mmlu_prompt(row):
    """Formats a classic text-completion prompt."""
    prompt_text = f"The following is a multiple-choice question.\n\nQuestion: {row['question']}\n\nChoices:\n"
    
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i, option in enumerate(row['options']):
        prompt_text += f"{letters[i]}. {option}\n"
    
    prompt_text += "\nAnswer with only a single letter (A-J).\nThe correct choice is: "
    return prompt_text

import sys

def run_llama_inference(prompt):
    # 1. Write the prompt to a physical file
    with open(PROMPT_FILE, "w", encoding="utf-8") as f_prompt:
        f_prompt.write(prompt)

    command = [
        LLAMA_CLI_PATH,
        "-m", MODEL_PATH,
        "-f", PROMPT_FILE,    
        "-n", "2",            
        "-t", "4",            
        "-c", "4096",         
        "--temp", "0.0",      
        "--log-file", "debug.log"       
    ]
    
    # 2. THE FIX: Remove DEVNULL so stderr flows naturally to the terminal.
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
        subprocess.run(command, stdout=f_out, stderr=sys.stderr, text=True, input="/exit\n")
        
    # 3. Read the physical output file back into Python
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f_in:
        raw_output = f_in.read()
        
    # 4. Echo the generated text to the console so it gets captured in your master log file
    print(raw_output)
        
    return raw_output

def main():
    print(f"Loading local dataset: {DATASET_PATH}...")
    
    df = pd.read_parquet(DATASET_PATH)
    physics_df = df[df['category'] == 'physics'].head(20)
    physics_test = physics_df.to_dict('records')
    
    correct_answers = 0
    total_questions = len(physics_test)
    
    print(f"Starting offline benchmark on {total_questions} questions...\n")
    
    for i, row in enumerate(physics_test):
        prompt = format_mmlu_prompt(row)
        
        raw_output = run_llama_inference(prompt)
        
        # 4. Strip ANSI color codes just in case they printed to the file
        clean_output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', raw_output)
        
        # 5. Isolate EXACTLY what the AI answered.
        # We chop off the prompt:
        split_phrase = "The correct choice is: "
        if split_phrase in clean_output:
            ai_text = clean_output.split(split_phrase)[-1]
        else:
            ai_text = clean_output
            
        # We chop off the timing metrics and interactive garbage at the end:
        ai_text = ai_text.split("[ Prompt:")[0]
        ai_text = ai_text.split(">")[0]
        ai_text = ai_text.split("/exit")[0]
            
        # Find the first standalone A-J letter in the perfectly isolated chunk
        matches = re.findall(r'\b([A-J])\b', ai_text.upper())
        model_answer = matches[0] if matches else "X"
        
        actual_answer = row['answer']
        
        is_correct = (model_answer == actual_answer)
        if is_correct:
            correct_answers += 1
            
        print(f"Q{i+1}: Expected [{actual_answer}] | Model Guessed [{model_answer}] -> {'CORRECT' if is_correct else 'WRONG'}")

    accuracy = (correct_answers / total_questions) * 100
    print(f"\n--- FINAL SCORE ---")
    print(f"Accuracy: {accuracy}% ({correct_answers}/{total_questions})")
    
    # Clean up the temporary files
    if os.path.exists(PROMPT_FILE): os.remove(PROMPT_FILE)
    if os.path.exists(OUTPUT_FILE): os.remove(OUTPUT_FILE)

if __name__ == "__main__":
    main()
