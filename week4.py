from utils import strxor
import urllib2
import sys

def Question1():
    old_cipher = "20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d "
    old = "Pay Bob 100$    "
    new = "Pay Bob 500$    "
    iv =  old_cipher[:16]
    new_iv = strxor(strxor(iv, old), new)
    new_cipher = "%s%s"%(new_iv, old_cipher[16:])
    print new_cipher


TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

if __name__ == "__main__":
    po = PaddingOracle()
    po.query(sys.argv[1])       # Issue HTTP query with the given argument

def main():
    pass