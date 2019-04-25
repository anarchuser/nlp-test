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
ARGS = {
    "server": "",
    "microphone": [
        "language",
        "interim results?"
    ]
}


def show_options():
    print("Syntax: " + sys.argv[0] + " [input] {arg1, arg2,...}")
    print("Input:")
    for option in list(OPTIONS):
        print("    " + option)
        for argc in range(len(ARGS[option])):
            print("        " + str(argc) + ": " + ARGS[option][argc])


if __name__ != "__main__":
    print("Who the hell imports a file called main.py???")
    sys.exit(1)
else:
    if len(sys.argv) < 2:
        print("Missing argument.")
        show_options()
        sys.exit(2)
    else:
        try:
            OPTIONS[sys.argv[1]](sys.argv[2:]).start()
        except KeyError:
            print("Unknown argument.")
            show_options()
            sys.exit(3)
        except KeyboardInterrupt:
            sys.exit(4)
