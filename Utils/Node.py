from uuid import uuid4
from Security import createStoreKeys

class Node(): #template that is used to save all the other nodes to connect to
    def __init__(self, hostname, publicKey=None, id=None):
        self.hostname = hostname
        self.id = id or uuid4()
        keys = createStoreKeys()
        self.publicKey = publicKey or keys[1]
        self.privateKey = keys[0]
        
        
