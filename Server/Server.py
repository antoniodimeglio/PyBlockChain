from flask import Flask
import utils
import json

#Creating our new node
app = Flask(__name__)

@app.route('/getnodes') #returns all nodes saved locally
def getNodes():
    return json.dumps([ob.__dict__ for ob in nodes])

@app.route('/blockchain') #returns blockchain
def getBlockchain():
    pass
