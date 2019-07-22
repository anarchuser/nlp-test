"""
NOTEPADAI
(Prepare)

A tool to segment the audio samples (spoken and written words) into phonemes
"""

from transcription import brain
from transcription.helper import *

import pandas as pd
import librosa.feature
import librosa.display
import matplotlib.pyplot as mp

import os
import sys
import time

import eyed3

CHUNK = 320  # Window Size

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

    def segment(self):
        self.__segment_text()
        return self.__segment_speech()

    def __segment_text(self):
        # TODO:
        #  Add phonetic spellings to table
        #   Finish db
        for table in TABLES:
            # TODO: Write to TSV
            for sentence in self.tables[table].sentence:
                for spelling in split_spellings(sentence):
                    # Write spellings in tsv file
                    pass

    def __segment_speech(self):
        try:
            for table in TABLES:
                # TODO: Write to TSV
                for file in self.tables[table].path:
                    audio, sr = librosa.load(os.path.join(self.path, "clips", file + ".mp3"))
                    for timestamp in split_phonemes(stream_to_librosa(audio_to_stream(audio))):
                        print(timestamp)
        except RuntimeError as e:
            print(e)

    def segment(self):
        self.__segment_text()
        return self.__segment_speech()

    def cepstrogram(self):
        # TODO:
        #  Save in file
        try:
            table = "validated"
            num = 0
            for file in self.tables[table].path:
                # Load audio & metadata
                path = os.path.join(self.path, "clips", file + ".mp3")
                audio, sr = librosa.load(path)
                metadata = eyed3.load(path)

                # Write metadata
                #metadata.tag.artist = entry.client_id
                metadata.tag.album = self.path
                metadata.tag.title = file
                #metadata.lyrics.set(entry.sentence)

                # Create images
                graph = librosa.feature.mfcc(audio, sr, n_mfcc=int(len(audio) / CHUNK), dct_type=2)
                mp.figure(figsize=(10, 4))
                librosa.display.specshow(graph, x_axis="time")
                mp.colorbar()
                mp.title(num)

                # Save & close
                mp.savefig(os.path.join(self.path, "images", file), orientation="landscape", quality=95, format="png")
                mp.close()
                print(str(num) + ":\t " + file)
                num += 1
                if num > 0:
                    sys.exit()

        except RuntimeError as e:
            print("Exception caught!:")
            print(e)

