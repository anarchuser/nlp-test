#!/usr/bin/env python3

from transcription import segment

scissors = segment.Segment("Data/de")

try:
    scissors.segment(True)
except KeyboardInterrupt:
    print("Interrupted by user")
    print("Exiting...")