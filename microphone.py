#!/usr/bin/env python3

"""
NOTEPADAI
(Microphone)

Sends microphone input to the processor, for testing purposes
"""

import pyaudio
import audioStream_pb2

import processor

CHUNK = 10


def toArray(stream):
    samples = audioStream_pb2.Samples()
    while True:
        samples.chunk = stream.read(CHUNK)
        yield samples


print("Setting up audio stream")

p = pyaudio.PyAudio()
mic = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK)
processor = processor.Processor()

print("Processing audio stream")
data_stream = processor.process(toArray(mic))
for data in data_stream:
    input(data)
