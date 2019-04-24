#!/usr/bin/env python3

"""
NOTEPADAI

Main Script for testing the transcription. Run with respective cli args
"""

from transcription import microphone, server

import sys

OPTIONS = {
    "server": server.Server,
    "microphone": microphone.Microphone
}


def show_options():
    print("Syntax: " + sys.argv[0] + " [options]")
    print("Options:")
    for option in list(OPTIONS):
        print("    " + option)


if __name__ != "__main__":
    print("Who the hell imports a file called main.py???")
    sys.exit(1)
else:
    if len(sys.argv) != 2:
        print("Wrong number of cli args.")
        show_options()
        sys.exit(2)
    else:
        try:
            OPTIONS[sys.argv[1]]().start()
        except KeyError:
            print("Unknown argument.")
            show_options()
            sys.exit(3)
        except KeyboardInterrupt:
            sys.exit(4)
