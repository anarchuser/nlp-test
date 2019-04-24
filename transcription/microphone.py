#!/usr/bin/env python3

"""
NOTEPADAI
(Microphone)

Sends microphone input to the processor, for testing purposes
"""

import pyaudio

from transcription.processor import *

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
        print(data for data in self.process)

    def __to_array(self, stream):
        while True:
            yield stream.read(CHUNK)

