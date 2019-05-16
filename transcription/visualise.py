"""
NOTEPADAI
(Visualiser)

A data science tool to produce cool graphs accompanying the process of speech recognition
"""


from transcription.helper import *

import librosa

CHUNK = 320


class Visualise:
    def __init__(self, path):
        self.path = path
        self.file = librosa.load(path)

    def play(self):
        pass

    def show_mfcc(self):
        pass

    def show_mfcc_d(self):
        pass

    def as_mfcc_stream(self, chunk=CHUNK):
        for window in audio_to_stream(self.file, chunk):
            yield librosa.feature.mfcc(window)

    def as_stream(self, chunk=CHUNK):
        return audio_to_stream(self.file, chunk)

