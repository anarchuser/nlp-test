"""
NOTEPADAI
(Main script)

Server to transcript audio
"""

from generated import audioStream_pb2_grpc, audioStream_pb2
from transcription.processor import *

from concurrent import futures
import grpc
import socket
import time

""" Constants: """
HOST = '192.168.44.103'     # Server name
PORT = 12345                # Server port
FOREVER = 1000000           # Large number to keep the server running.
WORKERS = 8                 # Max. amount of simultaneous threads
""""""


class Server:
    def __init__(self, host=HOST, port=PORT, uptime=FOREVER, workers=WORKERS):
        # Set up and start the server
        print("Route servant - Default IP: " + host)
        ip = self.get_valid_address(default=host)

        print("Conceive servant")
        print(ip)
        self.servant = AudioProcessorServicer(host=ip, port=port, uptime=uptime, workers=workers)

    def start(self):
        print("Enliven servant")
        self.servant.serve()

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


def string_to_response(word):
    response = audioStream_pb2.Response()
    response.word = word
    return response


class AudioProcessorServicer(audioStream_pb2_grpc.AudioProcessorServicer):
    def __init__(self, host, port, uptime, workers):
        print("Mark servant (" + str(port) + ")")
        self.host = host
        self.port = port
        self.uptime = uptime
        self.workers = workers

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=self.workers))

    def transcriptAudio(self, request_iterator, context):
        print("Connection received")
        for word in Processor().process(request_iterator):
            yield string_to_response(word)
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
