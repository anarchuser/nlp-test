#!/usr/bin/env python3

"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

import librosa
import numpy as np
import time

class Processor():
    def __init__(self):
        self.isRunning = False

    def process(self, stream):
        self.isRunning = True
        dummy_text = "Transmission!"

        sample = [0]
        while sample:
            sample = stream.read(1)
            print(sample)
            features = librosa.feature.mfcc(sample)
            print(features)
            time.sleep(1)
            yield dummy_text
