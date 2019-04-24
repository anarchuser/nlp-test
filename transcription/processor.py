#!/usr/bin/env python3

"""
NOTEPADAI
(Processor)

Provides tools to transcript an audio stream
"""

from __future__ import division
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

import os
import fnmatch

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


# From StackOverflow (https://stackoverflow.com/questions/1724693/find-a-file-in-python)
def findJSON(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return os.path.join(root, name)


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = findJSON("hypnote*.json", "../")
print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])


class Processor:
    def __init__(self, lang="de_DE"):
        self.lang = lang

    def process(self, stream):
        print("Start processing")

        language_code = self.lang

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

        for response in client.streaming_recognize(streaming_config, requests):
            if not response.results:
                continue

            result = response.results[0]
            if not result.alternatives:
                continue

            if not result.is_final:
                continue

            yield result.alternatives[0].transcript

