"""
List of functions used by several packages
"""

#from generated import audioStream_pb2
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


# TODO:
# Function to split a sentence into its phonetic spelling
# @in:  string
# @out: stream(string)
def split_spellings(sentence):
    word_array = tokenize.word_tokenize(sentence)
    phonems = []
    for word in range(len(word_array)):
        if word_array[word].isdigit():
            small_counter = 0
            numword = inflect_engine.number_to_words(word_array[word])
            del word_array[word]
            numword = numword.replace(",", "")
            numword = numword.replace("-", " ")
            if " " in numword:
                no = numword.split(" ")
                insert_list_list(word_array, no, word)
        phonem = pronouncing.phones_for_word(word_array[word])[0]
        phonems.append(phonem)
        #print(phonem)
        #yield phonem
    print(word_array)
    print(phonems)
    #yield phonems

#inserts all items of list2 into list1 at index - basically combines 'insert' with 'extend'
def insert_list_list(list1, list2, index_list1=0):
    for i in range(len(list2)):
        index0 = int(index_list1 + i)
        list1.insert(index0, list2[i])
    return list1

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

split_spellings("This is a very beautiful day amongst the 365 days of the year")