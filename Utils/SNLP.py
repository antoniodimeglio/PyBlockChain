#This module defines the Simple Node Lookup Protocol (SNLP).
#This is not an actual protocol, I just wanted it to sound fancy.
import os
import inspect
import sys
from uuid import uuid4
from security import createStoreKeys
import requests
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import Node


nodes = []
jsonNodes = ""

def localNodesLookup(): #looks for locally saved nodes and loads them 
    if (path.exists("nodes.json")): #loads nodes to communicate with
        with open("nodes.json") as fileStream:
            file = ""
            for l in fileStream:
                file += l

        jsonNodes = json.loads(file) #json file containing all saved nodes

        for node in jsonNodes:
            nodes.append(Node(node['hostname'], node['id'], node['publickey']))

          
    return nodes


def addNode(newNode):
    nodes.append(newNode)
    jsonNodes.append({'hostname':newNode.hostname, 'id':newNode.id, 'publickey':newNode.publicKey})


def lookUpNodes():
    if (localNodesLookup() == []):
        jsonNodes = requests.get('https://api.antoniodimeglio.io/defaultNodes').json() #as of right now this site doesn't exists.
        defaultNodes = json.load(jsonNodes)
        for node in defaultNodes:
            nodes.append(Node(node['hostname'], node['publicKey'], node['id']))
    
    return nodes



