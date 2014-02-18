import unittest
import os, binascii
import utils

class TestUtils(unittest.TestCase):
    
    def test_strxor(self):
       for i in range(10):
         a = os.urandom(16)
         b = os.urandom(16)
         res = utils.strxor(a, b)
         res1 = utils.strxor(res, a)
         res2 = utils.strxor(res, b)
         self.assertEquals(res1,b)
         self.assertEquals(res2,a)

if __name__ == '__main__':
    unittest.main()
