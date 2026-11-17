import subprocess
import re
import os
import time

# --- CONFIGURATION ---
LLAMA_CLI_PATH = "./bin/llama-cli"  
MODEL_PATH = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf?download=true" # Change to your current model
PROMPT_FILE = "temp_prompt.txt"
OUTPUT_FILE = "temp_output.txt"

# Thermal Control Settings
BATCH_SIZE = 3           # Number of prompts to process before resting
COOLDOWN_SECONDS = 60    # How long to rest the device (in seconds)

# --- INTEGRATED DATASET ---
# --- INTEGRATED DATASET (FULL CSV ORDER) ---
samsum_test = [
    {
        "id": 13829633,
        "dialogue": "Carolyn: hey!! Carolyn: I ran into your mum earlier today and she told me you'd moved out of town?? I had no idea! Sean: hi Sean: I guess we haven't talked in a while lol Sean: my fault too, sometimes I don't notice a month has passed Carolyn: I feel that Sean: so yeah, I have... I couldn't really find a new job and then bam! I found an interesting offer elsewhere Carolyn: ohhh Sean: at first I was reluctant but then I thought, whatever! I'll give it a shot. and they actually wanted me, haha Carolyn: well, that's great! are you happy with it now?? Sean: yeah, it's been good so far! the team are really nice people, they've helped me a lot!",
        "summary": "Sean moved out of town. He is satisfied with his new job."
    },
    {
        "id": 13717253,
        "dialogue": "James: good horror to watch? Kit: Japanese, US, Spain? James: Spanish could be cool. any good? Nick: I like Rec. not new thou. Seen it? James: no not yet. Really good? Ridley: I liked it too. Its more psycho than gore tho so depends what you into really James: psychological are cool so yeah, I'll watch that Nick: but makes sure it’s the first one not 2 or 0 or anything, they were realy shit Ridley: amen James: ok thx",
        "summary": "James wants to watch a good horror movie. Nick and Ridley recommended watching Rec."
    },
    {
        "id": 13814265,
        "dialogue": "Jake: forgot keys. U home? Noah: nope. at 4.  Jake: ok",
        "summary": "Jake forgot the keys. Noah will be back home at 4."
    },
    {
        "id": 13817247,
        "dialogue": "Kim: Knock knock! Frank: Hello :) Kim: Don't forget about Black Friday! Frank: wow, thanks! Kim: I figured that you may forget. Frank: Hahaha, true, thank you! Kim: No worries, I wanted to spare myself the week long whining on \"how could I forget about Black Friday\". Frank: Still not funny Kim :P Kim: This year set up a reminder or three ;) Frank: Is there anything in particular you're counting on? Kim: I'm actually more excited about the Cyber Monday, many studios already announced they will be releasing some bundles. Frank: Oh, which ones? Kim: BioWare and some less known indie producers. Frank: Cool! Are you on Steam? Kim: Yeah, but I'm not using it much any more since I've switched to PS. Frank: Yes! I've been wanting to ask you! How is it? In comparison with PC? Kim: Honestly? I love it. Kim: I know that many would like to stone me for saying that, but I don't see that much difference with PC and it's faaaar more comfortable. Frank: Even the graphics? I've heard you will never have the same effect on PS as on PC. Kim: Well, it's true, but I mostly enjoy the plot, the mechanics etc, so I don't feel like I'm missing out on something. Frank: Hm... interesting. Kim: If you're more into graphics than you can always watch some videos on YouTube where people compare PC and PS, but, to my mind, the differences are minimal. Kim: Also, if you really want to have amazing graphics you need quite a powerful PC, PS is more affordable. Frank: yeah, but games are more expensive. Kim: Not on Cyber Monday :D depends how much you play, it usually takes me quite a while to finish one. Frank: I'm more an occasional player, so I don't if there's any point. Kim: It is if you watch Netflix and don't have smart tv and I know you don't have it ;)",
        "summary": "Kim has reminded Frank about Black Friday. She has switched to using PlayStation."
    },
    {
        "id": 13817590,
        "dialogue": "Adriana: Sorry, I guess I can't make it. I'm feeling sick again. Adriana: I planned so many things for today... Adriana: Hate it. Elisa: What a pity... Elisa: Next time! Elisa: Hope you'll get better soon! Adriana: Hope so too. Adriana: How was at the pool? Elisa: The best ❤️ Elisa: 1 hour of swimming and 1 hour of sauna Elisa: Love it! Adriana:❤️ Adriana: I'm such a bad swimmer that you couldn't stand me xD Elisa: Ahahaha Elisa: There was such a girl today, soooo annoying 😂 Adriana: Just like me 😂😂😂",
        "summary": "Adriana is feeling sick, so she needs to give up her plans for today. Elisa went to the pool, she did 1 hour of swimming and 1 hour of sauna."
    },
    {
        "id": 13728210,
        "dialogue": "David: Hi Honey, did you have a good day? Sandy: Hi my love, oh ... i had meeting all day. What about you? David: great. . I went to Brooklyn and visit some really interesting museums Sandy: i'm sure you also had time for shopping? David: Yes of course. Sandy: what did you buy? David: a new pair of sneakers. Very nice, red and pink... Sandy: why did you buy them. You've got plenty of them! David: i need to keep fit during my stay here, so i want to run Sandy: i'm very impressed... you know you could run with me in the park nearby... David: yes, but central Park is such a nice place to run and to feel like a real new yorker. Sandy: I remind you that you're on business trip for week! David: i also went to Ralph Lauren on the fifth avenue. Sandy: Please, don't tell me you buy anything in there? David: I've found a very nice jacket ... for you! Sandy: Honey... David: I know ... i'm the man  Sandy: Have a good week. See you soon David: bye love",
        "summary": "David has bought a pair of sneakers because he wants to stay fit. He also bought a Ralph Lauren jacket as a present for Sandy."
    },
    {
        "id": 13810644,
        "dialogue": "Faheem : Hi Afhaam how are you? Afhaam : Hello Faheem i am a little bit busy i will call you soon. Faheem : OK ! Give my regards to family. Afhaam : Sure.",
        "summary": "Afhaam is a little busy and will cal Faheem soon."
    }
]
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
    total_questions = len(samsum_test)
    print(f"Starting staggered SAMSum benchmark on {total_questions} integrated prompts...\n")
    
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
