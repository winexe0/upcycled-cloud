# LG G7 ThinQ (`Q4_0`) Redo: SAMSum, AlpacaEval & SQuAD 2.0 Energy and Inference Analysis

All 27 `energy_log_*.csv` files and 27 `screenlog.*` files (`samsum_0..9`, `alpaca_0..9`, and `squad_0..9`) were pulled from `/data/data/com.termux/files/home/llama.cpp/build-cpu` on the **LG G7 ThinQ** (`LMG710ULM6eca37e0`) via `adb pull`, stored in [`raw/`](./raw) and organized by `<Model>/Q4_0/<Benchmark>/LG G7 ThinQ/CPU/`, and analyzed using [`~/energy_analysis_universal.py`](file:///home/aryan/energy_analysis_universal.py).

---

## 1. SAMSum Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_0`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`samsum_0`** | [`screenlog.samsum_0`](./raw/screenlog.samsum_0) | [`energy_log_1795571100.csv`](./raw/energy_log_1795571100.csv) | **Llama 3.2 3B** | Single-Fire (`train_single.csv`) | 1 | 5.00 | 2.00 | 168 s | 1.63 W | 5.02 W | 6.99 W | **739.41 J** | 0.2054 Wh | 23.9 → 28.5 (**29.0°C**) |
| **`samsum_1`** | [`screenlog.samsum_1`](./raw/screenlog.samsum_1) | [`energy_log_1795571533.csv`](./raw/energy_log_1795571533.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 7 | 4.61 | 2.27 | 603 s | 1.20 W | 4.67 W | 6.84 W | **2724.22 J** | 0.7567 Wh | 26.7 → 35.2 (**35.9°C**) |
| **`samsum_2`** | [`screenlog.samsum_2`](./raw/screenlog.samsum_2) | [`energy_log_1795573858.csv`](./raw/energy_log_1795573858.csv) | **Llama 3.2 3B** | Staggered Batch (`180s` cooldown) | 7 | 4.80 | 2.34 | 710 s | 1.10 W | 4.60 W | 7.07 W | **2616.59 J** | 0.7268 Wh | 24.4 → 33.6 (**34.9°C**) |
| **`samsum_3`** | [`screenlog.samsum_3`](./raw/screenlog.samsum_3) | [`energy_log_1795575681.csv`](./raw/energy_log_1795575681.csv) | **Ministral 3 3B** | Staggered Batch (`180s` cooldown) | 7 | 4.19 | 1.10 | 1929 s | 1.05 W | 4.40 W | 6.02 W | **7874.59 J** | 2.1874 Wh | 26.6 → 40.6 (**42.1°C**) |
| **`samsum_4`** | [`screenlog.samsum_4`](./raw/screenlog.samsum_4) | [`energy_log_1795579812.csv`](./raw/energy_log_1795579812.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 7 | 4.01 | 1.01 | 3086 s | 1.11 W | 3.98 W | 5.81 W | **7453.71 J** | 2.0705 Wh | 27.3 → 29.2 (**42.0°C**) |
| **`samsum_6`** | [`screenlog.samsum_6`](./raw/screenlog.samsum_6) | [`energy_log_1795584679.csv`](./raw/energy_log_1795584679.csv) | **Ministral 3 3B** | Single-Fire (`train_single.csv`) | 1 | 4.70 | 0.90 | 370 s | 1.41 W | 4.84 W | 6.74 W | **1693.37 J** | 0.4704 Wh | 28.1 → 35.6 (**36.4°C**) |
| **`samsum_7`** | [`screenlog.samsum_7`](./raw/screenlog.samsum_7) | [`energy_log_1795585619.csv`](./raw/energy_log_1795585619.csv) | **Qwen 2.5 3B** | Single-Fire (`train_single.csv`) | 1 | 4.80 | 2.90 | 167 s | 1.46 W | 4.68 W | 6.12 W | **688.64 J** | 0.1913 Wh | 30.7 → 32.9 (**33.8°C**) |
| **`samsum_8`** | [`screenlog.samsum_8`](./raw/screenlog.samsum_8) | [`energy_log_1795586356.csv`](./raw/energy_log_1795586356.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 7 | 4.04 | 2.63 | 635 s | 0.92 W | 4.20 W | 5.65 W | **2678.93 J** | 0.7441 Wh | 28.8 → 37.3 (**37.9°C**) |
| **`samsum_9`** | [`screenlog.samsum_9`](./raw/screenlog.samsum_9) | [`energy_log_1795587944.csv`](./raw/energy_log_1795587944.csv) | **Qwen 2.5 3B** | Staggered Batch (`180s` cooldown) | 7 | 4.47 | 3.04 | 686 s | 1.08 W | 4.49 W | 6.21 W | **2539.06 J** | 0.7053 Wh | 29.6 → 36.3 (**37.2°C**) |

---

## 2. AlpacaEval Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_0`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`alpaca_0`** | [`screenlog.alpaca_0`](./raw/screenlog.alpaca_0) | [`energy_log_1795631217.csv`](./raw/energy_log_1795631217.csv) | **Llama 3.2 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 4.90 | 2.80 | 156 s | 1.15 W | 5.29 W | 7.14 W | **728.92 J** | 0.2025 Wh | 23.9 → 27.9 (**28.6°C**) |
| **`alpaca_1`** | [`screenlog.alpaca_1`](./raw/screenlog.alpaca_1) | [`energy_log_1795631942.csv`](./raw/energy_log_1795631942.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.50 | 2.66 | 995 s | 1.01 W | 4.71 W | 7.26 W | **4603.91 J** | 1.2789 Wh | 26.3 → 39.6 (**40.7°C**) |
| **`alpaca_2`** | [`screenlog.alpaca_2`](./raw/screenlog.alpaca_2) | [`energy_log_1795635082.csv`](./raw/energy_log_1795635082.csv) | **Llama 3.2 3B** | Staggered Batch (`180s` cooldown) | 5 | 5.10 | 2.98 | 2058 s | 1.11 W | 5.01 W | 7.58 W | **4339.71 J** | 1.2055 Wh | 25.6 → 35.9 (**36.8°C**) |
| **`alpaca_3`** | [`screenlog.alpaca_3`](./raw/screenlog.alpaca_3) | [`energy_log_1795638517.csv`](./raw/energy_log_1795638517.csv) | **Ministral 3 3B** | Staggered Batch (`180s` cooldown) | 5 | 3.98 | 0.96 | 8167 s | 1.20 W | 4.30 W | 6.78 W | **26976.02 J** | 7.4933 Wh | 29.5 → 48.4 (**49.2°C**) |
| **`alpaca_4`** | [`screenlog.alpaca_4`](./raw/screenlog.alpaca_4) | [`energy_log_1795651374.csv`](./raw/energy_log_1795651374.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 3.98 | 1.08 | 5517 s | 0.99 W | 4.36 W | 7.05 W | **21159.58 J** | 5.8777 Wh | 28.5 → 47.7 (**48.8°C**) |
| **`alpaca_6`** | [`screenlog.alpaca_6`](./raw/screenlog.alpaca_6) | [`energy_log_1795660751.csv`](./raw/energy_log_1795660751.csv) | **Ministral 3 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 4.30 | 1.40 | 566 s | 1.04 W | 4.70 W | 5.97 W | **2578.10 J** | 0.7161 Wh | 28.5 → 37.9 (**38.8°C**) |
| **`alpaca_7`** | [`screenlog.alpaca_7`](./raw/screenlog.alpaca_7) | [`energy_log_1795662370.csv`](./raw/energy_log_1795662370.csv) | **Qwen 2.5 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 5.10 | 3.20 | 163 s | 1.22 W | 4.98 W | 5.92 W | **718.27 J** | 0.1995 Wh | 28.5 → 31.7 (**32.5°C**) |
| **`alpaca_8`** | [`screenlog.alpaca_8`](./raw/screenlog.alpaca_8) | [`energy_log_1795662557.csv`](./raw/energy_log_1795662557.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 3.98 | 2.60 | 1235 s | 1.34 W | 4.35 W | 6.04 W | **5285.86 J** | 1.4683 Wh | 31.5 → 40.9 (**41.6°C**) |
| **`alpaca_9`** | [`screenlog.alpaca_9`](./raw/screenlog.alpaca_9) | [`energy_log_1795667941.csv`](./raw/energy_log_1795667941.csv) | **Qwen 2.5 3B** | Staggered Batch (`180s` cooldown) | 5 | 4.88 | 2.98 | 2319 s | 1.01 W | 4.89 W | 6.50 W | **5348.41 J** | 1.4857 Wh | 25.6 → 34.2 (**36.8°C**) |

---

## 3. SQuAD 2.0 Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_0`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`squad_0`** | [`screenlog.squad_0`](./raw/screenlog.squad_0) | [`energy_log_1795671769.csv`](./raw/energy_log_1795671769.csv) | **Llama 3.2 3B** | Single-Fire (`run_squad_single.py`) | 1 | 4.90 | 1.30 | 62 s | 1.06 W | 4.88 W | 5.99 W | **214.48 J** | 0.0596 Wh | 27.9 → 28.5 (**28.9°C**) |
| **`squad_1`** | [`screenlog.squad_1`](./raw/screenlog.squad_1) | [`energy_log_1795671856.csv`](./raw/energy_log_1795671856.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.52 | 1.40 | 230 s | 1.19 W | 4.41 W | 5.90 W | **938.40 J** | 0.2607 Wh | 28.3 → 31.6 (**32.3°C**) |
| **`squad_2`** | [`screenlog.squad_2`](./raw/screenlog.squad_2) | [`energy_log_1795672716.csv`](./raw/energy_log_1795672716.csv) | **Llama 3.2 3B** | Staggered Batch (`60s` cooldown) | 5 | 4.96 | 1.42 | 461 s | 1.18 W | 4.69 W | 7.51 W | **953.38 J** | 0.2648 Wh | 28.8 → 31.6 (**32.1°C**) |
| **`squad_3`** | [`screenlog.squad_3`](./raw/screenlog.squad_3) | [`energy_log_1795674049.csv`](./raw/energy_log_1795674049.csv) | **Ministral 3 3B** | Staggered Batch (`60s` cooldown) | 2 | 4.05 | 0.60 | 42 s | 4.44 W | 5.57 W | 6.05 W | **105.63 J** | 0.0293 Wh | 32.5 → 34.7 (**35.5°C**) |
| **`squad_4`** | [`screenlog.squad_4`](./raw/screenlog.squad_4) | [`energy_log_1795675180.csv`](./raw/energy_log_1795675180.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 3.78 | 0.68 | 964 s | 1.20 W | 4.08 W | 6.19 W | **3857.39 J** | 1.0715 Wh | 29.7 → 37.9 (**38.7°C**) |
| **`squad_6`** | [`screenlog.squad_6`](./raw/screenlog.squad_6) | [`energy_log_1795675224.csv`](./raw/energy_log_1795675224.csv) | **Ministral 3 3B** | Single-Fire (`run_squad_single.py`) | 1 | 5.00 | 0.80 | 164 s | 0.82 W | 4.72 W | 6.64 W | **688.04 J** | 0.1911 Wh | 24.4 → 28.2 (**29.0°C**) |
| **`squad_7`** | [`screenlog.squad_7`](./raw/screenlog.squad_7) | [`energy_log_1795675268.csv`](./raw/energy_log_1795675268.csv) | **Qwen 2.5 3B** | Single-Fire (`run_squad_single.py`) | 1 | 5.00 | 3.30 | 55 s | 1.37 W | 4.74 W | 5.87 W | **171.81 J** | 0.0477 Wh | 26.9 → 28.1 (**28.5°C**) |
| **`squad_8`** | [`screenlog.squad_8`](./raw/screenlog.squad_8) | [`energy_log_1795675346.csv`](./raw/energy_log_1795675346.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.62 | 3.62 | 208 s | 1.28 W | 4.54 W | 6.43 W | **852.28 J** | 0.2367 Wh | 28.1 → 31.9 (**32.5°C**) |
| **`squad_9`** | [`screenlog.squad_9`](./raw/screenlog.squad_9) | [`energy_log_1795675578.csv`](./raw/energy_log_1795675578.csv) | **Qwen 2.5 3B** | Staggered Batch (`60s` cooldown) | 5 | 4.84 | 3.52 | 467 s | 1.30 W | 4.55 W | 6.33 W | **854.66 J** | 0.2374 Wh | 31.6 → 32.8 (**33.2°C**) |
