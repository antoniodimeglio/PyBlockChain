#This module defines the Simple Node Lookup Protocol (SNLP).
from Node import Node
from os import path
from uuid import uuid4
from utils import createStoreKeys
import json

        
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


def getNodes():
    return nodes

