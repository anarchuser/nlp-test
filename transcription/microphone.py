#!/usr/bin/env python3

"""
NOTEPADAI
(Microphone)

Sends microphone input to the processor, for testing purposes
"""


from transcription.processor import *
from generated import audioStream_pb2_grpc, audioStream_pb2

import pyaudio
import sys

CHUNK = 256


class Microphone:
    def __init__(self, argv):
        print("Setting up audio stream")
        p = pyaudio.PyAudio()
        self.mic = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK)

        lang = "de_DE" if len(argv) < 1 else argv[0]
        send_interim_results = len(argv) < 2 and False or bool(argv[1])

        self.processor = Processor(lang, send_interim_results)
        print("Set up")

    def start(self):
        for data in self.processor.process(self.__generator__()):
            print(data)

    def __generator__(self):
        while True:
            yield self.__to_sample(self.mic.read(CHUNK))

    def __to_sample(self, chunk):
        sample = audioStream_pb2.Samples()
        sample.chunk = chunk
        return sample

