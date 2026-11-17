import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# 1. Parse screenlog.0
with open("screenlog.0", "r", encoding="utf-8", errors="replace") as f:
    log_content = f.read()

# Clean up backspaces
log_content_clean = re.sub(r'.\x08', '', log_content)

# SAMSum run logic
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
        
        # In this specific log, look for text between "Summary:" and the "[ Prompt:" footer
        if "[ Prompt:" in b:
            # We look for the last chunk of text after 'Summary:'
            parts = b.split("Summary:")
            if len(parts) > 1:
                gen_part = parts[-1].split("[ Prompt:")[0]
                # Clean up spinner artifacts
                actual = re.sub(r'[|/\-\\ ]+', ' ', gen_part).strip()
            else:
                actual = "MISSING_GENERATION"
        else:
            actual = "MISSING_GENERATION"
            
        all_results.append({"expected": expected, "actual": actual})

# 2. Parse energy log
energy_df = pd.read_csv("/home/aryan/energy_log_1776734669.csv")
# LG G7 current is in uA (e.g. -263671 -> 0.26A)
energy_df['Power_W'] = (energy_df['Voltage_uV'] / 1e6) * (energy_df['Current_uA'].abs() / 1e6)
energy_df['Time_s'] = energy_df['Timestamp'] - energy_df['Timestamp'].min()
energy_df['dt'] = energy_df['Timestamp'].diff().fillna(0)
energy_df['Energy_J'] = energy_df['Power_W'] * energy_df['dt']
energy_df['Temp_Actual'] = energy_df['Temp_C'] / 10.0

# Stats for Section 7.8
mean_power = energy_df['Power_W'].mean()
active_mask = energy_df['Power_W'] > (mean_power * 1.2)
df_active = energy_df[active_mask]

stats = {}
if not df_active.empty:
    stats['duration'] = df_active['Timestamp'].max() - df_active['Timestamp'].min()
    stats['avg_power'] = df_active['Power_W'].mean()
    stats['peak_power'] = energy_df['Power_W'].max()
    stats['total_energy'] = df_active['Energy_J'].sum()
    stats['start_temp'] = energy_df['Temp_Actual'].iloc[0]
    stats['end_temp'] = energy_df['Temp_Actual'].iloc[-1]
    stats['max_temp'] = energy_df['Temp_Actual'].max()

# 3. Generate Plot
fig, ax1 = plt.subplots(figsize=(10, 5))
color1 = 'tab:orange'
ax1.set_xlabel('Time (seconds)', fontsize=12)
ax1.set_ylabel('Power (Watts)', color=color1, fontsize=12)
ax1.plot(energy_df['Time_s'], energy_df['Power_W'], color=color1, label='Power (W)', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('Temperature (°C)', color=color2, fontsize=12)
ax2.plot(energy_df['Time_s'], energy_df['Temp_Actual'], color=color2, label='Temp (°C)', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('SAMSum Benchmark (Ministral 3 3B) - LG G7 (Tier 3)', fontsize=14)
fig.tight_layout()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('lg_g7_ministral_3_3b_samsum.png', dpi=300)

print("PARSED_RESULTS:", all_results)
print("STATS:", stats)
