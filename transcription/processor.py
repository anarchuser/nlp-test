"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

from transcription.helper import *
from transcription.brain import *

import tensorflow as tf
import nltk


class Processor:
    def __init__(self):
        self.isRunning = False
        self.brain = Brain(layers=(), functions=())  # TODO

    # Apply future neural network
    def process(self, speech):
        print("Start processing")
        self.isRunning = True

        phonemes = split_phonemes(stream_to_librosa(speech))
        phonetic_spellings = self.brain.process(phonemes)
        words = self.concatenate(phonetic_spellings)
        return words

    # TODO:
    #  Convert recognized phonemes into words
    def concatenate(self, spellings):
        for spelling in spellings:
            word = spelling
            yield word

        print("Stop processing")
        self.isRunning = False
