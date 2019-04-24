#!/usr/bin/env python3

"""
NOTEPADAI
(Preprocessor)

A script to download/check the data set in order to promise functionality
Reference: Mozilla Voice Dataset - https://voice.mozilla.org/en/datasets
"""

from urllib.request import Request, urlopen

import sys
import os
from os import path

URL = "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/de.tar.gz"

DIR = "Data"
FORMAT = "tsv"
FILES = [
    "dev",
    "invalidated",
    "other",
    "test",
    "train",
    "validated"
]


class Preprocessor:
    def __init__(self, data_dir='.', download=False):
        self.root_dir = data_dir
        if download:
            self.download_data()
        else:
            self.check_data()

    def download_data(self):
        print("Downloading a new data set to " + self.root_dir + " ...")
        data_set = urlopen(Request(URL)).read()

        print("Extracting archive...")

        print("Saving files...")
        print(data_set)

    def check_data(self):
        pass
