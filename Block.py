from hashlib import sha512
from time import time

class Block:
    def __init__(self, index, data, prevHash, nonce, target):
        self.index = index #block index
        self.timestamp = time().__round__() #time expressed in Unix time
        self.data = data #data that is going to be stored in the blockchain
        self.prevHash = prevHash #hash of the previous block
        self.nonce = nonce #number that needs to be found
        self.target = target #target of zeros to reach
        self.currHash = sha512(str(self.__dict__).encode()).digest()
    