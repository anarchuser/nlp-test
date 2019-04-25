"""
NOTEPADAI
(Processor)

Transcripts a stream of audio in a stream of transcripts
"""

import google
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

import os
import fnmatch

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


# Adopted from StackOverflow (https://stackoverflow.com/questions/1724693/find-a-file-in-python)
# Recursively looks through local files looking for something that looks like a credentials file
# (Returning the first occurrence)
def findJSON(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return os.path.join(root, name)


# Set a environment variable pointing at the location of the credentials file (hypnote*.json)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = findJSON("hypnote*.json", "../")
print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])


class Processor:
    def __init__(self, lang="de_DE", send_interim_results=False):
        self.lang = lang
        self.interim = send_interim_results

    def process(self, stream):
        print("Start processing")

        language_code = self.lang

        # Configure connection to gcloud server
        client = speech.SpeechClient()
        config = types.cloud_speech_pb2.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=language_code)
        streaming_config = types.cloud_speech_pb2.StreamingRecognitionConfig(
            config=config,
            interim_results=self.interim)

        # Send all samples from the given audio stream to google
        requests = (types.cloud_speech_pb2.StreamingRecognizeRequest(audio_content=content.chunk)
                    for content in stream)

        # Parses the returning objects, filtering out the actual transcript
        # and yielding that (creating the actual response stream)
        try:
            for response in client.streaming_recognize(streaming_config, requests):
                if not response.results:
                    continue

                result = response.results[0]
                if not result.alternatives:
                    continue

                yield result.alternatives[0].transcript
        except google.api_core.exceptions.OutOfRange:
            return self.process(stream)

