from Crypto.Cipher import AES
from Crypto import Random

class AES_CBC:
    """
    AES encryptor and decryptor using CBC mode
    """

    def __init__( self, key ):
        """
        Constructor. The key should be hex encode
        """
        self.key = key.decode("hex")

    def encrypt( self, raw, block_size = 16 ):
        """
        Returns hex encoded encrypted value
        """
        pad = lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size) 
        raw = pad(raw)
        iv = Random.new().read(AES.block_size);
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return ( iv + cipher.encrypt( raw ) ).encode("hex")

    def decrypt( self, enc, block_size = 16 ):
        """
        Requires hex encoded param to decrypt
        """
        unpad = lambda s : s[0:-ord(s[-1])]
        enc = enc.decode("hex")
        iv = enc[:block_size]
        enc= enc[block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc))


