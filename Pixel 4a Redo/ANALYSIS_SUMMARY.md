# Google Pixel 4a (`Q4_K_M`) Redo: SAMSum, AlpacaEval & SQuAD 2.0 Energy and Inference Analysis

All 27 `energy_log_*.csv` files and 27 `screenlog.*` files (`samsum_0..9`, `alpaca_0..9`, and `squad_0..9`) were pulled from `/data/data/com.termux/files/home/llama.cpp/build-cpu` on the **Google Pixel 4a** (`08101JEC211208`) via `adb pull`, stored in [`raw/`](./raw) and organized by `<Model>/Q4_K_M/<Benchmark>/Pixel 4a/CPU/`, and analyzed using [`~/energy_analysis_universal.py`](file:///home/aryan/energy_analysis_universal.py).

---

## 1. SAMSum Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_K_M`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`samsum_0`** | [`screenlog.samsum_0`](./raw/screenlog.samsum_0) | [`energy_log_1795486255.csv`](./raw/energy_log_1795486255.csv) | **Llama 3.2 3B** | Single-Fire (`train_single.csv`) | 1 | 15.30 | 3.20 | 102 s | 0.89 W | 4.28 W | 6.19 W | **288.96 J** | 0.0803 Wh | 31.3 → 31.2 (**32.1°C**) |
| **`samsum_1`** | [`screenlog.samsum_1`](./raw/screenlog.samsum_1) | [`energy_log_1795486724.csv`](./raw/energy_log_1795486724.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 7 | 15.51 | 4.03 | 295 s | 1.36 W | 4.80 W | 6.70 W | **1221.21 J** | 0.3392 Wh | 29.1 → 31.6 (**32.1°C**) |
| **`samsum_2`** | [`screenlog.samsum_2`](./raw/screenlog.samsum_2) | [`energy_log_1795487406.csv`](./raw/energy_log_1795487406.csv) | **Llama 3.2 3B** | Staggered Batch (`180s` cooldown) | 7 | 15.53 | 4.00 | 674 s | 1.08 W | 4.45 W | 7.37 W | **1255.80 J** | 0.3488 Wh | 29.3 → 29.9 (**30.6°C**) |
| **`samsum_3`** | [`screenlog.samsum_3`](./raw/screenlog.samsum_3) | [`energy_log_1795488505.csv`](./raw/energy_log_1795488505.csv) | **Ministral 3 3B** | Staggered Batch (`180s` cooldown) | 7 | 13.56 | 2.50 | 1081 s | 1.05 W | 4.41 W | 7.29 W | **2994.12 J** | 0.8317 Wh | 28.1 → 32.7 (**33.8°C**) |
| **`samsum_4`** | [`screenlog.samsum_4`](./raw/screenlog.samsum_4) | [`energy_log_1795491099.csv`](./raw/energy_log_1795491099.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 7 | 13.54 | 2.51 | 699 s | 0.69 W | 4.15 W | 7.45 W | **2818.06 J** | 0.7828 Wh | 25.6 → 33.5 (**34.0°C**) |
| **`samsum_6`** | [`screenlog.samsum_6`](./raw/screenlog.samsum_6) | [`energy_log_1795492968.csv`](./raw/energy_log_1795492968.csv) | **Ministral 3 3B** | Single-Fire (`train_single.csv`) | 1 | 13.10 | 2.20 | 154 s | 0.90 W | 4.72 W | 7.48 W | **635.03 J** | 0.1764 Wh | 26.8 → 27.9 (**28.3°C**) |
| **`samsum_7`** | [`screenlog.samsum_7`](./raw/screenlog.samsum_7) | [`energy_log_1795493145.csv`](./raw/energy_log_1795493145.csv) | **Qwen 2.5 3B** | Single-Fire (`train_single.csv`) | 1 | 15.30 | 4.00 | 114 s | 0.92 W | 4.73 W | 7.51 W | **345.62 J** | 0.0960 Wh | 28.0 → 29.2 (**29.8°C**) |
| **`samsum_8`** | [`screenlog.samsum_8`](./raw/screenlog.samsum_8) | [`energy_log_1795493261.csv`](./raw/energy_log_1795493261.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 7 | 15.49 | 4.49 | 308 s | 0.75 W | 4.21 W | 6.64 W | **1138.26 J** | 0.3162 Wh | 29.3 → 32.2 (**32.7°C**) |
| **`samsum_9`** | [`screenlog.samsum_9`](./raw/screenlog.samsum_9) | [`energy_log_1795497469.csv`](./raw/energy_log_1795497469.csv) | **Qwen 2.5 3B** | Staggered Batch (`180s` cooldown) | 7 | 15.47 | 4.47 | 625 s | 0.92 W | 4.66 W | 6.58 W | **1243.90 J** | 0.3455 Wh | 22.8 → 26.8 (**27.5°C**) |

---

## 2. AlpacaEval Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_K_M`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`alpaca_0`** | [`screenlog.alpaca_0`](./raw/screenlog.alpaca_0) | [`energy_log_1795500302.csv`](./raw/energy_log_1795500302.csv) | **Llama 3.2 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 15.30 | 3.90 | 125 s | 0.80 W | 4.69 W | 5.91 W | **440.62 J** | 0.1224 Wh | 22.8 → 24.0 (**24.5°C**) |
| **`alpaca_1`** | [`screenlog.alpaca_1`](./raw/screenlog.alpaca_1) | [`energy_log_1795500434.csv`](./raw/energy_log_1795500434.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 15.30 | 3.78 | 699 s | 0.74 W | 4.40 W | 7.01 W | **3002.88 J** | 0.8341 Wh | 24.1 → 33.3 (**33.8°C**) |
| **`alpaca_2`** | [`screenlog.alpaca_2`](./raw/screenlog.alpaca_2) | [`energy_log_1795502426.csv`](./raw/energy_log_1795502426.csv) | **Llama 3.2 3B** | Staggered Batch (`180s` cooldown) | 5 | 15.36 | 3.72 | 1512 s | 1.31 W | 4.68 W | 7.01 W | **3565.77 J** | 0.9905 Wh | 27.5 → 32.9 (**33.3°C**) |
| **`alpaca_3`** | [`screenlog.alpaca_3`](./raw/screenlog.alpaca_3) | [`energy_log_1795506769.csv`](./raw/energy_log_1795506769.csv) | **Ministral 3 3B** | Staggered Batch (`180s` cooldown) | 5 | 13.62 | 1.98 | 7631 s | 1.30 W | 3.80 W | 7.09 W | **14383.33 J** | 3.9954 Wh | 25.2 → 18.6 (**35.8°C**) |
| **`alpaca_4`** | [`screenlog.alpaca_4`](./raw/screenlog.alpaca_4) | [`energy_log_1795547544.csv`](./raw/energy_log_1795547544.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 13.54 | 2.00 | 4775 s | 1.03 W | 3.93 W | 7.17 W | **11624.79 J** | 3.2291 Wh | 21.8 → 33.8 (**35.8°C**) |
| **`alpaca_6`** | [`screenlog.alpaca_6`](./raw/screenlog.alpaca_6) | [`energy_log_1795555265.csv`](./raw/energy_log_1795555265.csv) | **Ministral 3 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 13.80 | 2.10 | 456 s | 1.07 W | 4.52 W | 6.14 W | **1977.11 J** | 0.5492 Wh | 24.4 → 31.1 (**31.6°C**) |
| **`alpaca_7`** | [`screenlog.alpaca_7`](./raw/screenlog.alpaca_7) | [`energy_log_1795556470.csv`](./raw/energy_log_1795556470.csv) | **Qwen 2.5 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 15.30 | 4.30 | 136 s | 1.11 W | 5.09 W | 7.21 W | **503.46 J** | 0.1399 Wh | 28.2 → 29.0 (**29.6°C**) |
| **`alpaca_8`** | [`screenlog.alpaca_8`](./raw/screenlog.alpaca_8) | [`energy_log_1795570083.csv`](./raw/energy_log_1795570083.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 15.32 | 4.32 | 630 s | 1.19 W | 4.60 W | 6.50 W | **2720.23 J** | 0.7556 Wh | 25.1 → 33.4 (**33.9°C**) |
| **`alpaca_9`** | [`screenlog.alpaca_9`](./raw/screenlog.alpaca_9) | [`energy_log_1795571946.csv`](./raw/energy_log_1795571946.csv) | **Qwen 2.5 3B** | Staggered Batch (`180s` cooldown) | 5 | 15.36 | 4.26 | 1402 s | 0.98 W | 4.90 W | 7.28 W | **3204.88 J** | 0.8902 Wh | 27.6 → 31.7 (**32.3°C**) |

---

## 3. SQuAD 2.0 Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_K_M`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`squad_0`** | [`screenlog.squad_0`](./raw/screenlog.squad_0) | [`energy_log_1795574639.csv`](./raw/energy_log_1795574639.csv) | **Llama 3.2 3B** | Single-Fire (`run_squad_single.py`) | 1 | 15.30 | 5.50 | 62 s | 0.98 W | 4.03 W | 6.08 W | **84.64 J** | 0.0235 Wh | 25.9 → 26.1 (**26.5°C**) |
| **`squad_1`** | [`screenlog.squad_1`](./raw/screenlog.squad_1) | [`energy_log_1795574703.csv`](./raw/energy_log_1795574703.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 15.38 | 5.58 | 126 s | 0.98 W | 4.08 W | 7.15 W | **354.67 J** | 0.0985 Wh | 26.1 → 27.3 (**27.7°C**) |
| **`squad_2`** | [`screenlog.squad_2`](./raw/screenlog.squad_2) | [`energy_log_1795574831.csv`](./raw/energy_log_1795574831.csv) | **Llama 3.2 3B** | Staggered Batch (`60s` cooldown) | 5 | 15.38 | 5.58 | 364 s | 0.80 W | 4.00 W | 6.93 W | **345.28 J** | 0.0959 Wh | 27.3 → 28.3 (**28.7°C**) |
| **`squad_3`** | [`screenlog.squad_3`](./raw/screenlog.squad_3) | [`energy_log_1795575198.csv`](./raw/energy_log_1795575198.csv) | **Ministral 3 3B** | Staggered Batch (`60s` cooldown) | 5 | 13.78 | 3.50 | 564 s | 0.77 W | 4.76 W | 7.02 W | **1438.51 J** | 0.3996 Wh | 28.4 → 31.5 (**32.3°C**) |
| **`squad_4`** | [`screenlog.squad_4`](./raw/screenlog.squad_4) | [`energy_log_1795576916.csv`](./raw/energy_log_1795576916.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 13.78 | 3.56 | 324 s | 0.82 W | 4.60 W | 6.45 W | **1289.84 J** | 0.3583 Wh | 27.1 → 31.8 (**32.0°C**) |
| **`squad_6`** | [`screenlog.squad_6`](./raw/screenlog.squad_6) | [`energy_log_1795577604.csv`](./raw/energy_log_1795577604.csv) | **Ministral 3 3B** | Single-Fire (`run_squad_single.py`) | 1 | 13.60 | 3.60 | 97 s | 0.76 W | 4.57 W | 7.20 W | **270.77 J** | 0.0752 Wh | 30.0 → 30.0 (**30.8°C**) |
| **`squad_7`** | [`screenlog.squad_7`](./raw/screenlog.squad_7) | [`energy_log_1795577704.csv`](./raw/energy_log_1795577704.csv) | **Qwen 2.5 3B** | Single-Fire (`run_squad_single.py`) | 1 | 15.50 | 5.00 | 62 s | 0.66 W | 3.68 W | 7.05 W | **88.05 J** | 0.0245 Wh | 30.0 → 30.1 (**30.5°C**) |
| **`squad_8`** | [`screenlog.squad_8`](./raw/screenlog.squad_8) | [`energy_log_1795577768.csv`](./raw/energy_log_1795577768.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 15.40 | 5.38 | 128 s | 0.95 W | 4.23 W | 6.23 W | **391.08 J** | 0.1086 Wh | 30.1 → 30.7 (**31.2°C**) |
| **`squad_9`** | [`screenlog.squad_9`](./raw/screenlog.squad_9) | [`energy_log_1795577897.csv`](./raw/energy_log_1795577897.csv) | **Qwen 2.5 3B** | Staggered Batch (`60s` cooldown) | 5 | 15.38 | 5.30 | 347 s | 1.24 W | 4.28 W | 6.23 W | **367.01 J** | 0.1019 Wh | 30.7 → 30.2 (**31.3°C**) |
