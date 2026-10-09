import numpy as np

from visualization import (
    plot_time_domain,
    plot_frequency_domain
)

from signal_processing import (
    generate_signal,
    calculate_snr,
    bandpass_filter,
    detect_dominant_frequency
)


sampling_rate = 44100
duration = 2
frequency = 1000
noise_amplitude = 0.8

# Generate signal
t, clean_signal, noisy_signal, noise = generate_signal(
    sampling_rate,
    duration,
    frequency,
    noise_amplitude
)

# Calculate SNR before filtering
snr_before = calculate_snr(
    clean_signal,
    noise
)

# Apply band-pass filter
filtered_signal = bandpass_filter(
    noisy_signal,
    sampling_rate,
    800,
    1200
)

# Calculate residual noise
filtered_noise = filtered_signal - clean_signal

# Calculate SNR after filtering
snr_after = calculate_snr(
    clean_signal,
    filtered_noise
)

# Calculate improvement
snr_improvement = snr_after - snr_before

print(f"SNR before filtering: {snr_before:.2f} dB")
print(f"SNR after filtering: {snr_after:.2f} dB")
print(f"SNR improvement: {snr_improvement:.2f} dB")

dominant_frequency = detect_dominant_frequency(
    filtered_signal,
    sampling_rate
)

print(f"Dominant frequency: {dominant_frequency:.2f} Hz")

plot_time_domain(
    t,
    noisy_signal,
    filtered_signal,
    output_path="data/time_domain_comparison.png"
)

plot_frequency_domain(
    noisy_signal,
    filtered_signal,
    sampling_rate,
    output_path="data/frequency_comparison.png"
)

with open("data/results.txt", "w", encoding="utf-8") as f:
    f.write("Underwater Acoustic Signal Analysis\n")
    f.write("===================================\n")
    f.write(f"SNR before filtering: {snr_before:.2f} dB\n")
    f.write(f"SNR after filtering: {snr_after:.2f} dB\n")
    f.write(f"SNR improvement: {snr_improvement:.2f} dB\n")
    f.write(f"Dominant frequency: {dominant_frequency:.2f} Hz\n")

print("Results saved to data/results.txt")