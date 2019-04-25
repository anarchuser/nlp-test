"""
NOTEPADAI
(Microphone)

Sends microphone input to the processor, for testing purposes
"""


from transcription.processor import *
from generated import audioStream_pb2

import pyaudio

CHUNK = int(RATE / 10)  # 100ms


class Microphone:
    def __init__(self, argv):
        print("Setting up audio stream")
        p = pyaudio.PyAudio()
        self.mic = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK)

        # Parse processor parameters from the argv parameter list
        lang = "de_DE" if len(argv) < 1 else argv[0]
        send_interim_results = len(argv) < 2 and False or bool(argv[1])

        # Initialise a new Processor object used in .start()
        self.processor = Processor(lang, send_interim_results)
        print("Set up")

    # Sends the audio stream from the microphone to the Processor object
    # and prints the result
    def start(self):
        for data in self.processor.process(self.__generator__()):
            print(data)

    # transforms a stream of audio data into a stream of gRPC Samples
    # (which are used by the processor, so Microphone and Server can be changed interchangeably)
    def __generator__(self):
        while True:
            yield self.__to_sample(self.mic.read(CHUNK))

    # Returns a new Sample object containing audio samples
    def __to_sample(self, chunk):
        sample = audioStream_pb2.Samples()
        sample.chunk = chunk
        return sample

