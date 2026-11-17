# The Upcycled Cloud: Reproducibility Data & Code Repository

Accompanying dataset, telemetry logs, benchmark execution scripts, and model manifest for the research paper:

> **The Upcycled Cloud: Evaluating Legacy and Budget ARM Devices for Energy-Constrained Edge LLM Inference**  
> Aryan Chandna (Evergreen Valley High School)

---

## 1. Data and Code Availability Statement

This repository contains the benchmark execution scripts, 1 Hz hardware battery and USB power telemetry (`.xlsx` / `.csv`), evaluation prompt datasets, raw `llama.cpp` terminal inference transcripts (`screenlog.0`, `screenlog.1`, `output`, `command`), and post-processing analysis scripts used in the study.

In accordance with upstream model licensing restrictions and repository storage constraints, multi-gigabyte `.gguf` model weights are not redistributed directly in this repository. Instead, **Section 2** and **Section 3** below provide the complete model manifest—including exact `.gguf` filenames as logged by `llama-cli`, upstream base model identifiers, Hugging Face GGUF repositories, direct download URLs, quantization specifications, file sizes, and Git LFS `SHA-256` checksums—required to reproduce every experiment 1:1.

---

## 2. Master GGUF Model Manifest

All 10 model directories in [`Research Data/`](./Research%20Data) map to **18 distinct `.gguf` model files** across four quantization schemes (`Q4_0`, `Q4_K_M`, `Q3_K_M`, and `Q2_K`).

| Folder in `Research Data/` | Quant | Exact `.gguf` Filename | Logged String in `screenlog` / `command` | Hugging Face GGUF Repository (`<owner>/<repo>`) | Direct Download URL | Size | Git LFS `SHA-256` Checksum |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`Gemma 3 1B`** | `Q4_0` | `gemma-3-1b-it.Q4_0.gguf` | `gemma-3-1b-it.Q4_0.gguf` | [`brittlewis12/gemma-3-1b-it-GGUF`](https://huggingface.co/brittlewis12/gemma-3-1b-it-GGUF) | [Resolve URL](https://huggingface.co/brittlewis12/gemma-3-1b-it-GGUF/resolve/main/gemma-3-1b-it.Q4_0.gguf) | ~0.72 GB | `2fcb374ac4adbec25f522df27877b81667e1c69e6767d5b9f37a2b24f2976cbc` |
| **`TinyLLama 1.1B`** | `Q4_0` | `tinyllama-1.1b-chat-v1.0.Q4_0.gguf` | `tinyllama-1.1b-chat-v1.0.Q4_0.gguf`<br>`tinyllama-1.1b-chat-v1.0.Q4_0.gguf?download=true` | [`TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF`](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF) | [Resolve URL](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_0.gguf) | ~637 MB | `da3087fb14aede55fde6eb81a0e55e886810e43509ec82ecdc7aa5d62a03b556` |
| **`TinyLLama 1.1B`** | `Q4_K_M` | `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` | `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf?download=true` | [`TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF`](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF) | [Resolve URL](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf) | ~668 MB | `9fecc3b3cd76bba89d504f29b616eedf7da85b96540e490ca5824d3f7d2776a0` |
| **`Llama 3.2 1B`** | `Q4_0` | `Llama-3.2-1B-Instruct-Q4_0.gguf` | `Llama-3.2-1B-Instruct-Q4_0.gguf?download=true`<br>`Llama-3.2-1B-Instruct-Q4_0.gguf?download=true.1` | [`unsloth/Llama-3.2-1B-Instruct-GGUF`](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-GGUF) | [Resolve URL](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q4_0.gguf) | ~773 MB | `4b882e62a2fa5121f8c7e7caa912eead5c1f90be728e5d0e4ce9e1884a2ba6a6` |
| **`Llama 3.2 1B`** | `Q4_K_M` | `Llama-3.2-1B-Instruct-Q4_K_M.gguf` | `Llama-3.2-1B-Instruct-Q4_K_M.gguf?download=true` | [`unsloth/Llama-3.2-1B-Instruct-GGUF`](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-GGUF) | [Resolve URL](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q4_K_M.gguf) | ~808 MB | `3f5a22426976ab26cfe84dba63c1d08391717abb1af893e10f1b2968d862dcc1` |
| **`Qwen 2.5 1.5B`** | `Q4_0` | `Qwen2.5-1.5B-Instruct.Q4_0.gguf` | `./Qwen2.5-1.5B-Instruct.Q4_0.gguf\?download\=true` | [`QuantFactory/Qwen2.5-1.5B-Instruct-GGUF`](https://huggingface.co/QuantFactory/Qwen2.5-1.5B-Instruct-GGUF) | [Resolve URL](https://huggingface.co/QuantFactory/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/Qwen2.5-1.5B-Instruct.Q4_0.gguf) | ~0.94 GB | `dcd819ff094852c38faba6873d8ff0c9d51eadb2844539e52042ae5d647bbfdb` |
| **`Phi-2 2.7B`** | `Q4_0` | `phi-2-instruct.Q4_0.gguf` | `phi-2-instruct.Q4_0.gguf`<br>`phi-2-instruct.Q4_0.gguf?download=true` | [`RichardErkhov/ashmitkx_-_phi-2-instruct-gguf`](https://huggingface.co/RichardErkhov/ashmitkx_-_phi-2-instruct-gguf) | [Resolve URL](https://huggingface.co/RichardErkhov/ashmitkx_-_phi-2-instruct-gguf/resolve/main/phi-2-instruct.Q4_0.gguf) | ~1.60 GB | *(Verify via `hf download` LFS pointer)* |
| **`Phi-2 2.7B`** | `Q4_K_M` | `phi-2-instruct.Q4_K_M.gguf` | `phi-2-instruct.Q4_K_M.gguf?download=true` | [`RichardErkhov/ashmitkx_-_phi-2-instruct-gguf`](https://huggingface.co/RichardErkhov/ashmitkx_-_phi-2-instruct-gguf) | [Resolve URL](https://huggingface.co/RichardErkhov/ashmitkx_-_phi-2-instruct-gguf/resolve/main/phi-2-instruct.Q4_K_M.gguf) | ~1.73 GB | *(Verify via `hf download` LFS pointer)* |
| **`Llama 3.2 3B`** | `Q4_0` | `Llama-3.2-3B-Instruct-Q4_0.gguf` | `Llama-3.2-3B-Instruct-Q4_0.gguf`<br>`Llama-3.2-3B-Instruct-Q4_0.gguf?download=true` | [`bartowski/Llama-3.2-3B-Instruct-GGUF`](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF) | [Resolve URL](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_0.gguf) | ~1.92 GB | `4d491003bf6b470e4d04233824c5c939b76d6c81974ba17a3ff207343e1d8e85` |
| **`Llama 3.2 3B`** | `Q4_K_M` | `Llama-3.2-3B-Instruct-Q4_K_M.gguf` | `Llama-3.2-3B-Instruct-Q4_K_M.gguf` | [`bartowski/Llama-3.2-3B-Instruct-GGUF`](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF) | [Resolve URL](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf) | ~2.02 GB | `6c1a2b41161032677be168d354123594c0e6e67d2b9227c84f296ad037c728ff` |
| **`Ministral 3 3B`** | `Q4_0` | `Ministral-3-3B-Instruct-2512-Q4_0.gguf` | `Ministral-3-3B-Instruct-2512-Q4_0.gguf` | [`unsloth/Ministral-3-3B-Instruct-2512-GGUF`](https://huggingface.co/unsloth/Ministral-3-3B-Instruct-2512-GGUF) | [Resolve URL](https://huggingface.co/unsloth/Ministral-3-3B-Instruct-2512-GGUF/resolve/main/Ministral-3-3B-Instruct-2512-Q4_0.gguf) | ~2.00 GB | *(Verify via `hf download` LFS pointer)* |
| **`Ministral 3 3B`** | `Q4_K_M` | `Ministral-3-3B-Instruct-2512-Q4_K_M.gguf` | `Ministral-3-3B-Instruct-2512-Q4_K_M.gguf?download=true` | [`unsloth/Ministral-3-3B-Instruct-2512-GGUF`](https://huggingface.co/unsloth/Ministral-3-3B-Instruct-2512-GGUF) | [Resolve URL](https://huggingface.co/unsloth/Ministral-3-3B-Instruct-2512-GGUF/resolve/main/Ministral-3-3B-Instruct-2512-Q4_K_M.gguf) | ~2.15 GB | `fd46fc371ff0509bfa8657ac956b7de8534d7d9baaa4947975c0648c3aa397f4` |
| **`Qwen 2.5 3B`** | `Q4_0` | `qwen2.5-3b-instruct-q4_0.gguf` | `qwen2.5-3b-instruct-q4_0.gguf?download=true` | [`Qwen/Qwen2.5-3B-Instruct-GGUF`](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF) | [Resolve URL](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q4_0.gguf) | ~1.82 GB | `670d82d0fbee6289b661eb323612c65bd2e97ec8c65cdbd9131aa44d30e9816a` |
| **`Qwen 2.5 3B`** | `Q4_K_M` | `qwen2.5-3b-instruct-q4_k_m.gguf` | `qwen2.5-3b-instruct-q4_k_m.gguf?download=true` | [`Qwen/Qwen2.5-3B-Instruct-GGUF`](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF) | [Resolve URL](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q4_k_m.gguf) | ~2.10 GB | `626b4a6678b86442240e33df819e00132d3ba7dddfe1cdc4fbb18e0a9615c62d` |
| **`Phi-4 Mini 3.8B`** | `Q2_K` | `Phi-4-mini-instruct-Q2_K.gguf` | `~/Phi-4-mini-instruct-Q2_K.gguf` | [`unsloth/Phi-4-mini-instruct-GGUF`](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF) | [Resolve URL](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF/resolve/main/Phi-4-mini-instruct-Q2_K.gguf) | ~1.63 GB | `70763e15ae749fdd746a3f7b74a9701d0c556b687f026bacaa028bebfcbfdc11` |
| **`Phi-4 Mini 3.8B`** | `Q4_K_M` | `Phi-4-mini-instruct-Q4_K_M.gguf` | `Phi-4-mini-instruct-Q4_K_M.gguf` | [`unsloth/Phi-4-mini-instruct-GGUF`](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF) | [Resolve URL](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF/resolve/main/Phi-4-mini-instruct-Q4_K_M.gguf) | ~2.49 GB | `88c00229914083cd112853aab84ed51b87bdf6b9ce42f532d8c85c7c63b1730a` |
| **`Llama 3.1 8B`** | `Q3_K_M` | `Meta-Llama-3.1-8B.Q3_K_M.gguf` | `../../Meta-Llama-3.1-8B.Q3_K_M.gguf` | [`mradermacher/Meta-Llama-3.1-8B-GGUF`](https://huggingface.co/mradermacher/Meta-Llama-3.1-8B-GGUF) | [Resolve URL](https://huggingface.co/mradermacher/Meta-Llama-3.1-8B-GGUF/resolve/main/Meta-Llama-3.1-8B.Q3_K_M.gguf) | ~4.02 GB | `6464a71b2157425a39e219233b267c03870a4a6e02a759d6854f5db1031aaa16` |
| **`Llama 3.1 8B`** | `Q4_K_M` | `Meta-Llama-3.1-8B.Q4_K_M.gguf` | `../../Meta-Llama-3.1-8B.Q4_K_M.gguf` | [`mradermacher/Meta-Llama-3.1-8B-GGUF`](https://huggingface.co/mradermacher/Meta-Llama-3.1-8B-GGUF) | [Resolve URL](https://huggingface.co/mradermacher/Meta-Llama-3.1-8B-GGUF/resolve/main/Meta-Llama-3.1-8B.Q4_K_M.gguf) | ~4.92 GB | *(Verify via `hf download` LFS pointer)* |
| **`Llama 3.1 8B`** | `Q4_K_M` | `Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf` | `Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf?download=true` | [`bartowski/Meta-Llama-3.1-8B-Instruct-GGUF`](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF) | [Resolve URL](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf) | ~4.92 GB | `7b064f5842bf9532c91456deda288a1b672397a54fa729aa665952863033557c` |

> **Note on `?download=true` Suffixes in Logs:** When model files were fetched directly onto the Android/Termux testbed via `wget https://huggingface.co/<owner>/<repo>/resolve/main/<filename>.gguf?download=true` without `-O`, `wget` preserved the `?download=true` query string in the local filename (and `.1` when re-downloaded on the Galaxy S8). The underlying binary files are identical to the clean `.gguf` filenames listed above.

---

## 3. Detailed Model Metadata & Provenance

### 3.1 `Gemma 3 1B` (1.0B Parameters)
* **Upstream Base Model:** [`google/gemma-3-1b-it`](https://huggingface.co/google/gemma-3-1b-it) (Google DeepMind)
* **GGUF Repository:** [`brittlewis12/gemma-3-1b-it-GGUF`](https://huggingface.co/brittlewis12/gemma-3-1b-it-GGUF)
* **Quantization Evaluated:** `Q4_0` (`gemma-3-1b-it.Q4_0.gguf`, ~0.72 GB / 755,770,368 bytes, SHA-256: `2fcb374ac4adbec25f522df27877b81667e1c69e6767d5b9f37a2b24f2976cbc`)
* **Role in Study & Workloads:** Evaluated on the **ONN 4K TV Box Plus (Amlogic S905X5M)** CPU under the 500-word Roman Empire long-form generation prompt (`Research Data/Gemma 3 1B/Q4_0/.../onn-gemma-3.xlsx`), with external 1 Hz USB inline power telemetry.

### 3.2 `TinyLLama 1.1B` (1.1B Parameters)
* **Upstream Base Model:** [`TinyLlama/TinyLlama-1.1B-Chat-v1.0`](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
* **GGUF Repository:** [`TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF`](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
* **Quantizations Evaluated:**
  * `Q4_0`: `tinyllama-1.1b-chat-v1.0.Q4_0.gguf` (637 MB, SHA-256: `da3087fb14aede55fde6eb81a0e55e886810e43509ec82ecdc7aa5d62a03b556`)
  * `Q4_K_M`: `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` (668 MB, SHA-256: `9fecc3b3cd76bba89d504f29b616eedf7da85b96540e490ca5824d3f7d2776a0`)
* **`llama.cpp` Builds Recorded:** `b7902-3bc8d2cf2`, `b7968-9a5f57795`, `b7981-98e57ca42`, `b8099-3bb2fcc85` (`Q4_0`); `b8265-c96f608d9` (`Q4_K_M`)
* **Role in Study & Workloads:** Sub-scale 1.1B baseline without knowledge distillation. Evaluated across `SQuAD 2.0`, `AlpacaEval`, `SAMSum` (Single-Fire, Staggered Batch, and Continuous Batch), and the Roman Empire prompt (including Adreno 630 OpenCL testing on the LG G7 ThinQ).

### 3.3 `Llama 3.2 1B` (1.23B Parameters)
* **Upstream Base Model:** [`meta-llama/Llama-3.2-1B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) (Meta AI)
* **GGUF Repository:** [`unsloth/Llama-3.2-1B-Instruct-GGUF`](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-GGUF) (compatible with [`bartowski/Llama-3.2-1B-Instruct-GGUF`](https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF))
* **Quantizations Evaluated:**
  * `Q4_0`: `Llama-3.2-1B-Instruct-Q4_0.gguf` (773 MB, SHA-256: `4b882e62a2fa5121f8c7e7caa912eead5c1f90be728e5d0e4ce9e1884a2ba6a6`)
  * `Q4_K_M`: `Llama-3.2-1B-Instruct-Q4_K_M.gguf` (808 MB, SHA-256: `3f5a22426976ab26cfe84dba63c1d08391717abb1af893e10f1b2968d862dcc1`)
* **`llama.cpp` Builds Recorded:** `b7902-3bc8d2cf2`, `b7968-9a5f57795`, `b7981-98e57ca42`, `b8099-3bb2fcc85` (`Q4_0`); `b8265-c96f608d9` (`Q4_K_M`)
* **Role in Study & Workloads:** Knowledge-distilled sub-scale 1B model contrasted directly against `TinyLLama 1.1B` across `SQuAD 2.0`, `AlpacaEval`, and `SAMSum` across all six devices.

### 3.4 `Qwen 2.5 1.5B` (1.54B Parameters)
* **Upstream Base Model:** [`Qwen/Qwen2.5-1.5B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) (Alibaba Cloud Qwen)
* **GGUF Repository:** [`QuantFactory/Qwen2.5-1.5B-Instruct-GGUF`](https://huggingface.co/QuantFactory/Qwen2.5-1.5B-Instruct-GGUF)
* **Quantization Evaluated:** `Q4_0` (`Qwen2.5-1.5B-Instruct.Q4_0.gguf`, ~0.94 GB, SHA-256: `dcd819ff094852c38faba6873d8ff0c9d51eadb2844539e52042ae5d647bbfdb`)
* **Role in Study & Workloads:** Evaluated on the **ONN 4K TV Box Plus (Amlogic S905X5M)** CPU under the 500-word Roman Empire prompt (`Research Data/Qwen 2.5 1.5B/Q4_0/...`), capturing inline USB power telemetry (`onn-qwen.xlsx`) and verbose inference logs (`output`, `command`).

### 3.5 `Phi-2 2.7B` (2.7B Parameters)
* **Upstream Base Model:** [`microsoft/phi-2`](https://huggingface.co/microsoft/phi-2) / instruction-tuned variant [`venkycs/phi-2-instruct`](https://huggingface.co/venkycs/phi-2-instruct) (`ashmitkx/phi-2-instruct`)
* **GGUF Repository:** [`RichardErkhov/ashmitkx_-_phi-2-instruct-gguf`](https://huggingface.co/RichardErkhov/ashmitkx_-_phi-2-instruct-gguf)
* **Quantizations Evaluated:**
  * `Q4_0`: `phi-2-instruct.Q4_0.gguf` (~1.60 GB)
  * `Q4_K_M`: `phi-2-instruct.Q4_K_M.gguf` (~1.73 GB)
* **`llama.cpp` Builds Recorded:** `b7902-3bc8d2cf2`, `b7968-9a5f57795`, `b8099-3bb2fcc85` (`Q4_0`); `b8265-c96f608d9` (`Q4_K_M`)
* **Role in Study & Workloads:** Intermediate 2.7B parameter bridge between 1B sub-scale models and 3B architectures; evaluated on `SQuAD 2.0`, `AlpacaEval`, `SAMSum`, and the single-prompt Rotational Inertia Physics test.

### 3.6 `Llama 3.2 3B` (3.21B Parameters)
* **Upstream Base Model:** [`meta-llama/Llama-3.2-3B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) (Meta AI)
* **GGUF Repository:** [`bartowski/Llama-3.2-3B-Instruct-GGUF`](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF)
* **Quantizations Evaluated:**
  * `Q4_0`: `Llama-3.2-3B-Instruct-Q4_0.gguf` (~1.92 GB, SHA-256: `4d491003bf6b470e4d04233824c5c939b76d6c81974ba17a3ff207343e1d8e85`)
  * `Q4_K_M`: `Llama-3.2-3B-Instruct-Q4_K_M.gguf` (~2.02 GB, SHA-256: `6c1a2b41161032677be168d354123594c0e6e67d2b9227c84f296ad037c728ff`)
* **`llama.cpp` Builds Recorded:** `b7902-3bc8d2cf2`, `b7968-9a5f57795`, `b8099-3bb2fcc85`, `b8265-c96f608d9`
* **Role in Study & Workloads:** Primary 3B reference architecture evaluated across all benchmarks (`SQuAD 2.0`, `AlpacaEval`, `SAMSum`, `MMLU-Pro`, Roman Empire, Social Cue interpretation, and the 50-prompt thermally gated **Mega Benchmark** under `Research Data/Llama 3.2 3B/Q4_0/Mega/`).
* **Log Note:** In `Research Data/Llama 3.2 3B/Q4_K_M/Write a detailed history.../OnePlus 7T/CPU/commandllama`, the CLI flag points to `~/Llama-3.2-3B-Instruct-Q4_0.gguf`.

### 3.7 `Ministral 3 3B` (3.4B Language Parameters)
* **Upstream Base Model:** [`mistralai/Ministral-3-3B-Instruct-2512`](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512) (Mistral AI)
* **GGUF Repository:** [`unsloth/Ministral-3-3B-Instruct-2512-GGUF`](https://huggingface.co/unsloth/Ministral-3-3B-Instruct-2512-GGUF)
* **Quantizations Evaluated:**
  * `Q4_0`: `Ministral-3-3B-Instruct-2512-Q4_0.gguf` (~2.00 GB)
  * `Q4_K_M`: `Ministral-3-3B-Instruct-2512-Q4_K_M.gguf` (~2.15 GB, SHA-256: `fd46fc371ff0509bfa8657ac956b7de8534d7d9baaa4947975c0648c3aa397f4`)
* **`llama.cpp` Builds Recorded:** `b7902-3bc8d2cf2`, `b7968-9a5f57795`, `b8099-3bb2fcc85` (`Q4_0`); `b8265-c96f608d9` (`Q4_K_M`)
* **Role in Study & Workloads:** Evaluated across `SQuAD 2.0`, `AlpacaEval`, `SAMSum`, `MMLU-Pro`, and the Rotational Inertia Physics prompt across Tier 1, Tier 2, and Tier 3 smartphones.

### 3.8 `Qwen 2.5 3B` (3.09B Parameters)
* **Upstream Base Model:** [`Qwen/Qwen2.5-3B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) (Alibaba Cloud Qwen)
* **GGUF Repository:** [`Qwen/Qwen2.5-3B-Instruct-GGUF`](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF) (Official Qwen GGUF release)
* **Quantizations Evaluated:**
  * `Q4_0`: `qwen2.5-3b-instruct-q4_0.gguf` (~1.82 GB, SHA-256: `670d82d0fbee6289b661eb323612c65bd2e97ec8c65cdbd9131aa44d30e9816a`)
  * `Q4_K_M`: `qwen2.5-3b-instruct-q4_k_m.gguf` (~2.10 GB, SHA-256: `626b4a6678b86442240e33df819e00132d3ba7dddfe1cdc4fbb18e0a9615c62d`)
* **`llama.cpp` Builds Recorded:** `b7902-3bc8d2cf2`, `b7968-9a5f57795`, `b8099-3bb2fcc85` (`Q4_0`); `b8265-c96f608d9` (`Q4_K_M`)
* **Role in Study & Workloads:** Evaluated across `SQuAD 2.0`, `AlpacaEval`, and `SAMSum` (Single-Fire, Staggered Batch, and Continuous Batch) across Tier 1, Tier 2, and Tier 3 smartphones.

### 3.9 `Phi-4 Mini 3.8B` (3.8B Parameters)
* **Upstream Base Model:** [`microsoft/Phi-4-mini-instruct`](https://huggingface.co/microsoft/Phi-4-mini-instruct) (Microsoft)
* **GGUF Repository:** [`unsloth/Phi-4-mini-instruct-GGUF`](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF)
* **Quantizations Evaluated:**
  * `Q2_K`: `Phi-4-mini-instruct-Q2_K.gguf` (~1.63 GB, SHA-256: `70763e15ae749fdd746a3f7b74a9701d0c556b687f026bacaa028bebfcbfdc11`)
  * `Q4_K_M`: `Phi-4-mini-instruct-Q4_K_M.gguf` (~2.49 GB, SHA-256: `88c00229914083cd112853aab84ed51b87bdf6b9ce42f532d8c85c7c63b1730a`)
* **`llama.cpp` Builds Recorded:** `b8265-c96f608d9` (`Q4_K_M`)
* **Role in Study & Workloads:** Upper-bound "Goldilocks" (3.8B) dense reasoning model. `Q4_K_M` was evaluated on Tier 1 (`OnePlus 7T`) and Tier 2 (`Pixel 4a`) across `SQuAD 2.0`, `AlpacaEval`, `SAMSum`, `MMLU-Pro`, Rotational Inertia Physics, and Social Cue tasks. `Q2_K` was used on the RAM-constrained 4 GB `LG G7 ThinQ` (`Research Data/Phi-4 Mini 3.8B/Q2_K/...`) to test extreme 2-bit quantization degradation.

### 3.10 `Llama 3.1 8B` (8.03B Parameters)
* **Upstream Base Models:**
  * Base Pretrained: [`meta-llama/Meta-Llama-3.1-8B`](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B)
  * Instruction-Tuned: [`meta-llama/Meta-Llama-3.1-8B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)
* **GGUF Repositories & Quantizations Evaluated:**
  1. **Base `Q3_K_M` (`Meta-Llama-3.1-8B.Q3_K_M.gguf`):** Hosted at [`mradermacher/Meta-Llama-3.1-8B-GGUF`](https://huggingface.co/mradermacher/Meta-Llama-3.1-8B-GGUF) (~4.02 GB, SHA-256: `6464a71b2157425a39e219233b267c03870a4a6e02a759d6854f5db1031aaa16`). Used on the 6 GB **Pixel 4a** for the Roman Empire long-form prompt to avoid Android `lmkd` Out-Of-Memory termination.
  2. **Base `Q4_K_M` (`Meta-Llama-3.1-8B.Q4_K_M.gguf`):** Hosted at [`mradermacher/Meta-Llama-3.1-8B-GGUF`](https://huggingface.co/mradermacher/Meta-Llama-3.1-8B-GGUF) (~4.92 GB). Used on the 8 GB **OnePlus 7T** for the Roman Empire long-form prompt.
  3. **Instruct `Q4_K_M` (`Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf`):** Hosted at [`bartowski/Meta-Llama-3.1-8B-Instruct-GGUF`](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF) (~4.92 GB, SHA-256: `7b064f5842bf9532c91456deda288a1b672397a54fa729aa665952863033557c`). Used on the 8 GB **OnePlus 7T** across all structured benchmarks (`SQuAD 2.0`, `AlpacaEval`, `SAMSum`, and `MMLU-Pro`).
* **`llama.cpp` Builds Recorded:** `b8265-c96f608d9`

---

## 4. Hardware Testbed & `llama.cpp` Runtime Environment

### 4.1 Evaluated Consumer ARM Devices

| Device | Release Year | Hardware Tier | SoC & Process Node | CPU Core Topology | ARM ISA & SIMD Features | RAM | Tested Backend(s) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OnePlus 7T** | 2019 | Tier 1 | Snapdragon 855+ (7nm) | 1×2.96 GHz + 3×2.42 GHz Kryo 485 (Cortex-A76) + 4×1.80 GHz (A55) | ARMv8.2-A (`FEAT_DotProd` / `asimddp`, `FEAT_FP16`) | 8 GB LPDDR4X | CPU (`sdot` + `CPU_REPACK`) |
| **Google Pixel 4a** | 2020 | Tier 2 | Snapdragon 730G (8nm) | 2×2.20 GHz Kryo 470 (Cortex-A76) + 6×1.80 GHz (A55) | ARMv8.2-A (`FEAT_DotProd` / `asimddp`, `FEAT_FP16`) | 6 GB LPDDR4X | CPU (`sdot` + `CPU_REPACK`) |
| **LG G7 ThinQ** | 2018 | Tier 3 | Snapdragon 845 (10nm) | 4×2.80 GHz Kryo 385 (Cortex-A75) + 4×1.70 GHz (A55) | Early ARMv8.2-A (`FEAT_FP16` only; **no** `FEAT_DotProd`) | 4 GB LPDDR4X | CPU (NEON fallback), OpenCL |
| **Samsung Galaxy S8** | 2017 | Tier 3 | Exynos 8895 (10nm) | 4×2.30 GHz Exynos M2 + 4×1.70 GHz Cortex-A53 | ARMv8.0-A (Baseline NEON; **no** `FEAT_DotProd`) | 4 GB LPDDR4X | CPU (NEON fallback) |
| **Moto G Play (2024)** | 2024 | Tier 3 | Snapdragon 680 (6nm) | 4×2.40 GHz Kryo 265 (Cortex-A73) + 4×1.90 GHz (A53) | ARMv8.0-A (Baseline NEON; **no** `FEAT_DotProd`) | 4 GB LPDDR4X | CPU (NEON fallback) |
| **onn. 4K Streaming Box Plus** | 2025 | Tier 1 (Mains) | Amlogic S905X5M (6nm) | 4×2.50 GHz Cortex-A55 (in-order) | ARMv8.2-A (`FEAT_DotProd` / `asimddp`) | 2 GB DDR4 | CPU (`sdot`) |

### 4.2 `llama.cpp` Build Versions Recorded in Telemetry Logs
All benchmarks were executed inside Termux (`aarch64-linux-android`) using `llama-cli` compiled from [`ggml-org/llama.cpp`](https://github.com/ggml-org/llama.cpp):
* **`b8265-c96f608d9`** — Used for `Q4_K_M` benchmarks on Tier 1 (`OnePlus 7T`) and Tier 2 (`Pixel 4a`), and Mega Benchmark runs on `OnePlus 7T` and `Pixel 4a`.
* **`b8099-3bb2fcc85`** — Used for `Q4_0` benchmarks (including Mega Benchmark) on `LG G7 ThinQ`.
* **`b7981-98e57ca42`** — Used for `Q4_0` benchmarks on `onn. 4K Streaming Box Plus (Amlogic S905X5M)`.
* **`b7968-9a5f57795`** — Used for `Q4_0` benchmarks (including Mega Benchmark) on `Moto G Play (2024)`.
* **`b7902-3bc8d2cf2`** — Used for `Q4_0` benchmarks (including Mega Benchmark) on `Samsung Galaxy S8`.

---

## 5. Benchmark Datasets & Execution Scripts ([`Scripts/`](./Scripts))

### 5.1 Upstream Evaluation Datasets
| Local File in `Scripts/` | Benchmark Suite | Upstream Hugging Face Dataset Source | Usage in Study |
| :--- | :--- | :--- | :--- |
| [`test-00000-of-00001.parquet`](./Scripts/test-00000-of-00001.parquet) | **MMLU-Pro** | [`datasets/TIGER-Lab/MMLU-Pro`](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/blob/main/data/test-00000-of-00001.parquet) | 20-question offline multi-choice reasoning & Physics subset |
| [`train.csv`](./Scripts/train.csv) | **SAMSum (Batch)** | [`datasets/knkarthick/samsum`](https://huggingface.co/datasets/knkarthick/samsum/blob/main/train.csv) | 7-prompt dialogue summarization suite (Staggered & Continuous Batch) |
| [`train_single.csv`](./Scripts/train_single.csv) | **SAMSum (Single)** | [`datasets/knkarthick/samsum`](https://huggingface.co/datasets/knkarthick/samsum/blob/main/train.csv) | Isolated single-fire dialogue summarization prompt |
| [`mega.csv`](./Scripts/mega.csv) | **Mega Benchmark** | Composite (`SAMSum` + `AlpacaEval` + `SQuAD 2.0`) | 50 randomized prompts (20 SAMSum, 15 AlpacaEval, 15 SQuAD 2.0) with `IDLE_TEMP <= 31.0°C` gating |
| *(Embedded in `run_alpaca*.py`)* | **AlpacaEval** | [`datasets/tatsu-lab/alpaca_eval`](https://huggingface.co/datasets/tatsu-lab/alpaca_eval/blob/main/alpaca_eval.json) | 5-prompt open-ended instruction following suite |
| *(Embedded in `run_squad*.py`)* | **SQuAD 2.0** | [`datasets/rajpurkar/squad_v2`](https://huggingface.co/datasets/rajpurkar/squad_v2) | 5-prompt extractive reading comprehension & unanswerable abstention suite |

### 5.2 Benchmark & Telemetry Scripts
* **[`eco-logger.sh`](./Scripts/eco-logger.sh):** 1 Hz background hardware battery telemetry daemon polling `/sys/class/power_supply/battery/{voltage_now,current_now,temp,capacity}` on Android devices.
* **[`run_mega.py`](./Scripts/run_mega.py):** Executes the 50-prompt randomized **Cross-Domain Thermally Gated Protocol (Mega Benchmark)** using `Llama-3.2-3B-Instruct-Q4_0.gguf`, enforcing an active thermal cooldown gate (`<= 31.0°C`) between prompts.
* **[`run_squad.py`](./Scripts/run_squad.py) & [`run_squad_single.py`](./Scripts/run_squad_single.py):** Staggered/Continuous batch (5 prompts) and Single-Fire (1 prompt) SQuAD 2.0 runners.
* **[`run_alpaca.py`](./Scripts/run_alpaca.py) & [`run_alpaca_single.py`](./Scripts/run_alpaca_single.py):** Staggered/Continuous batch (5 prompts) and Single-Fire (1 prompt) AlpacaEval runners.
* **[`run_samsum.py`](./Scripts/run_samsum.py) & [`run_samsum_onn.py`](./Scripts/run_samsum_onn.py):** SAMSum dialogue summarization runners for smartphones and the ONN 4K TV Box Plus.
* **[`run_benchmark.py`](./Scripts/run_benchmark.py):** MMLU-Pro offline evaluation runner reading `test-00000-of-00001.parquet`.
* **[`energy_analysis_universal.py`](./Scripts/energy_analysis_universal.py), [`energy_analysis_onn.py`](./Scripts/energy_analysis_onn.py), [`galaxy_s8.py`](./Scripts/galaxy_s8.py), [`lg_g7.py`](./Scripts/lg_g7.py), [`moto_g_play.py`](./Scripts/moto_g_play.py):** Post-processing and plotting scripts that integrate 1 Hz voltage/current telemetry (`Power_W = Voltage_V * Current_A`) into total electrical energy (`Wh`) and thermal curves (`Temp_C`).

---

## 6. Repository Directory Structure

```text
Repository/
├── README.md                          # Master model manifest, SHA-256 hashes, and reproducibility guide
├── Scripts/                           # Benchmark runners, telemetry logger, datasets, and analysis scripts
│   ├── eco-logger.sh
│   ├── mega.csv
│   ├── train.csv
│   ├── train_single.csv
│   ├── test-00000-of-00001.parquet
│   ├── run_mega.py
│   ├── run_squad.py / run_squad_single.py
│   ├── run_alpaca.py / run_alpaca_single.py
│   ├── run_samsum.py / run_samsum_onn.py
│   ├── run_benchmark.py
│   └── energy_analysis_*.py
└── Research Data/                     # Raw inference logs (screenlog.0) and 1 Hz power telemetry (.xlsx)
    ├── Gemma 3 1B/
    │   └── Q4_0/
    ├── TinyLLama 1.1B/
    │   ├── Q4_0/
    │   └── Q4_K_M/
    ├── Llama 3.2 1B/
    │   ├── Q4_0/
    │   └── Q4_K_M/
    ├── Qwen 2.5 1.5B/
    │   └── Q4_0/
    ├── Phi-2 2.7B/
    │   ├── Q4_0/
    │   └── Q4_K_M/
    ├── Llama 3.2 3B/
    │   ├── Q4_0/                      # Includes Mega/ 50-prompt thermally gated benchmark logs
    │   └── Q4_K_M/
    ├── Ministral 3 3B/
    │   ├── Q4_0/
    │   └── Q4_K_M/
    ├── Qwen 2.5 3B/
    │   ├── Q4_0/
    │   └── Q4_K_M/
    ├── Phi-4 Mini 3.8B/
    │   ├── Q2_K/
    │   └── Q4_K_M/
    └── Llama 3.1 8B/
        ├── Q3_K_M/
        └── Q4_K_M/
```
