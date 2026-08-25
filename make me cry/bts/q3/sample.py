from scipy.io import wavfile
from scipy.signal import resample_poly
import numpy as np

INPUT = ".wav/tom_and_jerry.wav"
OUTPUT = ".wav/tom_and_jerry_8khz.wav"

# Read WAV
sample_rate, audio = wavfile.read(INPUT)

print("Original sample rate:", sample_rate)
print("Original number of samples:", len(audio))

# Convert stereo → mono
if audio.ndim > 1:
    audio = audio.mean(axis=1)

# Resample to exactly 8000 Hz
audio_8khz = resample_poly(audio, 4000, sample_rate)

# Keep integer PCM format
audio_8khz = audio_8khz.astype(np.int16)

# Save the 8 kHz WAV
wavfile.write(OUTPUT, 4000, audio_8khz)

print("New sample rate: 8000 Hz")
print("New number of samples:", len(audio_8khz))