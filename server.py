#!/usr/bin/env python3

"""
NOTEPADAI
(Main script)

Server to transcript audioIntro to Audio Programming, Part 2: streams and send them back
"""

import audioStream_pb2_grpc

from concurrent import futures
import grpc
import time


""" Constants: """
HOST = '127.0.0.1'   # Server name
PORT = 12345         # Server port
CHUNK = 128          # Amount of bytes per packet
FOREVER = 1000000    # Large number to keep the server running.
WORKERS = 8          # Max. amount of simultaneous threads
""""""


""" Server: """
# Starts an gRPC server
def serve(host, port, chunk, uptime = FOREVER, workers = WORKERS):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=workers))
    audioStream_pb2_grpc.add_AudioProcessorServicer_to_server(audioStream_pb2_grpc.AudioProcessorServicer, server)
    server.add_insecure_port(host + ':' + str(port))
    server.start()
    try:
        time.sleep(uptime)
    except KeyboardInterrupt:
        server.stop()


print("Start serving.")
serve(HOST, PORT, CHUNK, FOREVER, WORKERS)
print("Stop serving.")
