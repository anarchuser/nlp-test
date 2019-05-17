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


# Function to split a sentence into its phonetic spelling
# @in:  string
# @out: stream(string)
def split_spellings(sentence, full_pronounciation_output=False):
    word_array = tokenize.WhitespaceTokenizer().tokenize(sentence)
    print(word_array)
    for word in word_array:
        word = string_cleaner(word)
        if word == "":
            continue
        if word.isdigit():
            numword = inflect_engine.number_to_words(word)
            numword = string_cleaner(numword)
            print(numword)
            if " " in numword:
                numword = numword.split(" ")
            for element in numword:
                output = pronouncing.phones_for_word(element)[0]
                if not full_pronounciation_output:
                    yield output[0]
                else:
                    yield output
        else:
            output = pronouncing.phones_for_word(word)[0]
            if not full_pronounciation_output:
                yield output[0]
            else:
                yield output


zero_back = (",", ".", ";", "!", "?", "\"")
one_back = ("_", "-")
def string_cleaner(words):
    words.replace(zero_back, "")
    words.replace(one_back, " ")
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
