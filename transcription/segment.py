"""
NOTEPADAI
(Prepare)

A tool to segment the audio samples (spoken and written words) into phonemes
"""

from transcription import brain
from transcription.helper import *
from transcription.database import *

import pandas as pd
import librosa.feature
import librosa.display
import matplotlib.pyplot as mp

import os
import sys
import time

import eyed3

DEBUG = False

CHUNK = 320  # Window Size
MAX_AMNT = 4000  # Amount of cepstrograms to be produced


class Segment:
    def __init__(self, path='./'):
        self.path = path
        self.db = Database()

        try:
            self.db.load(path)
        except IOError:
            print("Couldn't open tables")
            sys.exit(1)

    def __segment_text(self):
        # TODO:
        #  Add phonetic spellings to table
        for table in TABLES:
            print("#### {}".format(table))
            #self.db.tables[table].spellings = "."
            for index in self.db.tables[table].index:
                sentence = self.db.get(index, "sentence", table)
                phonemes = [spelling for spelling in split_spellings(sentence)]
                self.db.tables[table]["spellings"][index] = [phonemes]

                if DEBUG:
                    print("{} {}".format(index, sentence))

    def __segment_speech(self):
        try:
            for table in TABLES:
                # TODO: Write to TSV
                for audio, sr in self.db.audio_from(table):
                    for timestamp in split_phonemes(stream_to_librosa(audio_to_stream(audio))):
                        print(timestamp)
        except RuntimeError as e:
            print(e)

    def segment(self):
        self.__segment_text()
        # self.__segment_speech()

    def cepstrogram(self):
        # TODO:
        #  Save in file
        try:
            table = "validated"
            for (metadata, index), (audio, sr) in self.db.audio_from(table):
                # Load audio & metadata
                file = metadata.path[index]
                path = self.db.path_of(file)
                id3 = eyed3.load(path)

                print("|-{}:\t {}".format(index, file))

                # Write metadata
                try:
                    id3.tag.artist = metadata.client_id[index]
                    id3.tag.album = self.path
                    id3.tag.title = file
                    # TODO:
                    #  Fix this:
                    # id3.tag.lyrics = metadata.sentence[index]
                    id3.tag.save()
                except AttributeError:
                    print(" \\ No metadata set!")

                # Create & save plots
                graph = librosa.feature.mfcc(audio, sr, n_mfcc=int(len(audio) / CHUNK), dct_type=2)
                mp.figure(figsize=(10, 4))
                librosa.display.specshow(graph, x_axis="time")
                mp.colorbar()
                mp.title(index)
                mp.savefig(os.path.join(self.path, "images", "{}:{}".format(index, file)), orientation="landscape", quality=95, format="png")
                mp.close()

                if index >= MAX_AMNT - 1:
                    sys.exit()

        except RuntimeError as e:
            print("Exception caught!:")
            print(e)

