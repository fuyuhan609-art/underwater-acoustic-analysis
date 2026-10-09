import matplotlib.pyplot as plt
import numpy as np

def plot_time_domain(
    time,
    noisy_signal,
    filtered_signal,
    output_path=None
):
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time, noisy_signal)
    plt.xlim(0, 0.005)
    plt.title("Noisy Underwater Acoustic Signal")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(time, filtered_signal)
    plt.xlim(0, 0.005)
    plt.title("Filtered Underwater Acoustic Signal")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300)

    plt.show()

    import numpy as np


def plot_frequency_domain(
    signal_before,
    signal_after,
    sampling_rate,
    output_path=None
):
    frequencies = np.fft.rfftfreq(
        len(signal_before),
        1 / sampling_rate
    )

    magnitude_before = np.abs(
        np.fft.rfft(signal_before)
    )

    magnitude_after = np.abs(
        np.fft.rfft(signal_after)
    )

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(frequencies, magnitude_before)
    plt.xlim(0, 5000)
    plt.title("Frequency Spectrum - Before Filtering")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(frequencies, magnitude_after)
    plt.xlim(0, 5000)
    plt.title("Frequency Spectrum - After Filtering")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300)

    plt.show()