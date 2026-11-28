# Moto G Play (2024) (`Q4_0`) Redo: SAMSum, AlpacaEval & SQuAD 2.0 Energy and Inference Analysis

All 27 `energy_log_*.csv` files and 27 `screenlog.*` files (`samsum_0..9`, `alpaca_0..9`, and `squad_0..9`) were pulled from `/data/data/com.termux/files/home/llama.cpp/build-cpu` (and `/data/data/com.termux/files/home/llama.cpp/build-cpu/redo` for the corrected `alpaca_9`, `squad_3`, `squad_4`, and `squad_6` runs) on the **Moto G Play (2024)** (`ZY22J9C8PX`) via `adb pull`, stored in [`raw/`](./raw) and organized by `<Model>/Q4_0/<Benchmark>/Moto G Play (2024)/CPU/`, and analyzed using [`~/energy_analysis_universal.py`](file:///home/aryan/energy_analysis_universal.py).

---

## 1. SAMSum Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_0`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`samsum_0`** | [`screenlog.samsum_0`](./raw/screenlog.samsum_0) | [`energy_log_1795571075.csv`](./raw/energy_log_1795571075.csv) | **Llama 3.2 3B** | Single-Fire (`train_single.csv`) | 1 | 4.20 | 2.40 | 179 s | 1.10 W | 3.06 W | 4.87 W | **492.56 J** | 0.1368 Wh | 24.0 → 25.0 (**25.0°C**) |
| **`samsum_1`** | [`screenlog.samsum_1`](./raw/screenlog.samsum_1) | [`energy_log_1795571277.csv`](./raw/energy_log_1795571277.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 7 | 4.26 | 2.73 | 674 s | 1.12 W | 2.85 W | 5.22 W | **1828.91 J** | 0.5080 Wh | 25.0 → 28.0 (**28.0°C**) |
| **`samsum_2`** | [`screenlog.samsum_2`](./raw/screenlog.samsum_2) | [`energy_log_1795573010.csv`](./raw/energy_log_1795573010.csv) | **Llama 3.2 3B** | Staggered Batch (`180s` cooldown) | 7 | 4.40 | 2.81 | 719 s | 0.87 W | 3.15 W | 5.27 W | **1800.22 J** | 0.5001 Wh | 24.0 → 29.0 (**29.0°C**) |
| **`samsum_3`** | [`screenlog.samsum_3`](./raw/screenlog.samsum_3) | [`energy_log_1795575452.csv`](./raw/energy_log_1795575452.csv) | **Ministral 3 3B** | Staggered Batch (`180s` cooldown) | 7 | 3.64 | 1.83 | 2011 s | 0.85 W | 2.87 W | 5.25 W | **5272.94 J** | 1.4647 Wh | 25.0 → 29.0 (**29.0°C**) |
| **`samsum_4`** | [`screenlog.samsum_4`](./raw/screenlog.samsum_4) | [`energy_log_1795579347.csv`](./raw/energy_log_1795579347.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 7 | 3.76 | 2.01 | 1806 s | 1.05 W | 2.97 W | 5.13 W | **5253.99 J** | 1.4594 Wh | 27.0 → 31.0 (**31.0°C**) |
| **`samsum_6`** | [`screenlog.samsum_6`](./raw/screenlog.samsum_6) | [`energy_log_1795584485.csv`](./raw/energy_log_1795584485.csv) | **Ministral 3 3B** | Single-Fire (`train_single.csv`) | 1 | 4.70 | 2.40 | 284 s | 0.92 W | 3.62 W | 4.41 W | **956.18 J** | 0.2656 Wh | 26.0 → 27.0 (**27.0°C**) |
| **`samsum_7`** | [`screenlog.samsum_7`](./raw/screenlog.samsum_7) | [`energy_log_1795585338.csv`](./raw/energy_log_1795585338.csv) | **Qwen 2.5 3B** | Single-Fire (`train_single.csv`) | 1 | 5.50 | 3.50 | 151 s | 1.04 W | 3.75 W | 5.29 W | **490.03 J** | 0.1361 Wh | 27.0 → 28.0 (**28.0°C**) |
| **`samsum_8`** | [`screenlog.samsum_8`](./raw/screenlog.samsum_8) | [`energy_log_1795586000.csv`](./raw/energy_log_1795586000.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 7 | 4.03 | 2.47 | 753 s | 0.88 W | 2.70 W | 4.61 W | **1899.68 J** | 0.5277 Wh | 28.0 → 30.0 (**30.0°C**) |
| **`samsum_9`** | [`screenlog.samsum_9`](./raw/screenlog.samsum_9) | [`energy_log_1795587787.csv`](./raw/energy_log_1795587787.csv) | **Qwen 2.5 3B** | Staggered Batch (`180s` cooldown) | 7 | 4.07 | 2.76 | 800 s | 0.96 W | 2.82 W | 4.58 W | **1767.82 J** | 0.4911 Wh | 28.0 → 30.0 (**30.0°C**) |

---

## 2. AlpacaEval Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_0`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`alpaca_0`** | [`screenlog.alpaca_0`](./raw/screenlog.alpaca_0) | [`energy_log_1795631229.csv`](./raw/energy_log_1795631229.csv) | **Llama 3.2 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 5.30 | 3.40 | 164 s | 1.07 W | 3.87 W | 4.57 W | **554.30 J** | 0.1540 Wh | 22.0 → 23.0 (**23.0°C**) |
| **`alpaca_1`** | [`screenlog.alpaca_1`](./raw/screenlog.alpaca_1) | [`energy_log_1795631418.csv`](./raw/energy_log_1795631418.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.72 | 2.82 | 970 s | 0.99 W | 3.32 W | 4.71 W | **3144.80 J** | 0.8736 Wh | 23.0 → 28.0 (**28.0°C**) |
| **`alpaca_2`** | [`screenlog.alpaca_2`](./raw/screenlog.alpaca_2) | [`energy_log_1795635083.csv`](./raw/energy_log_1795635083.csv) | **Llama 3.2 3B** | Staggered Batch (`300s` cooldown) | 5 | 4.20 | 2.48 | 2474 s | 0.97 W | 2.85 W | 4.97 W | **3528.42 J** | 0.9801 Wh | 25.0 → 29.0 (**29.0°C**) |
| **`alpaca_3`** | [`screenlog.alpaca_3`](./raw/screenlog.alpaca_3) | [`energy_log_1795639461.csv`](./raw/energy_log_1795639461.csv) | **Ministral 3 3B** | Staggered Batch (`300s` cooldown) | 5 | 4.64 | 2.18 | 4343 s | 1.10 W | 3.47 W | 5.66 W | **10447.77 J** | 2.9022 Wh | 27.0 → 32.0 (**33.0°C**) |
| **`alpaca_4`** | [`screenlog.alpaca_4`](./raw/screenlog.alpaca_4) | [`energy_log_1795646255.csv`](./raw/energy_log_1795646255.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.44 | 2.08 | 4877 s | 0.95 W | 3.14 W | 5.46 W | **12163.07 J** | 3.3786 Wh | 29.0 → 34.0 (**34.0°C**) |
| **`alpaca_6`** | [`screenlog.alpaca_6`](./raw/screenlog.alpaca_6) | [`energy_log_1795653890.csv`](./raw/energy_log_1795653890.csv) | **Ministral 3 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 3.90 | 2.00 | 560 s | 0.94 W | 3.11 W | 4.34 W | **1679.90 J** | 0.4666 Wh | 27.0 → 30.0 (**30.0°C**) |
| **`alpaca_7`** | [`screenlog.alpaca_7`](./raw/screenlog.alpaca_7) | [`energy_log_1795656051.csv`](./raw/energy_log_1795656051.csv) | **Qwen 2.5 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 5.70 | 3.70 | 122 s | 1.07 W | 3.90 W | 4.54 W | **401.68 J** | 0.1116 Wh | 28.0 → 28.0 (**28.0°C**) |
| **`alpaca_8`** | [`screenlog.alpaca_8`](./raw/screenlog.alpaca_8) | [`energy_log_1795656622.csv`](./raw/energy_log_1795656622.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.54 | 2.56 | 1298 s | 0.89 W | 3.06 W | 5.21 W | **3907.68 J** | 1.0855 Wh | 28.0 → 32.0 (**32.0°C**) |
| **`alpaca_9`** | [`screenlog.alpaca_9`](./raw/screenlog.alpaca_9) | [`energy_log_1795725899.csv`](./raw/energy_log_1795725899.csv) | **Qwen 2.5 3B** | Staggered Batch (`300s` cooldown) | 5 | 3.78 | 2.40 | 2406 s | 0.94 W | 2.81 W | 4.01 W | **3318.86 J** | 0.9219 Wh | 28.0 → 28.0 (**29.0°C**) |

---

## 3. SQuAD 2.0 Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_0`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`squad_0`** | [`screenlog.squad_0`](./raw/screenlog.squad_0) | [`energy_log_1795662594.csv`](./raw/energy_log_1795662594.csv) | **Llama 3.2 3B** | Single-Fire (`run_squad_single.py`) | 1 | 5.40 | 4.10 | 54 s | 1.08 W | 3.61 W | 4.52 W | **122.02 J** | 0.0339 Wh | 27.0 → 27.0 (**27.0°C**) |
| **`squad_1`** | [`screenlog.squad_1`](./raw/screenlog.squad_1) | [`energy_log_1795662673.csv`](./raw/energy_log_1795662673.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 3.92 | 3.24 | 239 s | 1.01 W | 2.76 W | 4.50 W | **579.09 J** | 0.1609 Wh | 27.0 → 27.0 (**27.0°C**) |
| **`squad_2`** | [`screenlog.squad_2`](./raw/screenlog.squad_2) | [`energy_log_1795663481.csv`](./raw/energy_log_1795663481.csv) | **Llama 3.2 3B** | Staggered Batch (`60s` cooldown) | 5 | 3.98 | 3.36 | 474 s | 0.92 W | 2.70 W | 4.15 W | **559.03 J** | 0.1553 Wh | 28.0 → 27.0 (**28.0°C**) |
| **`squad_3`** | [`screenlog.squad_3`](./raw/screenlog.squad_3) | [`energy_log_1795730550.csv`](./raw/energy_log_1795730550.csv) | **Ministral 3 3B** | Staggered Batch (`60s` cooldown) | 5 | 3.28 | 2.00 | 1354 s | 1.14 W | 2.63 W | 4.74 W | **2782.76 J** | 0.7730 Wh | 27.0 → 29.0 (**29.0°C**) |
| **`squad_4`** | [`screenlog.squad_4`](./raw/screenlog.squad_4) | [`energy_log_1795734091.csv`](./raw/energy_log_1795734091.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 3.22 | 1.64 | 1074 s | 0.98 W | 2.60 W | 4.60 W | **2702.36 J** | 0.7507 Wh | 28.0 → 30.0 (**30.0°C**) |
| **`squad_6`** | [`screenlog.squad_6`](./raw/screenlog.squad_6) | [`energy_log_1795736948.csv`](./raw/energy_log_1795736948.csv) | **Ministral 3 3B** | Single-Fire (`run_squad_single.py`) | 1 | 4.80 | 3.30 | 159 s | 0.99 W | 3.67 W | 5.04 W | **511.88 J** | 0.1422 Wh | 28.0 → 29.0 (**29.0°C**) |
| **`squad_7`** | [`screenlog.squad_7`](./raw/screenlog.squad_7) | [`energy_log_1795668356.csv`](./raw/energy_log_1795668356.csv) | **Qwen 2.5 3B** | Single-Fire (`run_squad_single.py`) | 1 | 3.90 | 2.80 | 45 s | 0.95 W | 2.73 W | 4.11 W | **125.25 J** | 0.0348 Wh | 27.0 → 27.0 (**27.0°C**) |
| **`squad_8`** | [`screenlog.squad_8`](./raw/screenlog.squad_8) | [`energy_log_1795668447.csv`](./raw/energy_log_1795668447.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 3.80 | 3.04 | 242 s | 1.02 W | 2.67 W | 3.37 W | **573.90 J** | 0.1594 Wh | 27.0 → 27.0 (**27.0°C**) |
| **`squad_9`** | [`screenlog.squad_9`](./raw/screenlog.squad_9) | [`energy_log_1795668713.csv`](./raw/energy_log_1795668713.csv) | **Qwen 2.5 3B** | Staggered Batch (`60s` cooldown) | 5 | 3.84 | 2.84 | 482 s | 0.99 W | 2.64 W | 3.56 W | **568.21 J** | 0.1578 Wh | 27.0 → 28.0 (**28.0°C**) |
