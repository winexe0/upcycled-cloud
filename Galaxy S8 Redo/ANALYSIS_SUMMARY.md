# Samsung Galaxy S8 (`Q4_0`) Redo: SAMSum, AlpacaEval & SQuAD 2.0 Energy and Inference Analysis

All 27 `energy_log_*.csv` files and 27 `screenlog.*` files (`samsum_0..9`, `alpaca_0..9`, and `squad_0..9`) were pulled from `/data/data/com.termux/files/home/llama.cpp/build-cpu` on the **Samsung Galaxy S8** (`ce0317139c75ac840c`) via `adb pull`, stored in [`raw/`](./raw) and organized by `<Model>/Q4_0/<Benchmark>/Galaxy S8/CPU/`, and analyzed using [`~/energy_analysis_universal.py`](file:///home/aryan/energy_analysis_universal.py).

---

## 1. SAMSum Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_0`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`samsum_0`** | [`screenlog.samsum_0`](./raw/screenlog.samsum_0) | [`energy_log_1795570565.csv`](./raw/energy_log_1795570565.csv) | **Llama 3.2 3B** | Single-Fire (`train_single.csv`) | 1 | 4.90 | 1.80 | 194 s | 0.96 W | 5.38 W | 6.40 W | **807.41 J** | 0.2243 Wh | 28.3 → 30.7 (**30.7°C**) |
| **`samsum_1`** | [`screenlog.samsum_1`](./raw/screenlog.samsum_1) | [`energy_log_1795571373.csv`](./raw/energy_log_1795571373.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 7 | 4.93 | 1.91 | 640 s | 1.03 W | 5.30 W | 6.95 W | **3162.57 J** | 0.8785 Wh | 28.3 → 36.6 (**36.6°C**) |
| **`samsum_2`** | [`screenlog.samsum_2`](./raw/screenlog.samsum_2) | [`energy_log_1795572872.csv`](./raw/energy_log_1795572872.csv) | **Llama 3.2 3B** | Staggered Batch (`180s` cooldown) | 7 | 4.93 | 1.91 | 741 s | 0.92 W | 5.30 W | 7.11 W | **3159.22 J** | 0.8776 Wh | 28.0 → 34.9 (**35.0°C**) |
| **`samsum_3`** | [`screenlog.samsum_3`](./raw/screenlog.samsum_3) | [`energy_log_1795574433.csv`](./raw/energy_log_1795574433.csv) | **Ministral 3 3B** | Staggered Batch (`180s` cooldown) | 7 | 4.33 | 1.51 | 1708 s | 0.66 W | 5.34 W | 7.91 W | **8449.11 J** | 2.3470 Wh | 30.0 → 41.6 (**41.9°C**) |
| **`samsum_4`** | [`screenlog.samsum_4`](./raw/screenlog.samsum_4) | [`energy_log_1795578132.csv`](./raw/energy_log_1795578132.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 7 | 4.34 | 1.39 | 1689 s | 1.02 W | 5.31 W | 7.15 W | **8719.95 J** | 2.4222 Wh | 25.6 → 41.6 (**41.6°C**) |
| **`samsum_6`** | [`screenlog.samsum_6`](./raw/screenlog.samsum_6) | [`energy_log_1795582881.csv`](./raw/energy_log_1795582881.csv) | **Ministral 3 3B** | Single-Fire (`train_single.csv`) | 1 | 4.40 | 1.40 | 342 s | 0.65 W | 5.48 W | 8.04 W | **1682.30 J** | 0.4673 Wh | 25.9 → 31.6 (**31.6°C**) |
| **`samsum_7`** | [`screenlog.samsum_7`](./raw/screenlog.samsum_7) | [`energy_log_1795583902.csv`](./raw/energy_log_1795583902.csv) | **Qwen 2.5 3B** | Single-Fire (`train_single.csv`) | 1 | 5.00 | 2.00 | 183 s | 1.06 W | 4.99 W | 6.59 W | **817.31 J** | 0.2270 Wh | 25.6 → 28.7 (**28.7°C**) |
| **`samsum_8`** | [`screenlog.samsum_8`](./raw/screenlog.samsum_8) | [`energy_log_1795584539.csv`](./raw/energy_log_1795584539.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 7 | 5.03 | 2.09 | 628 s | 0.89 W | 5.15 W | 7.57 W | **3132.35 J** | 0.8701 Wh | 25.3 → 35.0 (**35.0°C**) |
| **`samsum_9`** | [`screenlog.samsum_9`](./raw/screenlog.samsum_9) | [`energy_log_1795586046.csv`](./raw/energy_log_1795586046.csv) | **Qwen 2.5 3B** | Staggered Batch (`180s` cooldown) | 7 | 5.06 | 2.09 | 747 s | 0.88 W | 5.20 W | 6.76 W | **3148.21 J** | 0.8745 Wh | 29.3 → 37.2 (**37.3°C**) |

---

## 2. AlpacaEval Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_0`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`alpaca_0`** | [`screenlog.alpaca_0`](./raw/screenlog.alpaca_0) | [`energy_log_1795630627.csv`](./raw/energy_log_1795630627.csv) | **Llama 3.2 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 5.00 | 1.90 | 272 s | 0.95 W | 4.63 W | 6.08 W | **1062.61 J** | 0.2952 Wh | 26.0 → 28.4 (**28.4°C**) |
| **`alpaca_1`** | [`screenlog.alpaca_1`](./raw/screenlog.alpaca_1) | [`energy_log_1795631268.csv`](./raw/energy_log_1795631268.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.92 | 1.86 | 1403 s | 0.85 W | 4.89 W | 6.53 W | **6650.44 J** | 1.8473 Wh | 26.4 → 39.8 (**39.8°C**) |
| **`alpaca_2`** | [`screenlog.alpaca_2`](./raw/screenlog.alpaca_2) | [`energy_log_1795635034.csv`](./raw/energy_log_1795635034.csv) | **Llama 3.2 3B** | Staggered Batch (`300s` cooldown) | 5 | 4.94 | 1.88 | 2549 s | 0.79 W | 4.77 W | 6.59 W | **6357.08 J** | 1.7659 Wh | 26.9 → 36.5 (**36.5°C**) |
| **`alpaca_3`** | [`screenlog.alpaca_3`](./raw/screenlog.alpaca_3) | [`energy_log_1795641853.csv`](./raw/energy_log_1795641853.csv) | **Ministral 3 3B** | Staggered Batch (`300s` cooldown) | 5 | 4.38 | 0.86 | 8397 s | 0.89 W | 4.57 W | 7.93 W | **30994.87 J** | 8.6097 Wh | 25.7 → 41.2 (**43.7°C**) |
| **`alpaca_4`** | [`screenlog.alpaca_4`](./raw/screenlog.alpaca_4) | [`energy_log_1795656768.csv`](./raw/energy_log_1795656768.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.30 | 1.24 | 4880 s | 1.00 W | 4.69 W | 6.91 W | **22800.50 J** | 6.3335 Wh | 27.6 → 44.8 (**45.2°C**) |
| **`alpaca_6`** | [`screenlog.alpaca_6`](./raw/screenlog.alpaca_6) | [`energy_log_1795665762.csv`](./raw/energy_log_1795665762.csv) | **Ministral 3 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 4.50 | 1.40 | 689 s | 0.88 W | 4.83 W | 6.81 W | **3251.45 J** | 0.9032 Wh | 29.1 → 37.6 (**37.6°C**) |
| **`alpaca_7`** | [`screenlog.alpaca_7`](./raw/screenlog.alpaca_7) | [`energy_log_1795669226.csv`](./raw/energy_log_1795669226.csv) | **Qwen 2.5 3B** | Single-Fire (`run_alpaca_single.py`) | 1 | 5.00 | 2.10 | 216 s | 0.83 W | 4.63 W | 5.87 W | **828.28 J** | 0.2301 Wh | 27.6 → 30.2 (**30.2°C**) |
| **`alpaca_8`** | [`screenlog.alpaca_8`](./raw/screenlog.alpaca_8) | [`energy_log_1795670177.csv`](./raw/energy_log_1795670177.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.96 | 2.00 | 1446 s | 0.86 W | 5.01 W | 6.71 W | **7026.05 J** | 1.9517 Wh | 27.3 → 41.3 (**41.6°C**) |
| **`alpaca_9`** | [`screenlog.alpaca_9`](./raw/screenlog.alpaca_9) | [`energy_log_1795673519.csv`](./raw/energy_log_1795673519.csv) | **Qwen 2.5 3B** | Staggered Batch (`300s` cooldown) | 5 | 5.04 | 2.02 | 2842 s | 0.68 W | 4.88 W | 6.07 W | **7788.52 J** | 2.1635 Wh | 29.3 → 36.0 (**36.9°C**) |

---

## 3. SQuAD 2.0 Benchmark Suite (9 Runs)

| Run ID | Screen Log | Energy Log | Model (`Q4_0`) | Protocol | Prompts | Prompt (t/s) | Gen (t/s) | Active Duration (s) | Idle Baseline (W) | Avg Active Power (W) | Peak Power (W) | Total Energy (J) | Total Energy (Wh) | Temp Start → End (Max °C) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`squad_0`** | [`screenlog.squad_0`](./raw/screenlog.squad_0) | [`energy_log_1795678149.csv`](./raw/energy_log_1795678149.csv) | **Llama 3.2 3B** | Single-Fire (`run_squad_single.py`) | 1 | 5.00 | 2.20 | 60 s | 0.98 W | 4.84 W | 5.90 W | **205.04 J** | 0.0570 Wh | 28.8 → 29.2 (**29.2°C**) |
| **`squad_1`** | [`screenlog.squad_1`](./raw/screenlog.squad_1) | [`energy_log_1795678234.csv`](./raw/energy_log_1795678234.csv) | **Llama 3.2 3B** | Continuous Batch (`0s` cooldown) | 5 | 5.00 | 2.32 | 195 s | 0.79 W | 5.35 W | 6.85 W | **952.46 J** | 0.2646 Wh | 29.2 → 32.4 (**32.4°C**) |
| **`squad_2`** | [`screenlog.squad_2`](./raw/screenlog.squad_2) | [`energy_log_1795679070.csv`](./raw/energy_log_1795679070.csv) | **Llama 3.2 3B** | Staggered Batch (`60s` cooldown) | 5 | 5.00 | 2.34 | 440 s | 0.85 W | 5.23 W | 6.57 W | **932.19 J** | 0.2589 Wh | 29.0 → 30.7 (**30.7°C**) |
| **`squad_3`** | [`screenlog.squad_3`](./raw/screenlog.squad_3) | [`energy_log_1795683654.csv`](./raw/energy_log_1795683654.csv) | **Ministral 3 3B** | Staggered Batch (`60s` cooldown) | 5 | 4.48 | 1.30 | 1110 s | 1.01 W | 5.67 W | 7.62 W | **4900.75 J** | 1.3613 Wh | 24.4 → 36.9 (**36.9°C**) |
| **`squad_4`** | [`screenlog.squad_4`](./raw/screenlog.squad_4) | [`energy_log_1795683938.csv`](./raw/energy_log_1795683938.csv) | **Ministral 3 3B** | Continuous Batch (`0s` cooldown) | 5 | 4.42 | 1.42 | 793 s | 0.97 W | 5.60 W | 7.27 W | **4366.20 J** | 1.2128 Wh | 26.3 → 38.9 (**38.9°C**) |
| **`squad_6`** | [`screenlog.squad_6`](./raw/screenlog.squad_6) | [`energy_log_1795683984.csv`](./raw/energy_log_1795683984.csv) | **Ministral 3 3B** | Single-Fire (`run_squad_single.py`) | 1 | 4.10 | 0.30 | 3121 s | 0.68 W | 5.06 W | 7.17 W | **4028.39 J** | 1.1190 Wh | 25.1 → 23.7 (**27.2°C**) |
| **`squad_7`** | [`screenlog.squad_7`](./raw/screenlog.squad_7) | [`energy_log_1795724010.csv`](./raw/energy_log_1795724010.csv) | **Qwen 2.5 3B** | Single-Fire (`run_squad_single.py`) | 1 | 5.00 | 2.30 | 82 s | 0.88 W | 4.48 W | 6.06 W | **183.74 J** | 0.0510 Wh | 22.7 → 23.4 (**23.4°C**) |
| **`squad_8`** | [`screenlog.squad_8`](./raw/screenlog.squad_8) | [`energy_log_1795724095.csv`](./raw/energy_log_1795724095.csv) | **Qwen 2.5 3B** | Continuous Batch (`0s` cooldown) | 5 | 5.04 | 2.40 | 229 s | 0.90 W | 4.99 W | 6.60 W | **942.15 J** | 0.2617 Wh | 28.7 → 31.9 (**31.9°C**) |
| **`squad_9`** | [`screenlog.squad_9`](./raw/screenlog.squad_9) | [`energy_log_1795724140.csv`](./raw/energy_log_1795724140.csv) | **Qwen 2.5 3B** | Staggered Batch (`60s` cooldown) | 5 | 5.06 | 2.40 | 464 s | 0.83 W | 4.94 W | 6.11 W | **898.17 J** | 0.2495 Wh | 27.2 → 29.6 (**29.6°C**) |
