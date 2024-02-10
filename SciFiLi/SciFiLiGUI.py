from tkinter import *
from binaryTree import binaryTree
from BookClass import Book
from binNode import binNode
from LinkedList import LinkedList
from Node import Node

root = Tk()

Check = Frame(root)
Search = Frame (root)

root.title("SciFiLi")
root.geometry("900x600")
root.config(bg = "white")

def open_win():
   new = Toplevel(root)
   new.geometry("750x250")
   new.title("Check IN/OUT")
   entry = Entry(root, width = 40)
   entry.grid (row = 1, column = 0, padx = 0, pady = 0)
   entry.config (bg ="white")
   


l = Label(root, text = "Welcome to the world's best SciFiLi! Here you can check out books, check in books, and search for books. Happy reading!")
l.grid(row=1, column=0, padx=0, pady=0)
l.config(bg = "light blue", font =("Courier", 12))

b1 = Button(root, text = "Check in or out", font = "Courier", command = open_win)
b1.grid (row = 0, column = 0, padx=0, pady=0)




root.mainloop()