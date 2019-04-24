#!/usr/bin/env python3

"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

from __future__ import division
from os import environ
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

import threading

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../hypnote-e16ff3ca8e86.json"
print(environ["GOOGLE_APPLICATION_CREDENTIALS"])


class Processor(threading.Thread):
    def __init__(self):
        self.isRunning = False

    def process(self, stream):
        print("Start processing")
        self.isRunning = True
        
        language_code = 'de-DE'  # a BCP-47 language tag

        client = speech.SpeechClient()
        config = types.cloud_speech_pb2.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=language_code)
        streaming_config = types.cloud_speech_pb2.StreamingRecognitionConfig(
            config=config,
            interim_results=True)

        requests = (types.cloud_speech_pb2.StreamingRecognizeRequest(audio_content=content)
                    for content in stream)

        return client.streaming_recognize(streaming_config, requests)
