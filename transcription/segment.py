"""
NOTEPADAI
(Prepare)

A tool to segment the audio samples (spoken and written words) into phonemes
"""

import pandas as pd

import os

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

    # Load all tsv files into a dict
    def __load_tables(self):
        for table in TABLES:
            self.tables.update([table, pd.read_csv(os.path.join(self.path, table + FORMAT), sep='\t')])

    def __segment_text(self):
        # TODO:
        #  Read sentence
        #  Segment it
        #  Add it to table
        pass

    def __segment_speech(self):
        # TODO:
        #  Load mp3 file
        #  Convert it to wav
        #  Look how many phonemes there should be
        #  Try to locate them
        pass
