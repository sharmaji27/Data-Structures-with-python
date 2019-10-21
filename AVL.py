class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        self.height=0

class AVL:
    def __init__(self):
        self.root=None

    def calculateHeight(self,node):
        if not node:
            return -1
        return node.height

    def calcBalance(self,node):
        if not node:
            return 0
        return self.calculateHeight(node.leftchild)-self.calculateHeight(node.rightchild)
    #if it returns >1 then it is left heavy tree
    #if it returns <-1 then it is right heavy tree

    def RightRotate(self,node):
        templeft=node.leftchild
        t=templeft.rightchild
        templeft.rightchild=node
        node.leftchild=t

        node.height=max(self.calculateHeight(node.leftchild),self.calculateHeight(node.rightchild))+1
        templeft.height=max(self.calculateHeight(templeft.leftchild),self.calculateHeight(templeft.rightchild))+1

        return templeft

    def LefttRotate(self, node):
        temprightt = node.rightchild
        t = temprightt.leftchild
        temprightt.leftchild = node
        node.rightchild = t

        node.height = max(self.calculateHeight(node.leftchild), self.calculateHeight(node.rightchild)) + 1
        temprightt.height = max(self.calculateHeight(temprightt.leftchild), self.calculateHeight(temprightt.rightchild)) + 1

        return temprightt

    def insert(self,data):
        self.root=self.insertnode(data,self.root)

    def insertnode(self,data,node):
        if not node:
            return Node(data)

        if data<node.data:
            node.leftchild=self.insertnode(data,node.leftchild)
        else:
            node.rightchild=self.insertnode(data,node.rightchild)

        node.height=max(self.calculateHeight(node.leftchild),self.calculateHeight(node.rightchild))+1

        return self.settleviolations(data,node)

    def settleviolations(self,data,node):
        balance=self.calcBalance(node)

        if balance>1 and data<node.leftchild.data:
            print('left left heavy situation ',node.data)
            return self.RightRotate(node)

        elif balance<-1 and data>node.rightchild.data:
            print('right right heavy situation ',node.data)
            return self.LefttRotate(node)

        elif balance>1 and data>node.leftchild.data:
            print('left right heavy situation ',node.data)
            node.leftchild= self.LefttRotate(node.leftchild)

            return self.RightRotate(node)

        elif balance<-1 and data<node.rightchild.data:
            print('right left heavy situation ',node.data)
            node.rightchild= self.RightRotate(node.rightchild)

            return self.LefttRotate(node)

        return node

    def traverse(self):
        if self.root:
            self.traverseinorder(self.root)

    def traverseinorder(self,node):

        if node.leftchild:
            self.traverseinorder(node.leftchild)

        print(node.data)

        if node.rightchild:
            self.traverseinorder(node.rightchild)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):

        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:

            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return None

            if not node.leftChild:
                print("Removing a node with a right child...")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing a node with a left child...")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with two children...")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return node;  # if the tree had just a single node

        node.height = max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild)) + 1;

        balance = self.calcBalance(node)

        # doubly left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.RightRotate(node)

        # left right case
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.LefttRotate(node.leftChild)
            return self.RightRotate(node)

        # right right case
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.LefttRotate(node)

        # right left case
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.RightRotate(node.rightChild)
            return self.LefttRotate(node)

        return node

    def getPredecessor(self, node):

        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node


myavl=AVL()

myavl.insert(10)
myavl.insert(18)
myavl.insert(15)
myavl.insert(25)
myavl.insert(20)

myavl.remove(15)
myavl.traverse()