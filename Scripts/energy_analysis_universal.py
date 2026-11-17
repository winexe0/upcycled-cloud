import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# ==========================================
# 1. PARSE INFERENCE LOG (screenlog.0)
# ==========================================
with open("screenlog.0", "r", encoding="utf-8", errors="replace") as f:
    log_content = f.read()

# Clean up backspaces common in terminal logs
log_content_clean = re.sub(r'.\x08', '', log_content)

marker = "Starting staggered SAMSum benchmark"
runs = log_content_clean.split(marker)

all_results = []
if len(runs) > 1:
    last_run = runs[-1]
    blocks = last_run.split("--- Processing Prompt")
    
    for b in blocks[1:]:
        # Find Expected Summary
        exp_match = re.search(r'EXPECTED SUMMARY:\n(.*?)\n\nMODEL GENERATED SUMMARY:', b, re.DOTALL)
        expected = exp_match.group(1).strip() if exp_match else "N/A"
        
        # Find Actual Generated Summary
        if "[ Prompt:" in b:
            parts = b.split("Summary:")
            if len(parts) > 1:
                gen_part = parts[-1].split("[ Prompt:")[0]
                # Clean up spinner artifacts (| / - \)
                actual = re.sub(r'[|/\-\\ ]+', ' ', gen_part).strip()
            else:
                actual = "MISSING_GENERATION"
        else:
            actual = "MISSING_GENERATION"
            
        all_results.append({"expected": expected, "actual": actual})

# ==========================================
# 2. PARSE ENERGY LOG (eco-logger CSV)
# ==========================================
# CHANGE THIS FILENAME TO YOUR CURRENT RUN
energy_df = pd.read_csv("energy_log_current_run.csv")

# Standard conversion for uA to Amperes (Use / 1000.0 ONLY for Galaxy S8)
energy_df['Power_W'] = (energy_df['Voltage_uV'] / 1e6) * (energy_df['Current_uA'].abs() / 1e6)
energy_df['Time_s'] = energy_df['Timestamp'] - energy_df['Timestamp'].min()

# Calculate energy per tick (dt)
energy_df['dt'] = energy_df['Timestamp'].diff().fillna(0)
energy_df['Energy_J'] = energy_df['Power_W'] * energy_df['dt']
energy_df['Temp_Actual'] = energy_df['Temp_C'] / 10.0

# ==========================================
# 3. UNIVERSAL IDLE BASELINE LOGIC
# ==========================================
# Grab the first 15 seconds to establish the pure idle baseline for this specific device
idle_baseline = energy_df[energy_df['Time_s'] < 15.0]['Power_W'].mean()

# The active threshold is the device's unique idle baseline + a 0.75W buffer to ignore OS noise
active_mask = energy_df['Power_W'] > (idle_baseline + 0.75)
df_active = energy_df[active_mask]

# Calculate final stats strictly on the active inference blocks
stats = {}
if not df_active.empty:
    stats['duration'] = df_active['Timestamp'].max() - df_active['Timestamp'].min()
    stats['idle_baseline_W'] = idle_baseline
    stats['avg_active_power'] = df_active['Power_W'].mean()
    stats['peak_power'] = energy_df['Power_W'].max()
    stats['total_energy_J'] = df_active['Energy_J'].sum()
    stats['start_temp'] = energy_df['Temp_Actual'].iloc[0]
    stats['end_temp'] = energy_df['Temp_Actual'].iloc[-1]
    stats['max_temp'] = energy_df['Temp_Actual'].max()



# ==========================================
# 4. GENERATE PLOT
# ==========================================
fig, ax1 = plt.subplots(figsize=(10, 5))
color1 = 'tab:orange'
ax1.set_xlabel('Time (seconds)', fontsize=12)
ax1.set_ylabel('Power (Watts)', color=color1, fontsize=12)
ax1.plot(energy_df['Time_s'], energy_df['Power_W'], color=color1, label='Power (W)', linewidth=2)

# Draw a dotted line to visually show where the script set the Active Threshold
ax1.axhline(y=(idle_baseline + 0.75), color='black', linestyle='--', alpha=0.6, label='Active Threshold')

ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('Temperature (°C)', color=color2, fontsize=12)
ax2.plot(energy_df['Time_s'], energy_df['Temp_Actual'], color=color2, label='Temp (°C)', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color2)

# UPDATE TITLE AS NEEDED
plt.title('SAMSum Benchmark - Auto-Calibrated Universal Run', fontsize=14)
fig.tight_layout()

# Combine legends from both axes
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('current_run_graph.png', dpi=300)

# ==========================================
# 5. OUTPUT RESULTS
# ==========================================
print("--- QUALITATIVE RESULTS ---")
for i, res in enumerate(all_results):
    # Print the first 75 characters of the summary for quick verification
    print(f"P{i+1} Gen: {res['actual'][:75]}...")

print("\n--- QUANTITATIVE STATS ---")
for key, value in stats.items():
    if isinstance(value, float):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")
