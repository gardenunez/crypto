import math, re
from operator import xor
from string import atoi, hexdigits

def strxor(a, b):     
    """
    XOR two strings of different lengths
    """
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def strsplit(seq, lenght):
     """ 
     Split sequence into sub-sets of lenght elements
     """
     return [seq[i:i+lenght] for i in range(0, len(seq), lenght)]
