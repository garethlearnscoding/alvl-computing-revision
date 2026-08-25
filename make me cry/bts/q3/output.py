from scipy.io import wavfile
import numpy as np
import csv

INPUT = "tom_and_jerry_8khz.wav"

# Read the 8 kHz WAV
sample_rate, audio = wavfile.read(INPUT)

print("Sample rate:", sample_rate)
print("Number of samples:", len(audio))
print()

# Check that it is actually 8 kHz
if sample_rate != 8000:
    raise ValueError(f"Expected 8000 Hz, got {sample_rate} Hz")

audio_normalised = audio.astype(float) / 32768

samples = audio_normalised[::2]

data = np.column_stack((np.arange(len(samples)), samples))

np.savetxt(
    "samples.csv",
    data,
    delimiter=",",
    fmt=["%d", "%.6f"],
    header="Sample,Amplitude",
    comments=""
)