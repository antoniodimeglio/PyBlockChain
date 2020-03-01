from uuid import uuid4
from Utils import Security

class Node(): #template that is used to save all the other nodes to connect to
    def __init__(self, hostname, publicKey, id=None):
        self.hostname = hostname
        self.id = id or uuid4()
        self.publicKey = publicKey
        
