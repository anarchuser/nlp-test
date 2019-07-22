#!/usr/bin/env python3

from transcription import segment

scissors = segment.Segment("Data/en")

try:
    # scissors.segment()

    print("Start printing cepstrograms")
    scissors.cepstrogram()
except KeyboardInterrupt:
    print("Interrupted by user")
    print("Exiting...")