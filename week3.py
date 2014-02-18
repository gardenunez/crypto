"""
Problem Set, week 3
"""
import os
from Crypto import Random
from Crypto.Cipher import AES
from utils import strxor


def AES_Enc(k, m):
  return AES.new(k, AES.MODE_ECB).encrypt(m)

def AES_Dec(k, c):
  return AES.new(k, AES.MODE_ECB).decrypt(c)

def function_one(x, y):
  return strxor(AES_Enc(y, x), y)

def function_two(x, y):
  return strxor(AES_Enc(x, x), y)


def FindOne(x1, y1, y2):
    e = AES_Enc(y1, x1)
    or1 = strxor(e, y1)
    or2 = strxor(or1, y2)
    d = AES_Dec(y2, or2)
    return d

def FindTwo(x1, y1, x2):
    e = AES_Enc(x1, x1)
    or1 = strxor(e, y1)
    or2 = strxor(or1, AES_Enc(x2,x2))
    return or2


def DoOne():
    rnd = Random.new()
    x1 = rnd.read(16)
    y1 = rnd.read(16)
    y2 = rnd.read(16)
    f1 = function_one(x1, y1)
    x2 = FindOne(x1, y1, y2)
    f2 = function_one(x2, y2)
    print "F1: %r" % (f1 == f2)
    print "x1: %s" % x1.encode("hex")
    print "y1: %s" % y1.encode("hex")
    print "f1: %s" % f1.encode("hex")
    print "x2: %s" % x2.encode("hex")
    print "y2: %s" % y2.encode("hex")
    print "f2: %s" % f2.encode("hex")


def DoTwo():
    rnd = Random.new()
    x1 = rnd.read(16)
    y1 = rnd.read(16)
    x2 = rnd.read(16)
    f1 = function_two(x1, y1)
    y2 = FindTwo(x1, y1, x2)
    f2 = function_two(x2, y2)
    print "F2: %r" % (f1 == f2)
    print "x1: %s" % x1.encode("hex")
    print "y1: %s" % y1.encode("hex")
    print "f1: %s" % f1.encode("hex")
    print "x2: %s" % x2.encode("hex")
    print "y2: %s" % y2.encode("hex")
    print "f2: %s" % f2.encode("hex")

def main():
    DoOne()
    print 80*'-'
    DoTwo()

if __name__ == '__main__':
    main()