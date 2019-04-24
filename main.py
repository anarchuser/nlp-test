#!/usr/env/python3

"""
NOTEPADAI

Main Script for testing the transcription. Run with respective cli args
"""

from transcription import microphone, prepare, processor, server
from generated import audioStream_pb2, audioStream_pb2_grpc

import sys


def options():
    pass


if __name__ != "__main__":
    print("Who the hell imports a file called main.py???")
    sys.exit(1)
else:
    if len(sys.argv) != 2:
        print("Wrong number of cli args.")
        options()
        sys.exit(2)
    else:
        if sys.argv[1] == "server":
            server.Server().start()
        elif sys.argv[1] == "microphone":
            microphone.Microphone().start()
        else:
            print("Unknown argument.")
            options()
            sys.exit(3)
