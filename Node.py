from flask import Flask
from os import path
from uuid import uuid4
from requests import get #used to get the public ip address
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import json
import socket

#TODO: save both public and private keys locally along with the id

class Node(): #template that is used to save all the other nodes to connect to
    def __init__(self, hostname, publicKey, id=None):
        self.hostname = hostname
        self.id = id or uuid4()
        self.publicKey = publicKey

def createStorePK(): #function that generates both a private and a public key
    privateKey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    publicKey = privateKey.public_key()

    return (privateKey, publicKey)

keys = createStorePK() 
privateKey = keys[0] #private Key of the current node
publicKey = keys[1] #public Key of the current node
currentNode = Node(socket.gethostname(), uuid4()) #the current node
nodes = [] #list of all known nodes







if (path.exists("nodes.json")): #loads new nodes to communicate with
    with open("nodes.json") as file:
        temp = json.loads(file) #json file containing all known nodes
        for node in temp:
            nodes.append(Node(node['hostname'], node['id']))

nodes.append(currentNode) #adding this node to the list of nodes

#Creating our new node
app = Flask(__name__)

@app.route('/getnodes') #returns all nodes saved locally
def getNodes():
    return json.dumps([ob.__dict__ for ob in nodes])

@app.route('/blockchain') #returns blockchain
def getBlockchain():
    pass



print("{} \n {}".format(keys[0].__str__(), keys[1].__str__()))
