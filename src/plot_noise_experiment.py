
import pandas as pd
import matplotlib.pyplot as plt

# Load experiment results
df = pd.read_csv("data/noise_experiment.csv")

print(df)

# Plot SNR before and after filtering
plt.figure(figsize=(9, 5))

plt.plot(
    df["noise_amplitude"],
    df["snr_before_db"],
    marker="o",
    label="Before Filtering"
)

plt.plot(
    df["noise_amplitude"],
    df["snr_after_db"],
    marker="s",
    label="After Filtering"
)

plt.xlabel("Noise Amplitude")
plt.ylabel("SNR (dB)")
plt.title("SNR Before and After Band-Pass Filtering")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("data/noise_experiment_snr.png", dpi=150)
plt.show()

print("Plot saved to data/noise_experiment_snr.png")
