#!/usr/bin/env python3

"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream

=== New algorithm for speech to text ===
"""

import queue
import threading
import numpy as np
import pyaudio

import time

class Processor (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.samples = queue.Queue()
        self.responses = queue.Queue()
        self.isRunning = False

    def run(self):
        print("Thread started.")
        self.process()

    def stop(self):
        self.isRunning = False

    def process(self):
        msg = "Transmission"

        self.isRunning = True
        print("start processing...")

        """ Test implementation: """

        while self.isRunning or not self.samples.empty:
            # TODO: Add the actual audio processing here
            # (Take bytes from samples queue, process them, put words into responses queue)
            self.responses.put(msg)
            time.sleep(1)

        """ End of Test """