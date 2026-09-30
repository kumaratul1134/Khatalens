# KhataLens
Offline, NPU-accelerated voice & invoice copilot for Indian MSME bookkeeping. Built for Snapdragon-powered HP PCs (Snapdragon® AI Lab Build & Present Challenge).

## Pipeline
Voice / invoice image -> Whisper + OCR + Llama 3.2 3B (Qualcomm AI Hub, Hexagon NPU) -> JSON -> `guardrails.py` (GSTIN checksum, GST rate, totals) -> SQLite ledger -> GSTR-1 CSV / Tally XML.

## Setup (Windows on Arm)
1. Install ARM64 Python 3.11+ and `pip install onnxruntime-qnn qai-hub-models`
2. Export/download models from Qualcomm AI Hub (Whisper, OCR, Llama 3.2 3B) into `models/`
3. Run the app; disable Wi-Fi to verify it works fully offline

## Tests
`pytest` runs the guardrail checks.

## Benchmarks (fill in from your device)
| Metric | CPU | NPU |
|---|---|---|
| Seconds per invoice | | |
| Field extraction accuracy | | |
| Energy per invoice | | |
