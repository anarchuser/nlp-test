#!/usr/bin/env python3

from transcription.helper import *
from transcription.database import *

import matplotlib.pyplot as mp

import sys

db = Database("Data/en")
audio, sr = db.open(sys.argv[1])
mfcc = [x for x in mfcc(audio_to_stream(audio))]
xs = [x for x in mfcc]
#print(mfcc)
print(xs)

#mp.xkcd()
mp.plot(audio)
mp.plot(xs)
mp.ylabel("Amplitude")
mp.xlabel("Samples (" + str(sr) + "/second)")
mp.show()
