from BookClass import Book
from LinkedList import LinkedList
from Node import Node


class Queue(LinkedList):
    def __init__(self):
        super().__init__()
    
    def enqueue(self, d):
        super().append(d)
        
    def dequeue(self):
        if super().isEmpty():
            return None 
        super().goBeginning() #go beginning for a queue
        x = super().getData()
        super.remove()
        return x
    
    def peek (self):
        super().goBeginning()
        x = super().getData()
        return x

class priorityQ(Queue):
    
    def __init__(self):
        super().__init__()
#https://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/
#adds books to queue and swaps nodes if book is greater than the next book until all books are sorted in reverse order
    def enqueue(self, n):
        if n.data.status == 1:
            if super().isEmpty():
                super().append(n)
            else:
                super().insertBefore(n)
                super().goBeginning()
                temp = super().getHead()
                curr = temp.link
                while curr is not None and temp.data.gtPriority(curr.data):
                    temp.data, curr.data = curr.data, temp.data
                    temp = curr
                    curr = curr.link
        
            



                
            
        
        
        
        
        
    
    
    
        
    