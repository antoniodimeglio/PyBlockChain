from time import time
from Utils.security import hashBlock

class Block():
    def __init__(self, prevHash):
        self._prevHash = prevHash
        self._merkleRoot = 0
        self._timestamp = round(time())
        self.nonce = 0
        self.transactions = []
        self._currentHash = hashBlock(str(self.__dict__).encode('utf-8'))


    @property
    def prevHash(self):
        return self._prevHash

    @property
    def merkleRoot(self):
        return self._merkleRoot

    @property
    def timestamp(self):
        return self._timestamp
    
    @property
    def currentHash(self):
        return self._currentHash

b = Block('a')
