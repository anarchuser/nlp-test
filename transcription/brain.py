"""
NOTEPADAI
(Brain)

Listens to music for hours and then tries to understand you - phonemes only
Data Set: provided by Mozilla's Voice project to provide training data for speech recognition algorithms
(
"""

import pandas as pd
import tensorflow as tf
from tensorflow import keras

from os import path
from pydub import AudioSegment


class Brain:
    def __init__(self, layers=(20, 20), functions=(tf.nn.sigmoid, tf.nn.softmax)):
        self.layers = layers
        self.functions = functions
        if len(functions) is not len(layers):
            raise Exception("Needs one function per layer")

        # Model:
        self.model = keras.Sequential([
            keras.layers.Dense(layers[i], activation=functions[i])
            for i in range(0, len(layers))])
        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    # Load pre-trained NN from file corresponding to structure
    def load(self):
        pass

    # Save trained NN to file under name corresponding to structure (e.g. NN_*TUPLE*)
    def save(self):
        pass

    # Train NN from training set
    def train(self):
        train_tsv = pd.read_csv(path.join("Data", "train.tsv"), sep='\t')
        audio = []
        for file in train_tsv.path:
            audio.append(path.join("Data", file))
        pass

    # Test NN using test set
    def test(self):
        test_tsv = pd.read_csv(path.join("Data", "test.tsv"), sep='\t')
        print(test_tsv.columns)
        pass

    # Process audio given a trained NN
    # Takes features in form of MFCC - https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
    def process(self, mfcc):
        return None


# Function to split an audio stream into a phoneme stream
def split_phonemes(stream):
    for samples in stream:
        # TODO: Return separated segments
        pass
