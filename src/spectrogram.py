import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Signal parameters
sampling_rate = 44100
duration = 2

# Create time axis
t = np.linspace(
    0,
    duration,
    int(sampling_rate * duration),
    endpoint=False
)
# Generate time-varying signal
frequency = np.where(t < 1, 1000, 3000)

# Generate signal
clean_signal = np.sin(2 * np.pi * frequency * t)

# Add noise
noise = 0.3 * np.random.randn(len(t))

# Create noisy signal
noisy_signal = clean_signal + noise

# Calculate spectrogram
frequencies, times, Sxx = spectrogram(
    noisy_signal,
    fs=sampling_rate,
    nperseg=512
)

# Plot spectrogram
plt.figure(figsize=(10, 5))

plt.pcolormesh(
    times,
    frequencies,
    10 * np.log10(Sxx),
    shading="gouraud"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.title("Spectrogram of Simulated Underwater Acoustic Signal")

plt.ylim(0, 5000)

plt.colorbar(label="Power/Frequency (dB/Hz)")

plt.savefig("data/spectrogram.png", dpi=300)
plt.show()