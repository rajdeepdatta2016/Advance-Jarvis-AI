import pyaudio
import numpy as np

# Constants for audio processing
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate (adjust to your needs)
CHUNK = 1024  # Size of each audio chunk
THRESHOLD = 32000  # Adjust this threshold based on your environment and microphone sensitivity

def Tester():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for claps...")

    while True:
        try:
            data = stream.read(CHUNK)
            audio_data = np.frombuffer(data, dtype=np.int16)
            
            # Check if the audio data exceeds the threshold
            if np.max(np.abs(audio_data)) > THRESHOLD:
                print("Clap detected!")
                break
        except KeyboardInterrupt:
            break

    # print("Stopped listening.")
    stream.stop_stream()
    stream.close()
    p.terminate()

# if __name__ == "__main__":
#     Tester()
