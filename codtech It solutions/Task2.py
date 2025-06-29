
import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Load an audio file (wav format recommended)
with sr.AudioFile("sample_audio.wav") as source:
    audio = r.record(source)

# Convert speech to text
try:
    text = r.recognize_google(audio)
    print("Transcription:", text)
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))