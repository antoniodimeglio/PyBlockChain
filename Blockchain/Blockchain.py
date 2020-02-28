#https://medium.com/technology-nineleaps/how-to-create-blockchain-from-the-scratch-ce9e01436881

from Block import Block

class Blockchain:
    def __init__(self):
        b = Block(0, "Genesis Block", "0", "Default Nonce", 8)
        self.blocks = [b, ]

    def __lastBlock(self):
        last = len(self.blocks) - 1
        return (last, self.blocks[last].currHash)

    def addBlock(self, data, nonce, target):
        lastBlock = self.__lastBlock()
        b = Block(lastBlock[0], data, lastBlock[1], nonce, target)
        self.blocks.append(b)

    def getAllBlocks(self):
        x = []
        for b in self.blocks:
            x.append(b.__dict__)
        return x
    
    def onTransaction(self, sender, receiver, amount, sign):
        sender.newTransaction(receiver.node, amount, sign)


    def checkValidity(self):
        pass






bc = Blockchain()
bc.addBlock("Second block", "Random nonce 2", 8)

print(bc.getAllBlocks())


