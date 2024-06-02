class Node(object):

    def __init__(self,data):
        self.data=data
        self.height=0
        self.left=None
        self.right=None

class AVL(object):

    def __init__(self):
        self.root=None

    def calcheight(self,node):

        if not node:
            return -1

        return node.height

    def calcbalance(self,node):

        if not node:
            return 0

        return self.calcheight(node.left)-self.calcheight(node.right)

    def rotateRight(self,node):

        y=node.left
        z=y.right

        y.right=node
        node.left=z

        node.height=max(self.calcheight(node.left),self.calcheight(node.right))+1
        y.height=max(self.calcheight(y.left),self.calcheight(y.right))+1

        return y

    def rotateLeft(self,node):

        y=node.right
        z=y.left

        y.left=node
        node.right=z

        node.height=max(self.calcheight(node.left),self.calcheight(node.right))+1
        y.height=max(self.calcheight(y.left),self.calcheight(y.right))+1

        return y

    def settleViolation(self, node, data):

        balance=self.calcbalance(node)

        if balance>1 and data[1]< node.left.data[1]:
            return self.rotateRight(node)

        if balance<-1 and data[1]>node.right.data[1]:
            return self.rotateLeft(node)

        if balance>1 and data[1]>node.left.data[1]:
            node.left=self.rotateLeft(node.left)
            return self.rotateRight(node)

        if balance<-1 and data[1]<node.right.data[1]:
            node.right=self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    def insert(self,data):
        self.root=self.insertNode(self.root,data)

    def insertNode(self,node,data):

        if not node:
            return Node(data)

        if data[1]< node.data[1]:
            node.left=self.insertNode(node.left,data)
        else:
            node.right=self.insertNode(node.right,data)

        node.height=max(self.calcheight(node.left),self.calcheight(node.right))+1

        return self.settleViolation(node,data)

    def printdata(self):
        self.inorder(self.root)

    def inorder(self,node):

        if not node:
            return

        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def canBeInserted(self,data):

        return self.search(self.root,data)

    def search(self,node,data):

        if not node:
            return True
        if (data[1]+data[3]>=node.data[1]-node.data[2] and data[1]-data[2]<=node.data[1]+node.data[3]):
            return False
        if data[1]<node.data[1]:
            return self.search(node.left,data)
        return self.search(node.right,data)




