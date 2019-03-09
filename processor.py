#!/usr/bin/env python3

"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

import queue
import threading
import numpy
import pyaudio


class Processor (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.samples = queue.Queue
        self.responses = queue.Queue
        self.isRunning = False

    def run(self):
        print("Received connection from phone!!!")
        msg = "Transmission"

        self.isRunning = True
        while self.isRunning and not self.samples.empty:

            # Test to see whether data arrives
            if not self.samples.empty:
                print(self.samples.get())

            # TODO: Add the actual audio processing here
            # (Take bytes from samples queue, process them, put words into responses queue)
            self.responses.put(item=msg)

    def stop(self):
        self.isRunning = False
