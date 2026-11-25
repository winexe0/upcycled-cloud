# OnePlus 7T (`Q4_K_M`) Redo: SAMSum, AlpacaEval & SQuAD 2.0 Energy and Inference Analysis

All 27 `energy_log_*.csv` files and 27 `screenlog.*` files (`samsum_0..9`, `alpaca_0..9`, and `squad_0..9`) were pulled from `/data/data/com.termux/files/home/llama.cpp/build-cpu` on the **OnePlus 7T** via `adb pull`, stored in [`raw/`](./raw) and organized by `<Model>/Q4_K_M/<Benchmark>/OnePlus 7T/CPU/`, and analyzed using [`~/energy_analysis_universal.py`](file:///home/aryan/energy_analysis_universal.py) (with `Current_uA / 1000.0` since the OnePlus 7T kernel battery driver reports `current_now` in milliamps, `mA`).

---

## 1. SAMSum Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_K_M`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`samsum_0`** | [`screenlog.samsum_0`](./raw/screenlog.samsum_0) | [`energy_log_1795486818.csv`](./raw/energy_log_1795486818.csv) | **Llama 3.2 3B** | Single-Fire (`train_single.csv`) | 1 | 32.40 | 8.50 | 49 s | 1.01 W | 5.74 W | 7.94 W | **175.77 J** | 0.0488 Wh | 29.7 → 30.7 (**30.7°C**) |
| **`samsum_1`** | [`screenlog.samsum_1`](./raw/screenlog.samsum_1) | [`energy_log_1795486888.csv`](./raw/energy_log_1795486888.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 7 | 31.14 | 9.04 | 156 s | 1.04 W | 5.66 W | 8.08 W | **769.07 J** | 0.2136 Wh | 30.7 → 34.7 (**34.8°C**) |
| **`samsum_2`** | [`screenlog.samsum_2`](./raw/screenlog.samsum_2) | [`energy_log_1795487610.csv`](./raw/energy_log_1795487610.csv) | **Llama 3.2 3B** | Staggered Batch (`180s` cooldown) | 7 | 29.79 | 8.60 | 527 s | 0.81 W | 5.30 W | 8.43 W | **801.27 J** | 0.2226 Wh | 29.8 → 31.2 (**33.0°C**) |
| **`samsum_3`** | [`screenlog.samsum_3`](./raw/screenlog.samsum_3) | [`energy_log_1795488704.csv`](./raw/energy_log_1795488704.csv) | **Ministral 3 3B** | Staggered Batch (`180s` cooldown) | 7 | 27.54 | 6.90 | 687 s | 1.01 W | 5.82 W | 8.28 W | **1800.74 J** | 0.5002 Wh | 28.7 → 34.0 (**35.9°C**) |
| **`samsum_4`** | [`screenlog.samsum_4`](./raw/screenlog.samsum_4) | [`energy_log_1795490138.csv`](./raw/energy_log_1795490138.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 7 | 26.89 | 6.97 | 331 s | 0.90 W | 5.63 W | 8.23 W | **1761.17 J** | 0.4892 Wh | 29.5 → 37.7 (**37.8°C**) |
| **`samsum_6`** | [`screenlog.samsum_6`](./raw/screenlog.samsum_6) | [`energy_log_1795491094.csv`](./raw/energy_log_1795491094.csv) | **Ministral 3 3B** | Single-Fire (`train_single.csv`) | 1 | 27.30 | 5.90 | 82 s | 0.93 W | 5.91 W | 7.95 W | **367.28 J** | 0.1020 Wh | 30.9 → 33.4 (**33.4°C**) |
| **`samsum_7`** | [`screenlog.samsum_7`](./raw/screenlog.samsum_7) | [`energy_log_1795491197.csv`](./raw/energy_log_1795491197.csv) | **Qwen 2.5 3B** | Single-Fire (`train_single.csv`) | 1 | 31.60 | 9.30 | 55 s | 1.07 W | 5.75 W | 7.18 W | **207.42 J** | 0.0576 Wh | 33.4 → 33.8 (**33.8°C**) |
| **`samsum_8`** | [`screenlog.samsum_8`](./raw/screenlog.samsum_8) | [`energy_log_1795491273.csv`](./raw/energy_log_1795491273.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 7 | 30.79 | 9.67 | 158 s | 1.12 W | 5.52 W | 7.83 W | **767.59 J** | 0.2132 Wh | 33.8 → 36.8 (**36.9°C**) |
| **`samsum_9`** | [`screenlog.samsum_9`](./raw/screenlog.samsum_9) | [`energy_log_1795492117.csv`](./raw/energy_log_1795492117.csv) | **Qwen 2.5 3B** | Staggered Batch (`180s` cooldown) | 7 | 32.84 | 9.83 | 512 s | 0.95 W | 5.85 W | 8.13 W | **795.91 J** | 0.2211 Wh | 30.3 → 31.5 (**33.5°C**) |

---

## 2. AlpacaEval Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_K_M`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`alpaca_0`** | [`screenlog.alpaca_0`](./raw/screenlog.alpaca_0) | [`energy_log_1795493026.csv`](./raw/energy_log_1795493026.csv) | **Llama 3.2 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 34.10 | 9.10 | 42 s | 0.79 W | 6.67 W | 8.18 W | **290.39 J** | 0.0807 Wh | 28.8 → 30.6 (**30.6°C**) |
| **`alpaca_1`** | [`screenlog.alpaca_1`](./raw/screenlog.alpaca_1) | [`energy_log_1795493113.csv`](./raw/energy_log_1795493113.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 29.90 | 8.64 | 336 s | 1.08 W | 6.14 W | 8.37 W | **1945.46 J** | 0.5404 Wh | 30.6 → 38.5 (**38.7°C**) |
| **`alpaca_2`** | [`screenlog.alpaca_2`](./raw/screenlog.alpaca_2) | [`energy_log_1795497835.csv`](./raw/energy_log_1795497835.csv) | **Llama 3.2 3B** | Staggered Batch (`180s` cooldown) | 5 | 34.66 | 8.80 | 1085 s | 0.82 W | 6.87 W | 8.73 W | **2375.85 J** | 0.6600 Wh | 23.8 → 32.0 (**32.1°C**) |
| **`alpaca_3`** | [`screenlog.alpaca_3`](./raw/screenlog.alpaca_3) | [`energy_log_1795500269.csv`](./raw/energy_log_1795500269.csv) | **Ministral 3 3B** | Staggered Batch (`180s` cooldown) | 5 | 28.24 | 5.62 | 1745 s | 0.98 W | 6.06 W | 8.06 W | **6118.43 J** | 1.6996 Wh | 26.3 → 40.6 (**40.8°C**) |
| **`alpaca_4`** | [`screenlog.alpaca_4`](./raw/screenlog.alpaca_4) | [`energy_log_1795505662.csv`](./raw/energy_log_1795505662.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 26.32 | 5.40 | 1083 s | 0.91 W | 5.75 W | 8.36 W | **6114.71 J** | 1.6985 Wh | 25.1 → 43.1 (**43.4°C**) |
| **`alpaca_6`** | [`screenlog.alpaca_6`](./raw/screenlog.alpaca_6) | [`energy_log_1795508339.csv`](./raw/energy_log_1795508339.csv) | **Ministral 3 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 29.90 | 5.70 | 219 s | 0.91 W | 6.39 W | 8.40 W | **1293.42 J** | 0.3593 Wh | 27.1 → 35.0 (**35.1°C**) |
| **`alpaca_7`** | [`screenlog.alpaca_7`](./raw/screenlog.alpaca_7) | [`energy_log_1795508582.csv`](./raw/energy_log_1795508582.csv) | **Qwen 2.5 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 32.10 | 9.50 | 66 s | 0.82 W | 6.08 W | 7.49 W | **279.57 J** | 0.0777 Wh | 34.9 → 35.1 (**35.2°C**) |
| **`alpaca_8`** | [`screenlog.alpaca_8`](./raw/screenlog.alpaca_8) | [`energy_log_1795567588.csv`](./raw/energy_log_1795567588.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 31.02 | 9.50 | 290 s | 0.94 W | 6.42 W | 8.48 W | **1739.20 J** | 0.4831 Wh | 26.6 → 35.9 (**36.1°C**) |
| **`alpaca_9`** | [`screenlog.alpaca_9`](./raw/screenlog.alpaca_9) | [`energy_log_1795570073.csv`](./raw/energy_log_1795570073.csv) | **Qwen 2.5 3B** | Staggered Batch (`180s` cooldown) | 5 | 35.80 | 9.70 | 987 s | 0.90 W | 6.92 W | 8.85 W | **1730.37 J** | 0.4807 Wh | 25.0 → 31.0 (**31.0°C**) |

---

## 3. SQuAD 2.0 Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_K_M`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`squad_0`** | [`screenlog.squad_0`](./raw/screenlog.squad_0) | [`energy_log_1795573133.csv`](./raw/energy_log_1795573133.csv) | **Llama 3.2 3B** | Single-Fire (`run_squad_single.py`) | 1 | 34.80 | 11.80 | 31 s | 0.96 W | 5.16 W | 8.42 W | **67.78 J** | 0.0188 Wh | 24.8 → 25.4 (**25.4°C**) |
| **`squad_1`** | [`screenlog.squad_1`](./raw/screenlog.squad_1) | [`energy_log_1795573187.csv`](./raw/energy_log_1795573187.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 33.76 | 12.20 | 67 s | 1.09 W | 5.15 W | 8.05 W | **238.47 J** | 0.0662 Wh | 25.4 → 27.4 (**27.4°C**) |
| **`squad_2`** | [`screenlog.squad_2`](./raw/screenlog.squad_2) | [`energy_log_1795573275.csv`](./raw/energy_log_1795573275.csv) | **Llama 3.2 3B** | Staggered Batch (`60s` cooldown) | 5 | 34.76 | 12.20 | 306 s | 1.13 W | 5.43 W | 8.70 W | **240.89 J** | 0.0669 Wh | 27.4 → 27.3 (**27.4°C**) |
| **`squad_3`** | [`screenlog.squad_3`](./raw/screenlog.squad_3) | [`energy_log_1795574206.csv`](./raw/energy_log_1795574206.csv) | **Ministral 3 3B** | Staggered Batch (`60s` cooldown) | 5 | 29.62 | 9.50 | 398 s | 0.83 W | 6.08 W | 8.83 W | **846.36 J** | 0.2351 Wh | 25.7 → 29.5 (**29.5°C**) |
| **`squad_4`** | [`screenlog.squad_4`](./raw/screenlog.squad_4) | [`energy_log_1795575412.csv`](./raw/energy_log_1795575412.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 28.60 | 9.48 | 161 s | 0.88 W | 5.77 W | 8.07 W | **813.41 J** | 0.2259 Wh | 26.4 → 31.6 (**31.7°C**) |
| **`squad_6`** | [`screenlog.squad_6`](./raw/screenlog.squad_6) | [`energy_log_1795575595.csv`](./raw/energy_log_1795575595.csv) | **Ministral 3 3B** | Single-Fire (`run_squad_single.py`) | 1 | 28.30 | 10.20 | 47 s | 1.02 W | 5.56 W | 8.15 W | **161.04 J** | 0.0447 Wh | 31.6 → 31.5 (**31.6°C**) |
| **`squad_7`** | [`screenlog.squad_7`](./raw/screenlog.squad_7) | [`energy_log_1795575665.csv`](./raw/energy_log_1795575665.csv) | **Qwen 2.5 3B** | Single-Fire (`run_squad_single.py`) | 1 | 33.30 | 10.90 | 31 s | 1.04 W | 4.42 W | 7.64 W | **53.47 J** | 0.0149 Wh | 31.5 → 31.1 (**31.5°C**) |
| **`squad_8`** | [`screenlog.squad_8`](./raw/screenlog.squad_8) | [`energy_log_1795576926.csv`](./raw/energy_log_1795576926.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 34.04 | 11.78 | 67 s | 1.00 W | 5.42 W | 8.45 W | **263.16 J** | 0.0731 Wh | 26.3 → 28.4 (**28.4°C**) |
| **`squad_9`** | [`screenlog.squad_9`](./raw/screenlog.squad_9) | [`energy_log_1795577016.csv`](./raw/energy_log_1795577016.csv) | **Qwen 2.5 3B** | Staggered Batch (`60s` cooldown) | 5 | 35.30 | 11.78 | 307 s | 1.03 W | 5.58 W | 8.43 W | **271.47 J** | 0.0754 Wh | 28.4 → 28.3 (**28.5°C**) |
