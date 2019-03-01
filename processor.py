#!/usr/bin/env python3

"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

import numpy
import pyaudio


class processor (object):
    def __init__(self, chunk):
        self.chunk = chunk
        self.buffer = []
