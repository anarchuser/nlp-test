#!/usr/bin/env python3

from transcription.segment import *

sc = Segment("Data/en")
sc.segment()
sc.db.save()
