import unittest, os
from AES_CBC import AES_CBC
from AES_CTR import AES_CTR

class Test_AES(unittest.TestCase):
    def setUp(self):
        self.msgs = ['Basic CBC mode encryption needs padding.',
                     'Our implementation uses rand. IV',
                     'CTR mode lets you build a stream cipher from a block cipher.',
                     'Always avoid the two time pad!']
    def test_AES_CTR(self):
        key = os.urandom(16).encode('hex')
        decryptor = AES_CTR(key)
        for m in self.msgs:
            self.assertEqual(decryptor.decrypt(decryptor.encrypt(m)), m)

    def test_AES_CBC(self):
        key = os.urandom(16).encode('hex')
        decryptor = AES_CBC(key)
        for m in self.msgs:
            self.assertEqual(decryptor.decrypt(decryptor.encrypt(m)), m)


if __name__ == '__main__':
    unittest.main()
