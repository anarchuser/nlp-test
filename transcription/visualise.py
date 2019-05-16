"""
NOTEPADAI
(Visualiser)

A data science tool to produce cool graphs accompanying the process of speech recognition
"""


from transcription.helper import *

import librosa
import vlc
import matplotlib.pyplot as plt

CHUNK = 320


class Visualise:
    def __init__(self, path):
        self.path = path
        self.data, self.sample_rate = librosa.load(path)
        self.__player__ = vlc.MediaPlayer(path)

    def play(self):
        self.__player__.play()

    def mfcc(self):
        return [convert(data) for data in self.as_mfcc_stream()]

    def mfcc_d(self):
        pass

    def as_mfcc_stream(self, chunk=CHUNK):
        for window in audio_to_stream(self.data, chunk):
            yield librosa.feature.mfcc(window)

    def as_audio_stream(self, chunk=CHUNK):
        return audio_to_stream(self.data, chunk)


def specgram(obj, xlabel=None, ylabel=None, axis=None, chunk=CHUNK):
    s = plt
    s.specgram(obj.data, NFFT=chunk, Fs=obj.sample_rate)

    if xlabel is not None:
        s.xlabel(xlabel)
    if ylabel is not None:
        s.ylabel(ylabel)
    if axis is not None:
        s.axis(axis)

    s.show()


def convert(coefficients):
    return [data for data in [pair for pair in coefficients]]
