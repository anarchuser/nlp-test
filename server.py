"""
NOTEPADAI
(Main script)

Server to transcript audio
"""

import audioStream_pb2_grpc
import audioStream_pb2

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


def is_valid(address):
    try:
        socket.inet_aton(address)
    except socket.error:
        return False
    return True


def get_valid_address(default):
    address = input("Use different address?: ")
    if address == '':
        return default
    if is_valid(address):
        return address
    else:
        return get_valid_address(default)


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

    def transcriptAudio(self, request_iterator, context):
        print("Connection received")
        for Samples in request_iterator:
            pass
        print("Connection Lost")

    def serve(self):
        print("Prepare servant")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=self.workers))
        audioStream_pb2_grpc.add_AudioProcessorServicer_to_server(self, server)
        server.add_insecure_port(self.host + ':' + str(self.port))

        print("Start serving")
        server.start()
        try:
            time.sleep(self.uptime)
        except KeyboardInterrupt:
            server.stop(None)
        print("Stop serving")


if __name__ == "__main__":
    # Set up and start the server
    print("Route servant - Default IP: " + HOST)
    ip = get_valid_address(default=HOST)

    print("Conceive servant")
    servant = AudioProcessorServicer(host=ip, port=PORT, uptime=FOREVER, workers=WORKERS)

    print("Enliven servant")
    servant.serve()

    print("Kill servant")
