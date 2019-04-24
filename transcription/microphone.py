#!/usr/bin/env python3

"""
NOTEPADAI
(Microphone)

Sends microphone input to the processor, for testing purposes
"""


from transcription.processor import *
from generated import audioStream_pb2_grpc, audioStream_pb2

import pyaudio

CHUNK = 256


class Microphone:
    def __init__(self):
        print("Setting up audio stream")
        p = pyaudio.PyAudio()
        mic = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK)
        processor = Processor()
        print("Set up")

        self.process = processor.process(self.__to_array(mic))

    def start(self):
        for data in self.process:
            print(data)

    def __to_array(self, stream):
        while True:
            yield self.__to_sample(stream.read(CHUNK))

    def __to_sample(self, chunk):
        sample = audioStream_pb2.Samples()
        sample.chunk = chunk
        return sample

