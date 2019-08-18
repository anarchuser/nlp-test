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
    def __init__(self, path=None):
        self.isLoaded = False
        self.path = path
        self.tables = {}
        if path:
            try:
                self.load(path)
            except IOError:
                print("Couldn't load database from given files!")

    def load(self, path):
        self.path = path
        self.__load_tables()
        self.isLoaded = True

    def save(self, path=None):
        path = path if path else self.path
        for table in TABLES:
            fname = os.path.join(path, "{}_MOD{}".format(table, FORMAT))
            try:
                print("Writing {}...".format(fname), end='\0')
                self.tables[table].to_csv(fname, sep='\t')
                print("Done")
            except RuntimeError as e:
                print(e)
                raise IOError
        print("Database modified successfully.")

    # Load all tsv files into a dict
    def __load_tables(self):
        for table in TABLES:
            fname = os.path.join(self.path, table + FORMAT)
            try:
                print("Reading {}...".format(fname), end='\0')
                self.tables[table] = pd.read_csv(fname, sep='\t')
                print("Done")
            except RuntimeError as e:
                print(e)
                raise IOError
        print("Database loaded successfully.")

    def index(self, value, column, table):
        return self.find_row(value, column, table).index

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
        return self.tables[table][self.tables[table][s_col] == s_val]

    def get(self, row, column, table):
        return self.get_row(row, table)[column][0]

    def get_row(self, row, table):
        try:
            return self.tables[table][self.tables[table].index == row]
        except RuntimeError as e:
            print(e)
            sys.exit(1)

