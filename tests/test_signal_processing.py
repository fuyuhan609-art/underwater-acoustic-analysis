import numpy as np
import pytest

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

def test_snr_decreases_when_noise_increases():
    _, clean, _, low_noise = generate_signal(
        sampling_rate=44100,
        duration=2,
        frequency=1000,
        noise_amplitude=0.1
    )

    _, _, _, high_noise = generate_signal(
        sampling_rate=44100,
        duration=2,
        frequency=1000,
        noise_amplitude=1.0
    )

    low_noise_snr = calculate_snr(clean, low_noise)
    high_noise_snr = calculate_snr(clean, high_noise)

    assert low_noise_snr > high_noise_snr

def test_filtered_signal_dominant_frequency():
    sampling_rate = 44100
    target_frequency = 1000

    _, clean, noisy, _ = generate_signal(
        sampling_rate=44100,
        duration=2,
        frequency=target_frequency,
        noise_amplitude=0.8
    )

    filtered = bandpass_filter(
        noisy,
        sampling_rate,
        800,
        1200
    )

    detected_frequency = detect_dominant_frequency(
        filtered,
        sampling_rate
    )

    assert abs(detected_frequency - target_frequency) < 5

def test_bandpass_filter_rejects_invalid_cutoffs():
    signal = np.ones(1000)

    with pytest.raises(ValueError):
        bandpass_filter(
            signal,
            sampling_rate=44100,
            low_cutoff=1200,
            high_cutoff=800
        )