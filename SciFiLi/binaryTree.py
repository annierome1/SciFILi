# binary tree code
# TO DO:
#      1. Add a method for deleting (removing) a node no matter where it's located
#      2. Add the other traversal methods (postorder and preorder) using recursion
#      3. Print the tree level by level (feel free to get online/AI help for this one)

from binNode import binNode
from LinkedList import LinkedList
from Node import Node
from QUEUE2_10 import *

class binaryTree:
    def __init__(self, r = None, c = None):
        self._root = r
        self._curr = c
    
    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, n):
        self._root = n
    @property
    def curr(self):
        return self._curr
    @curr.setter
    def curr(self, n):
        self._curr = n
    
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
    
    def isLeaf(self):
        if self.curr.left == None and self.curr.right == None:
            return True
        else:
            return False
    
    def getData(self):
        if self.curr == None:
            return None
        else:
            return self.curr.data
        
    def goRoot(self):
        self.curr = self.root
    
    def goLeft(self):
        self.curr = self.curr.left
    
    def goRight(self):
        self.curr = self.curr.right
        
    def getMin(self):
        self.goRoot()
        while self.curr.left != None:
            self.goLeft()
        return self.getData()

    def getMax(self):
        self.goRoot()
        while self.curr.right != None:
            self.goRight()
        return self.getData()

    # recursive function to insert
    # only used inside binaryTree class!!!
    def insertNode(self, here, n):
        if here == None:
            here = n
        else:
            if n.data < here.data:
                 here.left = self.insertNode(here.left, n)
            else:
                here.right = self.insertNode(here.right, n)
        return here
    
    # inserts a node (n)
    # This is the method you'll call outside of this class
    def insert(self, n):
        if self.isEmpty() == True:
            self.root = n
            self.curr = n
        else:
            self.goRoot()
            self.curr = self.insertNode(self.curr, n)
            
    # does the actual counting
    # again, used only in-class
    def count(self, n):
         if n == None:
             return 0
         else:
             l = 1
             l += self.count(n.left);
             l += self.count(n.right);
             return l
            
    # use this outside of the class
    def getSize(self):
        return self.count(self.root)
    
    # next 2 methods find a node in the tree or returns None if not there
    def findIt(self, n, what):
        if n == None:
            return None # not found
        elif n.data == what:
            return n
        elif what < n.data:
            return self.findIt(n.left, what)
        elif what > n.data:
            return self.findIt(n.right, what)

    def search(self, what):
        self.curr = self.findIt(self.root, what)
        return self.curr
        



    def findParent(self, here, n):
        if here == None:
            return None
        if here.left == n or here.right == n:
            return here
        if n.data < here.data:
            return self.findParent(here.left, n)
        else:
            return self.findParent(here.right, n)
        
    def Parent(self, n):
        if self.root == n:
            return None
        return self.findParent(self.root, n)
     
    #priority queue 
    def doPQ(self, n, q):
        if n != None:
            q.enqueue(Node(n.data))
            q = self.doPQ(n.left, q)
            q = self.doPQ(n.right, q)
        return q
    
    def PQ(self):
        pq = priorityQ()
        self.goRoot()
        q = self.doPQ(self.curr, pq)
        return q
    
    
    def inOrder(self, n):
        if n != None:
            self.inOrder(n.left)
            print(n.data)
            self.inOrder(n.right)
            
        
    
    def traverseInOrder(self):
        self.goRoot()
        self.inOrder(self.curr)
        
#These two functions traverse through a binary search tree and print to a a txt file in alphaebtical order        
    def pinOrder(self, n, file):
        if n is not None:
            self.pinOrder(n.left, file)
            file.write(str(n.data) + '\n')
            self.pinOrder(n.right, file)

    def ptraverseInOrder(self):
        self.goRoot()
        with open('fire.txt', 'w') as file:
            self.pinOrder(self.curr, file)

        
    
        
#These three functions find book with author being searched for and append them to a LL, the LL is then returned containing the books by author at a
    def doAuthor(self, n, a, L):
        if n != None:
            if n.data.author == a:
                L.append(Node(n.data))
            L = self.doAuthor(n.left, a, L)
            L = self.doAuthor(n.right, a, L)
        return L
    
    def findAuthor(self, a):
        L = LinkedList()
        self.goRoot()
        L = self.doAuthor(self.curr, a, L)
        return L
   

    def findA(self, a):
        self.findAuthor(self.curr, a)

    def preOrder(self, n):
        if n!= None:
            print(n.data)
            self.preOrder(n.left)
            self.preOrder(n.right)
            
    def traversePreOrder(self):
        self.goRoot()
        self.preOrder(self.curr)
    
    def postOrder(self, n):
        if n!= None:
            self.postOrder(n.left)
            self.postOrder(n.right)
            print(n.data)
            
    def traversePostOrder(self):
        self.goRoot()
        self.postOrder(self.curr)
        
                
                