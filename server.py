"""
NOTEPADAI
(Main script)

Server to transcript audioIntro to Audio Programming, Part 2: streams and send them back
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
        self.host = host
        self.port = port
        self.uptime = uptime
        self.workers = workers

    def TranscriptAudio(self, request_iterator, context):
        processor = Processor()                         # Create a new object to process the audio stream
        processor.start()                               # Start the thread the processor is working on
        processor.run()                                 # Start the actual processor
        for sample in request_iterator:
            for byte in samples.chunk:
                processor.samples.put(byte)             # Put data in sample queue
            while not processor.response.Empty:
                yield processor.response.get()          # Get data from response queue
        processor.stop()                                # Stop the thread

    def serve(self, **kwargs):
        """ Apply new arguments if available"""
        host = kwargs['host'] if kwargs['host'] else self.host
        port = kwargs['port'] if kwargs['port'] else self.port
        uptime = kwargs['time'] if kwargs['time'] else self.uptime
        workers = kwargs['workers'] if kwargs['workers'] else self.workers

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=workers))
        audioStream_pb2_grpc.add_AudioProcessorServicer_to_server(audioStream_pb2_grpc.AudioProcessorServicer, server)
        server.add_insecure_port(host + ':' + str(port))

        print("Start serving")
        server.start()
        try:
            time.sleep(uptime)
        except KeyboardInterrupt:
            print("Stop serving")
            server.stop()


if __name__ == "__main__":
    # Set up and start the server
    print("Conceive servant")
    servant = AudioProcessorServicer(HOST, PORT, FOREVER, WORKERS)

    print("Vitalise servant")
    servant.serve()

    print("Kill servant")
