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
        print("Start processing")
        self.isRunning = True
        dummy_text = "Transmission!"

        sample = [0]
        while len(sample) > 0:
            sample = librosa.util.buf_to_float(np.array(stream.__next__()))
            features = librosa.feature.mfcc(sample)
            print(features)
            yield dummy_text

