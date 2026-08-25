from piper import PiperVoice
import wave

voice = PiperVoice.load("en_US-john-medium.onnx")


code_names = [
    "Tom and Jerry",
    "Mission Banana",
    "Agent Waffle",
    "Operation Chicken Rice",
    "Purple Otter",
    "Project Fishball"
]

for name in code_names:
    filename = name.lower().replace(" ", "_") + ".wav"

    with wave.open(filename, "wb") as f:
        voice.synthesize_wav(name, f)

    print(f"Generated: {filename}")