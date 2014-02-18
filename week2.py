"""
Problem Set, week 2.
"""

from AES_CBC import AES_CBC
from AES_CTR import AES_CTR
from utils import strxor
 

l1 = ["5f67abaf", "4af53267", "7b50baab","9f970f4e"]
l2 = ["bbe033c0", "87a40cfa", "ac343a22", "6068f0b1"]

MSGS = ["To consider the resistance of an enciphering process to being broken we should assume that at same times the enemy knows everything but the key being used and to break it needs only discover the key from this information.", 
        'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.',
        'An enciphering-deciphering machine (in general outline) of my invention has been sent to your organization.',
        'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.']

def check_question4(left1, left2):
    for i in range(4):
        print i
        res = strxor(l1[i].decode("hex"), l2[i].decode("hex"))
        if res == '\xff\xff\xff\xff':
            print "found it!!"
        else:
            print res

def check_question5(msgs):
    for m in msgs:
        print len(m), 128 - len(m)

def main():
    ctr_ciphers = ["69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329",      \
                    "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"]
    cbc_ciphers = ["4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81",
                   "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"]
    ctr_key = "36f18357be4dbd77f050515c73fcf9f2"  
    cbc_key = "140b41b22a29beb4061bda66b6747e14"

    #CBC
    decryptor = AES_CBC(cbc_key)
    for c in cbc_ciphers:
        print '%s' % decryptor.decrypt(c)

    #CTR
    decryptor = AES_CTR(ctr_key)
    for c in ctr_ciphers:
        print '%s' % decryptor.decrypt(c)

if __name__ == '__main__':
    main()