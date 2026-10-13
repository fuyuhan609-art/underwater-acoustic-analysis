import csv
import numpy as np

from signal_processing import (
    generate_signal,
    calculate_snr,
    bandpass_filter
)

sampling_rate = 44100
duration = 2
target_frequency = 1000

noise_levels = [0.1, 0.3, 0.5, 0.8, 1.0]

print("Noise-Level Experiment")
print("=" * 55)
print(
    f"{'Noise':>8} "
    f"{'Before SNR':>15} "
    f"{'After SNR':>15} "
    f"{'Improvement':>15}"
)
results = []

for noise_amplitude in noise_levels:
    _, clean_signal, noisy_signal, noise = generate_signal(
        sampling_rate,
        duration,
        target_frequency,
        noise_amplitude
    )

    snr_before = calculate_snr(
        clean_signal,
        noise
    )

    filtered_signal = bandpass_filter(
        noisy_signal,
        sampling_rate,
        800,
        1200
    )

    filtered_noise = filtered_signal - clean_signal

    snr_after = calculate_snr(
        clean_signal,
        filtered_noise
    )

    improvement = snr_after - snr_before
    results.append({
        "noise_amplitude": noise_amplitude,
        "snr_before_db": snr_before,
        "snr_after_db": snr_after,
        "snr_improvement_db": improvement
    })

    print(
        f"{noise_amplitude:>8.1f} "
        f"{snr_before:>12.2f} dB "
        f"{snr_after:>12.2f} dB "
        f"{improvement:>12.2f} dB"
    )
with open(
    "data/noise_experiment.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "noise_amplitude",
            "snr_before_db",
            "snr_after_db",
            "snr_improvement_db"
        ]
    )

    writer.writeheader()
    writer.writerows(results)

print("\nResults saved to data/noise_experiment.csv")