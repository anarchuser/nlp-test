"""
NOTEPADAI
(Server)

Server to connect to the world and transcript audio in a bidirectional stream
"""

from generated import audioStream_pb2_grpc, audioStream_pb2
from transcription.processor import *

from concurrent import futures
import grpc
import socket
import time

""" Constants: """
HOST = '192.168.43.51'     # Server name
PORT = 12345                # Server port
FOREVER = 1000000           # Large number to keep the server running.
WORKERS = 8                 # Max. amount of simultaneous threads

DEFAULT_LANG = "de_DE"      # The default target language
""""""


# Class handling the AudioStreamServicer internally
class Server:
    def __init__(self, argv=[]):
        # Set up and start the server
        print("Route servant - Default IP: " + str(HOST))
        ip = self.get_valid_address(default=HOST)

        print("Conceive servant")
        print(ip)
        self.servant = AudioProcessorServicer(host=ip, port=PORT, workers=WORKERS, argv=argv)

    def start(self):
        print("Enliven servant")
        self.servant.serve()
        time.sleep(FOREVER)
        self.servant.murder()

    def stop(self):
        print("Kill servant")
        self.servant.murder()

    def is_valid(self, address):
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return True

    def get_valid_address(self, default):
        address = input("Use different address?: ")
        if address == '':
            return default
        if self.is_valid(address):
            return address
        else:
            return self.get_valid_address(default)


# Actual server connecting to the outer world.
# Only used by the Server class
class AudioProcessorServicer(audioStream_pb2_grpc.AudioProcessorServicer):
    def __init__(self, host, port, workers, argv):
        print("Mark servant (" + str(port) + ")")
        self.host = host
        self.port = port
        self.workers = workers

        # Parse processor parameters from the argv parameter list
        self.lang = DEFAULT_LANG if len(argv) < 1 else argv[0]
        self.send_interim_results = False if len(argv) < 2 else bool(argv[1])
        self.print = False if len(argv) < 3 else bool(argv[2])
        print("  (Printing == " + str(self.print) + ")")

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=self.workers))

    def transcriptAudio(self, request_iterator, context):
        print("Connection received")

        processor = Processor(lang=self.lang, send_interim_results=self.send_interim_results)
        for word in processor.process(self.__sample_to_audio(request_iterator)):
            if self.print:
                print(word)
            yield self.__string_to_response(word)
        print("Connection lost")

    def serve(self):
        print("Prepare servant")
        audioStream_pb2_grpc.add_AudioProcessorServicer_to_server(self, self.server)
        self.server.add_insecure_port(self.host + ':' + str(self.port))

        print("Start serving")
        self.server.start()

    def murder(self):
        self.server.stop()
        print("Stop serving")

    def __sample_to_audio(self, samples):
        for sample in samples:
            yield sample.chunk

    def __string_to_response(self, word):
        response = audioStream_pb2.Response()
        response.word = word
        return response


