#!/usr/bin/env python3

"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

import librosa
import numpy as np
import queue


class Processor:
    def __init__(self):
        self.isRunning = False
        self.phonemes = queue.Queue()

    # Apply future neural network
    def process(self, speech):
        print("Start processing")
        self.isRunning = True

        for samples in speech:
            data = samples.chunk
            features = self.extract_features(data)
            phoneme = self.recognize_phoneme(features)
            self.phonemes.put(phoneme)
            word = self.understand_word()
            yield phoneme

        print("Stop processing")
        self.isRunning = False

    # Train future neural network
    def train(self):
        pass

    # Test future neural network
    def test(self):
        pass

    def extract_features(self, window):
        samples_b = np.array(window)
        samples_f = librosa.util.buf_to_float(samples_b)
        return librosa.feature.mfcc(samples_f)

    def recognize_phoneme(self, mfcc):
        return mfcc

    def understand_word(self):
        return "Transmission!"
