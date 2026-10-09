import numpy as np
from scipy.signal import butter, sosfilt


def generate_signal(
    sampling_rate,
    duration,
    frequency,
    noise_amplitude=0.0
):
    t = np.linspace(
        0,
        duration,
        int(sampling_rate * duration),
        endpoint=False
    )

    clean_signal = np.sin(
        2 * np.pi * frequency * t
    )

    noise = noise_amplitude * np.random.randn(len(t))

    noisy_signal = clean_signal + noise

    return t, clean_signal, noisy_signal, noise


def calculate_snr(signal, noise):
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)

    return 10 * np.log10(
        signal_power / noise_power
    )


def bandpass_filter(
    signal,
    sampling_rate,
    low_cutoff,
    high_cutoff
):
    if not 0 < low_cutoff < high_cutoff < sampling_rate / 2:
        raise ValueError(
            "Cutoff frequencies must satisfy "
            "0 < low_cutoff < high_cutoff < Nyquist frequency."
        )

    sos = butter(
        4,
        [low_cutoff, high_cutoff],
        btype="bandpass",
        fs=sampling_rate,
        output="sos"
    )

    return sosfilt(sos, signal)

def detect_dominant_frequency(signal, sampling_rate):
    fft_result = np.fft.rfft(signal)

    magnitude = np.abs(fft_result)

    frequencies = np.fft.rfftfreq(
        len(signal),
        1 / sampling_rate
    )

    peak_index = np.argmax(magnitude)

    return frequencies[peak_index]