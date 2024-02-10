class Node:
    def __init__(self, data=None, nextNode=None):
        self._data = data
        self._link = nextNode
        
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value
        
    @property
    def link(self):
        return self._link
    @link.setter
    def link(self, value):
        self._link = value
    def __str__(self):
        return str(self._data)
