from Crypto.Cipher import AES
from Crypto import Random
from utils import strxor, strsplit

class IVCounter(object):
    '''
    AES CTR Counter.  
    '''

    def __init__(self, value):
        self.value = value

    def increment(self):
        '''Add counter value to IV'''
        newIV = hex(int(self.value.encode('hex'), 16) + 1)

        # Delete the negligible part of the string
        self.value = newIV[2:len(newIV) - 1].decode('hex') 
        return self.value

    def __repr__(self):
        self.increment()
        return self.value

    def string(self):
        return self.value

class AES_CTR:
    """AES encryptor and decryptor using CTR mode """
    
    def __init__(self, k):
        self.key = k.decode('hex')

    def __AESencryptor(self, cipher):
        encryptor = AES.new(self.key, AES.MODE_ECB)
        return encryptor.encrypt(cipher)

    def encrypt(self, raw):
        """Returns hex encoded encrypted value"""
        blocks = strsplit(raw, 16)

        # Takes the initiator vector
        iv = Random.new().read(16)
        self.IV = IVCounter(iv)

        # Message block 
        msg = [iv]

        # Decrypt
        for b in blocks:
            aes = self.__AESencryptor(self.IV.string())
            msg.append(strxor(b, aes))
            self.IV.increment()
        
        return ''.join(msg).encode('hex')

    def decrypt(self, cipher):
        """Returns the decrypted plaintext.
        Requires hex encoded param to decrypt """
        # Split the CT into blocks of 16 bytes
        blocks = strsplit(cipher.decode('hex'), 16)

        # Takes the initiator vector
        self.IV = IVCounter(blocks[0])
        blocks.remove(blocks[0])    

        # Message block 
        msg = []

        # Decrypt
        for b in blocks:
            aes = self.__AESencryptor(self.IV.string())
            msg.append(strxor(b, aes))
            self.IV.increment()

        return ''.join(msg)
