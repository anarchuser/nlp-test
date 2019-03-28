#!/usr/bin/env python3

"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

import librosa
import numpy as np


class Processor:
    def __init__(self, stream):
        self.isRunning = False
        self.speech = stream
        self.features = self.extract_features()

    def process(self):
        print("Start processing")
        self.isRunning = True

        while True > 0:
            yield self.features.__next__()

        print("Stop processing")
        self.isRunning = False

    def extract_features(self):
        while True:
            sample_byte = np.array(self.speech.__next__())
            sample_float = librosa.util.buf_to_float(sample_byte)
            yield librosa.feature.mfcc(sample_float)
