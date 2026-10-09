import numpy as np
from scipy.signal import butter, sosfilt

sampling_rate = 44100
duration = 2
target_frequency = 1000

t = np.linspace(
    0,
    duration,
    int(sampling_rate * duration),
    endpoint=False
)

# Generate clean signal
clean_signal = np.sin(2 * np.pi * target_frequency * t)

# Generate noise
noise = 0.8 * np.random.randn(len(t))

# Create noisy signal
noisy_signal = clean_signal + noise

signal_power = np.mean(clean_signal ** 2)
noise_power = np.mean(noise ** 2)

snr = 10 * np.log10(signal_power / noise_power)

print("Number of samples:", len(t))
print(f"Signal power: {signal_power:.4f}")
print(f"Noise power: {noise_power:.4f}")
print(f"SNR: {snr:.2f} dB")

# Design band-pass filter
low_cutoff = 800
high_cutoff = 1200

sos = butter(
    4,
    [low_cutoff, high_cutoff],
    btype="bandpass",
    fs=sampling_rate,
    output="sos"
)

# Apply filter
filtered_signal = sosfilt(sos, noisy_signal)

filtered_noise = filtered_signal - clean_signal

filtered_noise_power = np.mean(filtered_noise ** 2)

filtered_snr = 10 * np.log10(
    signal_power / filtered_noise_power
)

print(f"SNR before filtering: {snr:.2f} dB")
print(f"SNR after filtering: {filtered_snr:.2f} dB")

snr_improvement = filtered_snr - snr

print(f"SNR improvement: {snr_improvement:.2f} dB")