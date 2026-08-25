import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

files = [
    "tom_and_jerry.wav",
    "tom_and_jerry_8khz.wav",
]

for filename in files:
    sample_rate, audio = wavfile.read(f".wav/{filename}")

    if audio.ndim > 1:
        audio = audio.mean(axis=1)

    samples = audio[:100].astype(float)
    samples /= np.max(np.abs(samples))

    time = np.arange(len(samples)) / sample_rate * 1000

    plt.plot(time, samples, label=filename)

plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()