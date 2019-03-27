#!/usr/bin/env python3

"""
NOTEPADAI
(Microphone)

Sends microphone input to the processor, for testing purposes
"""

import pyaudio
import time

CHUNK = 300

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt8, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK)

try:
    while True:
        data = stream.read(CHUNK)
        print(data)
        time.sleep(10)
except KeyboardInterrupt:
    print("Stop recording")
