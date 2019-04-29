"""
NOTEPADAI
(Processor)

Transcripts a stream of audio in a stream of transcripts
"""

import pyaudio

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
        self.pa = pyaudio.PyAudio()

    def process(self, audio):
        print("Start processing")

        stream = self.pa.open(format=self.pa.get_format_from_width(width=2), channels=1, rate=RATE, output=True)

        for content in audio:
            print(content)
            stream.write(content)
            yield '.'

        stream.stop_stream()
        stream.close()

        yield "End"

