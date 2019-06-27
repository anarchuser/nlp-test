<<<<<<< HEAD
"""
NOTEPADAI
(Database)

Class to manage the tsv files, for most easy access to all the data
"""


import numpy as np
import pandas as pd
import librosa
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


class Database:
    def __init__(self, path='./'):
        self.path = path
        self.tables = {}
        self.__load_tables()

    # Load all tsv files into a dict
    def __load_tables(self):
        for table in TABLES:
            try:
                self.tables[table] = pd.read_csv(os.path.join(self.path, table + FORMAT), sep='\t')
            except RuntimeError:
                raise FileNotFoundError

    def index(self, value, column, table="validated"):
        return np.where(self.tables[table][column] == value)[0][0]

    def open(self, file):
        return librosa.load(os.path.join(self.path, "clips", file + ".mp3"))

    def get_row(self, value, column="path", table="validated"):
        index = self.index(value, column, table)
        if not index:
            raise FileNotFoundError
        return self.tables[table][index:index+1]
