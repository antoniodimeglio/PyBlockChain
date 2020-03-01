from time import time

class Block():
    def __init__(self, prevHash):
        self._prevHash = prevHash
        self._merkleRoot = 0
        self._timestamp = round(time())
        self.nonce = 0
        self.transactions = []


    @property
    def prevHash(self):
        return self._prevHash

    @property
    def merkleRoot(self):
        return self._merkleRoot

    @property
    def timestamp(self):
        return self._timestamp
    

