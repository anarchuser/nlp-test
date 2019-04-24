#!/usr/bin/env python3

"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

import librosa
import numpy as np
import time


class Processor:
    def __init__(self):
        self.isRunning = False

    def process(self, stream):
        print("Start processing")
        self.isRunning = True

        dummy_text = "Transmission!"

        sample = [0]
        while len(sample) > 0:
            sample = stream.__next__()
            yield dummy_text
