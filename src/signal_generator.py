import numpy as np
import matplotlib.pyplot as plt


# Signal parameters
sampling_rate = 44100
duration = 2
frequency = 1000

# Create time axis
t = np.linspace(
    0,
    duration,
    int(sampling_rate * duration),
    endpoint=False
)

# Generate a clean sine wave
clean_signal = np.sin(2 * np.pi * frequency * t)

# Generate random noise
noise = 0.3 * np.random.randn(len(t))

# Combine signal and noise
noisy_signal = clean_signal + noise

# Plot the noisy signal
plt.figure(figsize=(10, 4))
plt.plot(t, noisy_signal)

# Show only the first 5 milliseconds
plt.xlim(0, 0.005)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Simulated Noisy Underwater Acoustic Signal")
plt.grid()
plt.show()