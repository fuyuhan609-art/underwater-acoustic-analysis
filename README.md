# Underwater Acoustic Signal Analysis

## Overview

This project explores underwater acoustic signal processing using Python. It implements a signal processing pipeline to generate noisy signals, analyze frequency components, apply band-pass filtering, and evaluate signal quality using the Signal-to-Noise Ratio (SNR).

The project also investigates how different noise levels affect filtering performance.

## Objectives

- Generate synthetic acoustic signals with configurable noise levels.
- Analyze frequency components using the Fast Fourier Transform (FFT).
- Apply band-pass filtering to isolate a target frequency.
- Evaluate signal quality before and after filtering using SNR.
- Visualize signals in the time and frequency domains.
- Compare filtering performance under different noise conditions.
- Validate core functions with automated tests.

## Technologies

- Python
- NumPy
- SciPy
- pandas
- Matplotlib
- pytest
- Git and GitHub

## Signal Processing Pipeline

1. Generate a 1,000 Hz sinusoidal signal with configurable noise.
2. Analyze the signal's frequency components.
3. Apply a band-pass filter with cutoff frequencies of 800 Hz and 1,200 Hz.
4. Calculate SNR before and after filtering.
5. Compare results across different noise amplitudes.
6. Visualize and save analysis results.

## Experimental Results

In one experiment with a noise amplitude of 0.8, the measured SNR increased from approximately -1.09 dB before filtering to 10.40 dB after filtering, an improvement of 11.49 dB.

Across five tested noise amplitudes (0.1, 0.3, 0.5, 0.8, and 1.0), the measured SNR improvement ranged from -5.36 dB to 12.78 dB.

At the lowest noise level, the measured SNR decreased after filtering. This highlights the importance of considering filter-induced signal distortion when evaluating performance.

These results are from a synthetic-signal experiment and should not be interpreted as validation on real underwater recordings.

## Project Structure

```text
underwater-acoustic-analysis/
├── data/
├── src/
│   ├── signal_generator.py
│   ├── fft_analysis.py
│   ├── filtering.py
│   ├── snr_analysis.py
│   ├── spectrogram.py
│   ├── signal_processing.py
│   ├── visualization.py
│   ├── noise_experiment.py
│   └── pipeline.py
├── tests/
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/fuyuhan609-art/underwater-acoustic-analysis.git
cd underwater-acoustic-analysis
```

Create and activate a virtual environment.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Project

Run the main processing pipeline:

```bash
python src/pipeline.py
```

Run the noise-level experiment:

```bash
python src/noise_experiment.py
```

## Run Tests

```bash
python -m pytest -v
```

The current test suite contains seven tests covering signal generation, SNR calculation, filtering, dominant-frequency detection, and invalid filter parameters.

## Limitations and Future Work

- Evaluate performance using real or representative underwater acoustic recordings.
- Improve SNR estimation to distinguish residual noise from filter-induced signal distortion.
- Compare different filter designs and parameters.
- Add automated plots and experiment summaries.
- Expand the test suite and continuous integration workflow.

## Author

Developed as a portfolio project combining Python programming, digital signal processing, and an academic background in underwater acoustics.
