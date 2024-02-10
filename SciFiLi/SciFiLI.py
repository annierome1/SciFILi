#SciFiLi
#CSC 201
#A.Rome
#Program that uses BinaryTree, LinkedList, and Priority Queue to create a book library based off of books from a txt file

#BinaryTree was used to search for a book title, find book to be checked in/out, and find books by a certain author. Binary Search trees are a fast way to search for data, especially larger data sets which is why it was used
#LinkedList was used to store books that contained author being searched for. Books were appended to the LinkedList and the LinkedList was returned. LL was used as it is an easy way to store data and link data together.
#Priority Queue was used to sort through the data and return the books in order of highest priority(1) to lowest priority(108). PQs are great ways to sort hierarchal data.

from binaryTree import binaryTree
from BookClass import Book
from binNode import binNode
from LinkedList import LinkedList
from Node import Node

#Searches for book title using binary search tree        
def findTitle():
    x = input("What book are you looking for?")
    result = bst.search(Book(x))
    print(result)
    if result == None:
        print("Sorry, we do not have this book")
    else:
        print("Book found: {}".format(Book(x)))

#Searches by author by appending book by searched author to a LinkedList and returning that LL      
def findAuthor():
    a = input("What author are you looking for?")
    books = bst.findAuthor(a)
    print(books)


#Check in book by searching in bst and changing bool status   
def checkIN():
    ci = input("What book would you like to check in?")
    resl = bst.search(Book(ci))
    if resl == None:
        print("Sorry, we do not have this book")
        return
    resl.data.status == 1
    print("{} is checked in".format(ci))
    return

#Check out book by searching in bst and changing bool if book is checked in 
def checkOut():
    co = input("What book would you like to check out?")
    resu = bst.search(Book(co))
    if resu.data.status == 1:
        resu.data.status == 0
        print("{} has been checked out".format(co))
        return
    else:
        print("{} is already checked out")
        return 
# Priority Queue implementation on BST by priority. 1 = highest priority  
def fire(): 
    q = bst.PQ()
    print(q)


    
    
    
    
    
#Binary Tree implementation
#Books.txt read into Binary Search Tree
bst = binaryTree()
f = open("Books.txt")
for line in f:
    line = line.rstrip("\n")
    info = line.split(", ")
    b = Book(info[0], info[1], info[2], int(info[3]))
    bst.insert(binNode(b))
    


#Main program Menu
    
print("Welcome to the world's best SciFiLi")
done = False
while done == False:
    y = input("Press 1 to search for a book and press 2 to check in a book, 3 to check out a book, and press 4 to exit")
    if y == '1':
        z = input("Press 1 to seach by title and 2 to search by author")
        if z == '1':
            findTitle()
        elif z =='2':
            findAuthor()
    elif y == '2':
        checkIN()
    elif y == '3':
        checkOut()
    elif y == '4':
        print("Thank you for visiting the world's greatest library, I have printed all of our books alphabetically to a file for your future reference.")
        print("Oh no! There has been a fire, I have saved the highest priority books first that are checked in! Here they are:")
       
       #prints inorder traversal of binary tree to a file named "fire.txt"        
        bst.ptraverseInOrder()
        fire()
        break
