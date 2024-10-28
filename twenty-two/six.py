import numpy as np
import re

'''
Day 6: Tuning Trouble
The Elves communicate with radios. To lock on to these, the radio must detect a "start-of-packet marker"
in the datastream; this is a sequence of four characters that are all different.

We just need to report the first character where a marker appears.

'''
def find_marker(length):
    """
    Finds the character position for the contiguous unique sequence of length "length"
    """
    with open('data/six.txt') as f:
        signal = f.read()
        marker = []
        input_index = 0
        while len(marker) == 0:
            duplicate_index = index_unique(signal[input_index:input_index+length])
            if len(duplicate_index) != 0:
                input_index += duplicate_index[0]+1
            else:
                marker.append(input_index+length)
    return marker

def index_unique(input):
    """
    Returns list of indexes of repeated characters in a four letter span
    If unique, doesn't return anything
    """
    unique_chars = []
    duplicate_index = []
    for char in input:
        if char in unique_chars:
            duplicates = [i for i in range(len(input)) if input[i] == char]
            duplicate_index.extend(duplicates)
        else:
            unique_chars.append(char)
    return duplicate_index

print(find_marker(14))
