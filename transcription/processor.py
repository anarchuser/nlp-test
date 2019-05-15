"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

from transcription.helper import *
from transcription.brain import *

import tensorflow as tf
import nltk

NUM_FEATURES = 20           # MFCC returns 20 features TODO: REWORK THIS


class Processor:
    def __init__(self):
        self.isRunning = False
        self.brain = Brain(layers=(NUM_FEATURES, 25, 30), functions=(tf.nn.sigmoid, tf.nn.relu, tf.nn.softmax))

    # Apply future neural network
    def process(self, speech):
        print("Start processing")
        self.isRunning = True

        phonemes = split_phonemes(stream_to_librosa(speech))
        phonetic_spellings = self.brain.process(phonemes)

        return self.concatenate(phonetic_spellings)

    # TODO
    # Convert recognized phonemes into words
    def concatenate(self, spellings):
        for spelling in spellings:
            yield spelling
