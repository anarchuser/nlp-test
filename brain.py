#!/usr/bin/env python3

"""
NOTEPADAI
(Brain)

Listens to music for hours and then tries to understand you - phonemes only
Data Set: provided by Mozilla's Voice project to provide training data for speech recognition algorithms
(
"""

import pandas as pd

class Brain:
    def __init__(self, structure):
        self.structure = structure      # Tuple; index = layer, value = nodes of layer
        self.neurons = 0                # TODO: Create NN

    # Load pre-trained NN from file corresponding to structure
    def load(self):
        pass

    # Save trained NN to file under name corresponding to structure (e.g. NN_*TUPLE*)
    def save(self):
        pass

    # Train NN from training set
    def train(self):
        train_tsv = pd.read_csv("Data/train.tsv", sep='\t')
        pass

    # Test NN using test set
    def test(self):
        test_tsv = pd.read_csv("Data/test.tsv", sep='\t')
        pass

    # Process audio given a trained NN
    # Takes features in form of MFCC - https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
    def process(self, mfcc):
        pass

