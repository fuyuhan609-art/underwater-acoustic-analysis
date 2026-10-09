import numpy as np
import matplotlib.pyplot as plt


# Signal parameters
sampling_rate = 44100
duration = 2
n = int(sampling_rate * duration)

frequency_resolution = sampling_rate / n

print(f"Number of samples: {n}")
print(f"Frequency resolution: {frequency_resolution:.2f} Hz")
frequency_1 = 1000
frequency_2 = 2500
frequency_3 = 4000

# Create time axis
t = np.linspace(
    0,
    duration,
    int(sampling_rate * duration),
    endpoint=False
)

# Generate clean signal
clean_signal = (
    np.sin(2 * np.pi * frequency_1 * t)
    + 0.5 * np.sin(2 * np.pi * frequency_2 * t)
    + 0.3 * np.sin(2 * np.pi * frequency_3 * t)
)

# Generate noise
noise = 0.3 * np.random.randn(len(t))

# Create noisy signal
noisy_signal = clean_signal + noise

# Perform FFT
fft_result = np.fft.fft(noisy_signal)

# Calculate frequency axis
frequencies = np.fft.fftfreq(len(noisy_signal), 1 / sampling_rate)

# Calculate magnitude
magnitude = np.abs(fft_result)

# Plot positive frequencies only
positive_frequencies = frequencies[:len(frequencies) // 2]
positive_magnitude = magnitude[:len(magnitude) // 2]
# Find the frequency with the highest magnitude
peak_index = np.argmax(positive_magnitude)
peak_frequency = positive_frequencies[peak_index]

print(f"Peak frequency: {peak_frequency:.2f} Hz")

from scipy.signal import find_peaks

peaks, properties = find_peaks(
    positive_magnitude,
    height=np.max(positive_magnitude) * 0.2
)

peak_frequencies = positive_frequencies[peaks]

print("Detected frequencies:")

for frequency in peak_frequencies:
    print(f"{frequency:.2f} Hz")

plt.figure(figsize=(10, 4))
plt.plot(positive_frequencies, positive_magnitude)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency Spectrum of Noisy Acoustic Signal")

plt.xlim(0, 5000)
plt.grid()

plt.show()
