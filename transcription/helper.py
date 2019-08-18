"""
List of functions used by several packages
"""

from generated import audioStream_pb2
from nltk import tokenize

import librosa
import numpy as np
import pronouncing
import inflect

CHUNK = 320

PUNCTUATION = (",", ".", ";", "!", "?", "\"")
DASHES = ("_", "-", "/")

inflect_engine = inflect.engine()


# Maps a stream of gRPC samples to a stream of actual audio samples
# @in:  stream(Samples)
# @out: stream(list(int))
def sample_to_audio(samples):
    for sample in samples:
        yield sample.chunk


# Returns a Response containing a given word as message
# @in:  String
# @out: Response
def string_to_response(word):
    response = audioStream_pb2.Response()
    response.word = word
    return response


# Turns a stream of samples into a librosa usable stream
def stream_to_librosa(stream):
    for samples in stream:
        yield arr_to_librosa(samples)


# Turns a list of samples into a librosa-usable array
# @in:  list(int)
# @out: np_array
def arr_to_librosa(arr):
    samples = np.array(arr)
    return librosa.util.buf_to_float(samples)


# Converts an audio file (an array of samples) into a stream with arrays of size chunk
# @in:  list(int), OPT int
# @out: stream(list(int))
def audio_to_stream(audio, chunk=CHUNK):
    while True:
        samples = audio[:chunk]
        audio = audio[chunk:]
        yield samples
        if len(audio) is 0:
            break


# Prints out every phoneme in a (sequence of) words
# @in:  string
# @out: NOTHIN'
def print_phonemes(word):
    for phoneme in split_spellings(word):
        print(phoneme)


# Function to split a sentence into its phonetic spelling
# @in:  string
# @out: stream(string)
def split_spellings(sentence, full_pronunciation_output=False):
    word_array = tokenize.WhitespaceTokenizer().tokenize(sentence)
    for word in word_array:
        word = __string_cleaner(word)
        if word == "":
            continue
        if word.isdigit():
            num_word = inflect_engine.number_to_words(word)
            num_word = __string_cleaner(num_word)
            print(num_word)
            if " " in num_word:
                num_word = num_word.split(" ")
            for element in num_word:
                try:
                    yield __pronounce(element, full_pronunciation_output)
                except ValueError:
                    print("{}:\nPronunciation failed for '{}'".format(sentence, element))
        else:
            try:
                yield __pronounce(word, full_pronunciation_output)
            except ValueError:
                print("{}:\nPronunciation failed for '{}'".format(sentence, word))


def __pronounce(word, full_pronunciation_output):
    output = pronouncing.phones_for_word(word)
    if output:
        if full_pronunciation_output:
            return output
        else:
            return output[0]
    else:
        raise ValueError


def __string_cleaner(words):
    for i in range(len(PUNCTUATION)):
        words = words.replace(PUNCTUATION[i], "")
    for i in range(len(DASHES)):
        words = words.replace(DASHES[i], " ")
    return words


# TODO:
# Function to split an audio stream into a phoneme stream
# @in:  stream(librosa_array)
# @out: stream(mfcc)
def split_phonemes(stream):
    pass


# Converts audio streams into mfcc streams (used for plotting)
# @in:  stream(librosa_array)
# @out: stream(mfcc)
def mfcc(stream):
    for samples in stream:
        yield librosa.feature.mfcc(samples)


# Converts an mfcc stream into its derivative (also used for plotting)
# @in:  stream(mfcc)
# @out: stream(mfcc)
def mfcc_d(stream):
    mem = stream.__next__()
    for coefficients in stream:
        yield mem - coefficients
        mem = coefficients
