import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. PARSE ENERGY LOG (USB Tester CSV format)
# ==========================================
csv_filename = "/home/aryan/Downloads/llama-onn-squad-batch-nobreaks.csv"
print(f"Loading {csv_filename}...")
energy_df = pd.read_csv(csv_filename)

# Calculate the exact time interval (dt) between every single row using Unix time
energy_df['dt'] = energy_df['Unix time'].diff().fillna(0)
energy_df['Energy_J'] = energy_df['Power (W)'] * energy_df['dt']

# ==========================================
# 2. PURE COMPUTE THRESHOLD LOGIC
# ==========================================
# Grab the first 15 seconds to establish the pure idle baseline
idle_baseline = energy_df[energy_df['Run time (seconds)'] < 15]['Power (W)'].mean()

# Active threshold: Idle baseline + 0.5W buffer (Lowered for low-power ONN tablet)
active_mask = energy_df['Power (W)'] > (idle_baseline + 0.2)
df_active = energy_df[active_mask]

stats = {}
if not df_active.empty:
    # Summing 'dt' isolates the exact silicon compute time
    stats['active_compute_duration_s'] = df_active['dt'].sum()
    
    stats['idle_baseline_W'] = idle_baseline
    stats['avg_active_power_W'] = df_active['Power (W)'].mean()
    stats['peak_power_W'] = energy_df['Power (W)'].max()
    stats['total_energy_J'] = df_active['Energy_J'].sum()

# ==========================================
# 3. GENERATE PLOT (POWER ONLY)
# ==========================================
fig, ax1 = plt.subplots(figsize=(12, 6))

color1 = 'tab:orange'
ax1.set_xlabel('Run Time (seconds)', fontsize=12)
ax1.set_ylabel('Power (Watts)', color=color1, fontsize=12)
ax1.plot(energy_df['Run time (seconds)'], energy_df['Power (W)'], color=color1, label='Power (W)', linewidth=2)

# Draw the dotted visual threshold line
ax1.axhline(y=(idle_baseline + 0.2), color='black', linestyle='--', alpha=0.6, label='Active Threshold')

ax1.tick_params(axis='y', labelcolor=color1)

plt.title('ONN Device Inference Power Profile (SQuAD 2.0 Batch Runs Without Breaks) (Llama 3.2 1B)', fontsize=14)
fig.tight_layout()

ax1.legend(loc='upper left')

plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('onn_power_graph_corrected.png', dpi=300)
print("Saved graph as 'onn_power_graph_corrected.png'")

# ==========================================
# 4. OUTPUT RESULTS
# ==========================================
print("\n--- QUANTITATIVE STATS ---")
for key, value in stats.items():
    if isinstance(value, float):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")

# Quick Math Validation Check
if not df_active.empty:
    math_check = stats['avg_active_power_W'] * stats['active_compute_duration_s']
    print(f"\n[Math Validation: {stats['avg_active_power_W']:.2f}W * {stats['active_compute_duration_s']:.2f}s = {math_check:.2f} J]")
