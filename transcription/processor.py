"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

from transcription.brain import *

import librosa
import tensorflow as tf
import numpy as np
import queue

NUM_FEATURES = 20           # MFCC returns 20 features


class Processor:
    def __init__(self):
        self.isRunning = False
        self.brain = Brain(layers=(NUM_FEATURES, 25, 30), functions=(tf.nn.sigmoid, tf.nn.relu, tf.nn.softmax))
        self.phonemes = queue.Queue()

    # Apply future neural network
    def process(self, speech):
        print("Start processing")
        self.isRunning = True

        for sample in speech:
            data = sample.chunk
            features = self.extract_features(data)
            phoneme = self.recognize_phoneme(features)
            self.phonemes.put(phoneme)
            word = self.understand_word()
            yield word

        print("Stop processing")
        self.isRunning = False

    def extract_features(self, window):
        samples_b = np.array(window)
        samples_f = librosa.util.buf_to_float(samples_b)
        return librosa.feature.mfcc(samples_f)

    def recognize_phoneme(self, mfcc):
        return self.brain.process(mfcc)

    def understand_word(self):
        return "Transmission!"
