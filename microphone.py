#!/usr/bin/env python3

"""
NOTEPADAI
(Microphone)

Sends microphone input to the processor, for testing purposes
"""

import pyaudio
import time

import processor

CHUNK = 256


def toArray(stream):
    while True:
        yield stream.read(CHUNK)

print("Setting up audio stream")

p = pyaudio.PyAudio()
mic = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK)
processor = processor.Processor()

print("Set up")

process = processor.process(toArray(mic))

for data in process:
    print(data)
