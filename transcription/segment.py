"""
NOTEPADAI
(Prepare)

A tool to segment the audio samples (spoken and written words) into phonemes
"""

from transcription import brain

import pandas as pd
import librosa
import matplotlib.pyplot as mp

import os

CHUNK = 640  # Window Size

FORMAT = ".tsv"
TABLES = [
    "dev",
    "invalidated",
    "other",
    "test",
    "train",
    "validated"
]


class Segment:
    def __init__(self, path='./'):
        self.path = path
        self.tables = {}
        self.__load_tables()

    # Load all tsv files into a dict
    def __load_tables(self):
        for table in TABLES:
            self.tables[table] = pd.read_csv(os.path.join(self.path, table + FORMAT), sep='\t')

    def segment(self, printout=False):
        self.__segment_text()
        return self.__segment_speech(printout)

    def __segment_text(self):
        # TODO:
        #  Read sentence
        #  Segment it
        #  Add it to table
        pass

    def __segment_speech(self, printout=False):
        try:
            if printout:
                audio, sr = librosa.load(os.path.join(self.path, "mp3", self.tables['validated'].path[0] + ".mp3"))
                """
                for value in brain.split_phonemes(self.__audio_to_stream(audio)):
                    print(value)
                    yield value
                """
                chunk = int(sr / 50)
                chunk = 320

                mp.plot([value + 1000 for value in brain.mfcc(self.__audio_to_stream(audio, chunk))])
                mp.plot([value for value in brain.mfcc_derivative(self.__audio_to_stream(audio, chunk))])
                mp.ylabel("Something something")
                mp.xlabel("Time in t/" + str(sr/chunk) + " seconds (Sample rate: " + str(sr) + ")")
                mp.show()
                #"""#
            else:
                for table in TABLES:
                    # TODO: Write to TSV
                    for file in self.tables[table].path:
                        audio, sr = librosa.load(os.path.join(self.path, "mp3", file + ".mp3"))
                        for timestamp in brain.split_phonemes(self.__audio_to_stream(audio)):
                            print(timestamp)
        except RuntimeError:
            pass

        pass

    def __audio_to_stream(self, audio, chunk):
        while True:
            samples = audio[:chunk]
            audio = audio[chunk:]
            if len(audio) is 0:
                break
            yield samples
