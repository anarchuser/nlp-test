"""
NOTEPADAI
(Brain)

Listens to music for hours and then tries to understand you - phonemes only
Data Set: provided by Mozilla's Voice project to provide training data for speech recognition algorithms
(
"""

from transcription import processor

import pandas as pd
import tensorflow as tf
from tensorflow import keras
import librosa


from os import path
import sys
from pydub import AudioSegment


BORDER = 0  # Border to detect different syllables


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
def mfcc_derivative(stream):
    mem = stream.__next__()
    SAMPLES_PER_WINDOW = len(mem)
    timesteps = 0
    for samples in stream:
        samples += SAMPLES_PER_WINDOW

        window = processor.arr_to_librosa(samples)
        try:
            window = librosa.feature.mfcc(window)
        except ValueError:
            continue

        try:
            yield is_different_mfcc_d(mem, window)

            #if is_different(mem, window):
            #    yield timesteps
        except IndexError:
            pass
        except ValueError:
            pass
        except RuntimeError:
            pass

        mem = window


def is_different_mfcc_d(win_a, win_b):
    diff = 0
    for i in range(len(win_a)):
        for j in range(2):
            diff += abs(win_b[i][j] - win_a[i][j])

    return diff
    return False
    #return diff > BORDER


def mfcc(stream):
    mem = stream.__next__()
    SAMPLES_PER_WINDOW = len(mem)
    timesteps = 0
    stream.__next__()
    for samples in stream:
        samples += SAMPLES_PER_WINDOW

        window = processor.arr_to_librosa(samples)
        try:
            window = librosa.feature.mfcc(window)
        except ValueError:
            continue

        try:
            yield is_different_mfcc(window)

            #if is_different(mem, window):
            #    yield timesteps
        except IndexError:
            pass
        except ValueError:
            pass
        except RuntimeError:
            pass


def is_different_mfcc(window):
    summ = 0
    for i in range(1, len(window)):
        for j in range(2):
            summ += abs(window[i][j])

    return summ
    return False
    #return diff > BORDER
