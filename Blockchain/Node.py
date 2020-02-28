from flask import Flask
from uuid import uuid4
from Transaction import Transaction
import json

ledgher = []


#Creating a new node
app = Flask(__name__)

nodeId = str(uuid4()).replace('-', '')


print(app)
print(nodeId)


@app.route('/mine', methods=['GET'])
def mine():
    pass

@app.route('/transactions/new', methods=['POST'])
def newTransaction():
    pass

@app.route('/chain', methods=['GET'])
def fullChain():
    pass

if __name__ == "__main__":
    app.run(host='localhost', port=5000)