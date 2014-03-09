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

def gcd(a, b):
    '''
    greatest common divisor of a, b.
    '''
    while b != 0:
        (a, b) = (b, a%b)
    return a

def egcd(a, b):
    """
   Ttake positive integers a, b as input, 
    and return a triple (g, x, y), such that ax + by = g = gcd(a, b).
    """
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y
