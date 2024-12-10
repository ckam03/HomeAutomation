import speech_recognition as sr
import torch
import pyaudio


class VoiceInput:
    def __init__(self):
        self.audio = sr.AudioData
        self.builtin_mic = 5
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.r = sr.Recognizer()

    def get_microphone_input(self):
        with sr.Microphone(device_index=self.builtin_mic) as source:
            print("Say something!")
            self.audio = self.r.listen(source)
            print("audio captured")

    def get_audio(self) -> torch.Any | str:
        self.get_microphone_input()
        try:
            audio = self.r.recognize_whisper(
                self.audio, model="tiny", language="english"
            )
            if audio:
                return audio
        except sr.UnknownValueError:
            return "Whisper could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Whisper; {e}"

    def get_available_devices(self):
        # List all available audio devices
        print("Available audio devices:")
        for i in range(pyaudio.PyAudio().get_device_count()):
            device_info = pyaudio.PyAudio().get_device_info_by_index(i)
            print(f"Index {i}: {device_info['name']}")
