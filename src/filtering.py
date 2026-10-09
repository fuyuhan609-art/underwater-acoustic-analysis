import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt
from scipy.signal import find_peaks

# Signal parameters
sampling_rate = 44100
duration = 2

# Target frequency
target_frequency = 1000

# Create time axis
t = np.linspace(
    0,
    duration,
    int(sampling_rate * duration),
    endpoint=False
)

# Generate target signal
clean_signal = np.sin(
    2 * np.pi * target_frequency * t
)

# Generate noise
noise = 0.8 * np.random.randn(len(t))

# Create noisy signal
noisy_signal = clean_signal + noise

# Design a band-pass filter
low_cutoff = 800
high_cutoff = 1200

sos = butter(
    4,
    [low_cutoff, high_cutoff],
    btype="bandpass",
    fs=sampling_rate,
    output="sos"
)

# Apply the filter
filtered_signal = sosfilt(sos, noisy_signal)


# FFT of noisy signal
noisy_fft = np.fft.rfft(noisy_signal)
noisy_magnitude = np.abs(noisy_fft)

# FFT of filtered signal
filtered_fft = np.fft.rfft(filtered_signal)
filtered_magnitude = np.abs(filtered_fft)

# Frequency axis
frequencies = np.fft.rfftfreq(
    len(noisy_signal),
    1 / sampling_rate
)
peak_index = np.argmax(filtered_magnitude)
peak_frequency = frequencies[peak_index]

print(f"Dominant frequency after filtering: {peak_frequency:.2f} Hz")
# Plot noisy signal
# Plot original and filtered signals
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, noisy_signal)
plt.xlim(0, 0.005)
plt.title("Noisy Signal")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal)
plt.xlim(0, 0.005)
plt.title("Filtered Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()


# Plot frequency spectra
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(frequencies, noisy_magnitude)
plt.xlim(0, 5000)
plt.title("Frequency Spectrum - Before Filtering")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(frequencies, filtered_magnitude)
plt.xlim(0, 5000)
plt.title("Frequency Spectrum - After Filtering")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

plt.tight_layout()
plt.show()

