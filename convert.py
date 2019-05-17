#!/usr/bin/env python3

import pydub
from pydub import AudioSegment

import sys
import os
from os import path


def convert(bp=None):
	reachedBP = (bp is not None)
	failedCounter = 0
	with open("ls.txt") as ls:
		for file in ls:
			file = file[:-1]
			if reachedBP:
				if file == bp:
					reachedBP = False
				continue
			try:
				clip = AudioSegment.from_mp3(path.join("mp3", file))
				clip.export(path.join("wav", file[:-3] + "wav"), format="wav")
				del clip
			except pydub.exceptions.CouldntDecodeError:
				failedCounter += 1
				print("Couldn't decode file!")
				os.system("echo " + file + " >> failed_decodings.log")
				continue
			print("Successfully converted file '" + file + "'")
		print("Finished converting with " + str(failedCounter) + " failed decodings! (See log)")


if __name__ == "__main__":
	convert(sys.argv[-1] if len(sys.argv) == 2 else None)

