#!/usr/bin/env python3

"""
NOTEPADAI
(Main script)

Server to transcript audioIntro to Audio Programming, Part 2: streams and send them back
"""

import audioStream_pb2_grpc
import processor

from concurrent import futures
import grpc
import time


""" Constants: """
HOST = '127.0.0.1'   # Server name
PORT = 12345         # Server port
CHUNK = 320          # Amount of bytes per packet
FOREVER = 1000000    # Large number to keep the server running.
WORKERS = 8          # Max. amount of simultaneous threads
""""""


class AudioProcessorServicer(audioStream_pb2_grpc.AudioProcessorServicer):
    def __init__(self, host, port, chunk, uptime, workers):
        self.host = host
        self.port = port
        self.chunk = chunk
        self.uptime = uptime
        self.workers = workers
        self.processor = processor.processor(chunk)

    def TranscriptAudio(self, request_iterator, context):
        for chunk in request_iterator:
            yield self.processor.exchangeData(chunk)

    def serve(self, **kwargs):
        """ Apply new arguments if available"""
        host = kwargs['host'] if kwargs['host'] else self.host
        port = kwargs['port'] if kwargs['port'] else self.port
        uptime = kwargs['time'] if kwargs['time'] else self.uptime
        workers = kwargs['workers'] if kwargs['workers'] else self.workers

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=workers))
        audioStream_pb2_grpc.add_AudioProcessorServicer_to_server(audioStream_pb2_grpc.AudioProcessorServicer, server)
        server.add_insecure_port(host + ':' + str(port))
        server.start()
        try:
            time.sleep(uptime)
        except KeyboardInterrupt:
            server.stop()


print("Conceive servant")
servant = AudioProcessorServicer(HOST, PORT, CHUNK, FOREVER, WORKERS)

print("Start serving.")
servant.serve()

print("Stop serving.")
