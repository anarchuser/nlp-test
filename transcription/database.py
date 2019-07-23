"""
NOTEPADAI
(Database)

Class to manage the tsv files, for most easy access to all the data
"""


import numpy as np
import pandas as pd
import librosa
import os
import sys

FORMAT = ".tsv"
TABLES = [
    "dev",
    "invalidated",
    "other",
    "test",
    "train",
    "validated"
]


class Database:
    def __init__(self, path='./'):
        self.path = path
        self.tables = {}

    def load(self, path):
        self.path = path
        self.__load_tables()

    # Load all tsv files into a dict
    def __load_tables(self):
        for table in TABLES:
            try:
                self.tables[table] = pd.read_csv(os.path.join(self.path, table + FORMAT), sep='\t')
            except RuntimeError as e:
                print(e)
                raise FileNotFoundError

    def index(self, value, column, table="validated"):
        return np.where(self.tables[table][column] == value)[0][0]

    def audio(self, file):
        return librosa.load(self.path_of(file))

    def audio_from(self, table):
        for file in self.tables[table].path:
            yield self.find_row(file, "path", table), self.audio(file)

    def path_of(self, file):
        return os.path.join(self.path, "clips", file + ".mp3")

    def find(self, s_val, s_col, t_col, table):
        return self.find_row(s_val, s_col, table)[t_col]

    def find_row(self, s_val, s_col, table):
        index = self.index(s_val, s_col, table)
        return self.get_row(index, table), index

    def get(self, row, column, table="validated"):
        return self.get_row(row, table)[column]

    def get_row(self, row, table="validated"):
        try:
            return self.tables[table][row:row+1]
        except RuntimeError as e:
            print(e)
            sys.exit(1)

