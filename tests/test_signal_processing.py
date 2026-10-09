import numpy as np

from src.signal_processing import (
    generate_signal,
    calculate_snr,
    bandpass_filter,
    detect_dominant_frequency
)


def test_generate_signal():

    t, clean, noisy, noise = generate_signal(
        sampling_rate=44100,
        duration=2,
        frequency=1000,
        noise_amplitude=0.5
    )

    assert len(t) == 88200
    assert len(clean) == 88200
    assert len(noisy) == 88200
    assert len(noise) == 88200


def test_calculate_snr():

    signal = np.ones(1000)
    noise = np.ones(1000) * 0.1

    snr = calculate_snr(signal, noise)

    assert snr > 15


def test_bandpass_filter():

    sampling_rate = 44100

    signal = np.sin(
        2 * np.pi * 1000 *
        np.arange(44100) / sampling_rate
    )

    filtered = bandpass_filter(
        signal,
        sampling_rate,
        800,
        1200
    )

    assert len(filtered) == len(signal)
    assert np.max(np.abs(filtered)) > 0.1


def test_dominant_frequency():

    sampling_rate = 44100
    frequency = 1000

    t = np.arange(44100) / sampling_rate

    signal = np.sin(
        2 * np.pi * frequency * t
    )

    detected_frequency = detect_dominant_frequency(
        signal,
        sampling_rate
    )

    assert abs(detected_frequency - frequency) < 1