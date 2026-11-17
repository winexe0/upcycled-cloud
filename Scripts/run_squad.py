import subprocess
import re
import os
import time

# --- CONFIGURATION ---
LLAMA_CLI_PATH = "./bin/llama-cli"  
MODEL_PATH = "../../qwen2.5-3b-instruct-q4_k_m.gguf?download=true" # Change as needed
PROMPT_FILE = "temp_squad_prompt.txt"
OUTPUT_FILE = "temp_squad_output.txt"

# --- EXTREME THERMAL CONTROL SETTINGS ---
BATCH_SIZE = 1           
COOLDOWN_SECONDS = 180   

# --- THE 5 CALIBRATED SQuAD 2.0 PROMPTS ---
# Format: (Context, Question, Expected Answer / "Unanswerable")
SQUAD_DATA = [
    # 1. Answerable (Simple Extraction)
    (
        "The Norman dynasty had a major political, cultural and military impact on medieval Europe and even the Near East. The Normans were famed for their martial spirit and eventually for their Christian piety, becoming exponents of the Catholic orthodoxy into which they assimilated.",
        "What were the Normans famed for?",
        "Their martial spirit and Christian piety."
    ),
    
    # 2. UNANSWERABLE (Trick Question - tests hallucination restraint)
    (
        "In 1999, the BBC broadcast a six-part series documenting the Apollo missions. The series was highly acclaimed and won several documentary awards. Neil Armstrong and Buzz Aldrin were heavily featured in the archival footage.",
        "What award did Neil Armstrong win in 1999?",
        "UNANSWERABLE" # The text says the series won awards, not Armstrong.
    ),
    
    # 3. Answerable (Complex span extraction)
    (
        "Amazon rainforest deforestation is primarily driven by cattle ranching, which accounts for up to 80% of current deforestation. Secondary causes include agriculture for soy, logging, and infrastructure expansion such as highways.",
        "What is the secondary cause of deforestation in the Amazon?",
        "Agriculture for soy, logging, and infrastructure expansion."
    ),
    
    # 4. UNANSWERABLE (Plausible sounding, but missing data)
    (
        "Nikola Tesla was an inventor, electrical engineer, and mechanical engineer best known for his contributions to the design of the modern alternating current (AC) electricity supply system. He was born in Smiljan, in the Austrian Empire.",
        "What university did Nikola Tesla graduate from?",
        "UNANSWERABLE" # The text mentions his birth, not his education.
    ),
    
    # 5. Answerable (Specific numerical extraction)
    (
        "The speed of light in vacuum, commonly denoted c, is a universal physical constant important in many areas of physics. Its exact value is defined as 299,792,458 metres per second (approximately 300,000 km/s, or 186,000 mi/s).",
        "What is the exact defined value of the speed of light in metres per second?",
        "299,792,458 metres per second."
    )
]

def format_squad_prompt(context, question):
    """Formats the instruction for strict reading comprehension."""
    prompt_text = "You are a strict reading comprehension AI. Answer the question using ONLY the provided context. If the context does not contain the answer, reply exactly with 'Unanswerable'. Do not provide conversational filler.\n\n"
    prompt_text += f"Context:\n{context}\n\n"
    prompt_text += f"Question:\n{question}\n\n"
    prompt_text += "Answer:\n"
    return prompt_text

def run_llama_inference(prompt):
    with open(PROMPT_FILE, "w", encoding="utf-8") as f_prompt:
        f_prompt.write(prompt)

    command = [
        LLAMA_CLI_PATH,
        "-m", MODEL_PATH,
        "-f", PROMPT_FILE,    
        "-n", "128",           # Decreased tokens! SQuAD answers should be short. Saves energy.
        "-t", "4",            
        "-c", "2048",          # Context window easily fits SQuAD paragraphs
        "--temp", "0.0",       # STRICT 0.0 temp to prevent hallucinations
        "--log-disable"        
    ]
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
        subprocess.run(command, stdout=f_out, stderr=subprocess.DEVNULL, text=True, input="/exit\n")
        
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f_in:
        raw_output = f_in.read()
        
    return raw_output

def main():
    total_questions = len(SQUAD_DATA)
    print(f"Starting SQuAD 2.0 Comprehension Benchmark on {total_questions} prompts...\n")
    
    for i, data in enumerate(SQUAD_DATA):
        context, question, expected = data
        print(f"--- Processing Prompt {i+1}/{total_questions} ---")
        prompt = format_squad_prompt(context, question)
        
        raw_output = run_llama_inference(prompt)
        
        clean_output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', raw_output)
        
        split_phrase = "Answer:\n"
        if split_phrase in clean_output:
            ai_text = clean_output.split(split_phrase)[-1]
        else:
            ai_text = clean_output
            
        ai_text = ai_text.split("[ Prompt:")[0].split(">")[0].split("/exit")[0].strip()
        
        print("\nCONTEXT:")
        print(context)
        print(f"\nQUESTION: {question}")
        print(f"EXPECTED: {expected}")
        print("\nMODEL GENERATED RESPONSE:")
        print(ai_text)
        print("==================================================\n")

        if (i + 1) != total_questions:
            print(f"Pausing for {COOLDOWN_SECONDS} seconds...")
            time.sleep(COOLDOWN_SECONDS)
    
    if os.path.exists(PROMPT_FILE): os.remove(PROMPT_FILE)
    if os.path.exists(OUTPUT_FILE): os.remove(OUTPUT_FILE)
    print("SQuAD Benchmark complete!")

if __name__ == "__main__":
    main()
