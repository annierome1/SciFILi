class Book:
    def __init__(self, title = " ", author = " ", status = False, priority = 0):
        self._title = str(title)
        self._author = str(author)
        self._status = bool(status)
        self._priority = int(priority)
        
        
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title 
        
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        self._authour = author
        
    @property
    def status(self):
        return self._status
    @status.setter
    def status (self, status):
        self._status = status
        
    @property
    def priority(self):
        return self._priority
    @priority.setter
    def priority(self, priority):
        self._priority = priority
        
    def checked(self):
        if self._status == 0:
            return 'checked out'
        elif self._status == 1:
            return 'checked in'
        else:
            return 'fuck'
        
    def __eq__(self, other):
        return (self._title == other.title)
    
    def __gt__(self, other):
        return (self._title > other.title)
    
    
    def __lt__(self, other):
        return (self._title < other.title)
          
    
    def gtPriority(self, other):
        return self.priority > other.priority
   
    def ltPriority(self, other):
        return self.priority < other.priority 
    
    
    
    
    def __str__(self):
        c = self.checked()
        return ("{}, {}, {}, priority = {} \n").format(self._title, self._author, c, self._priority)
    

    
