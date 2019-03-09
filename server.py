"""
NOTEPADAI
(Main script)

Server to transcript audio
"""

import audioStream_pb2_grpc
from processor import *

from concurrent import futures
import grpc
import time

""" Constants: """
HOST = '127.0.0.1'   # Server name
PORT = 12345         # Server port
FOREVER = 1000000    # Large number to keep the server running.
WORKERS = 8          # Max. amount of simultaneous threads
""""""


class AudioProcessorServicer(audioStream_pb2_grpc.AudioProcessorServicer):
    def __init__(self, host, port, uptime, workers):
        print("Mark servant (" + str(port) + ")")
        self.host = host
        self.port = port
        self.uptime = uptime
        self.workers = workers

    def TranscriptAudio(self, request_iterator, context):
        processor = Processor()                         # Create a new object to process the audio stream
        processor.start()                               # Start the thread the processor is working on
        processor.run()                                 # Start the actual processor
        for samples in request_iterator:
            for byte in samples.chunk:
                processor.samples.put(byte)             # Put data in sample queue
            while not processor.responses.Empty:
                yield processor.responses.get()          # Get data from response queue
        processor.stop()                                # Stop the thread

    def serve(self):
        print("Prepare servant")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=self.workers))
        audioStream_pb2_grpc.add_AudioProcessorServicer_to_server(audioStream_pb2_grpc.AudioProcessorServicer, server)
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
    print("Conceive servant")
    servant = AudioProcessorServicer(HOST, PORT, FOREVER, WORKERS)

    print("Enliven servant")
    servant.serve()

    print("Kill servant")
