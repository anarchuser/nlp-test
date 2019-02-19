#!/usr/bin/env python3

"""
NOTEPADAI
(Main script)

Server to transcript audio streams and send them back
"""

import socket
import os
import time
import grpc
from concurrent import futures

import audioStream_pb2_grpc

HOST = '127.0.0.1'  # Server name
PORT = 12345         # Standard RTP port
CHUNK = 128
FOREVER = 10000000

def serve(UPTIME):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    audioStream_pb2_grpc.add_AudioProcessorServicer_to_server(audioStream_pb2_grpc.AudioProcessorServicer, server)
    server.add_insecure_port('[::]:' + str(PORT))
    server.start()
    try:
        time.sleep(UPTIME)
    except KeyboardInterrupt:
        server.stop()

print("Start serving.")
serve(FOREVER)
print("Stop serving.")