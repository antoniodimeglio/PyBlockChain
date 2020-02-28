from hashlib import sha512
from Transaction import Transaction
import json
from time import time

class Block:
    def __init__(self, index, data, prevHash, nonce, target):
        self.index = index #block index
        self.timestamp = round(time()) #time expressed in Unix time
        self.data = data #data that is going to be stored in the blockchain
        self.prevHash = prevHash #hash of the previous block
        self.nonce = nonce #number that needs to be found
        self.target = target #target of zeros to reach
        self.currHash = sha512(json.dumps(self.__dict__, separators=(',', ':')) \
        .encode("utf-8")).hexdigest()
        self.ledger = []
    
    def newTransaction(self, recipient, amount, sign):
        t = Transaction(sender, recipient, amount, sign)
        self.ledger.append(t)
        return self

    def validateSign(self, block, sign):
        pass

    

        
    