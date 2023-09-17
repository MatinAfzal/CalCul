############################################################################
# CalCul Created By Matin Afzal
# https://github.com/MatinAfzal
# contact.matin@yahoo.com
############################################################################

# File identity information
__author__ = 'Matin Afzal (contact.matin@yahoo.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/09/17'

class List:
    def __init__(self, size):
        self.list = []
        self.size = size

    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False

    def is_full(self):
        if len(self.list) == self.size:
            return True
        return False

    def push(self, item):
        if self.is_full() != True:
            self.list.append(item)
            return True
        return False

    def pop(self):
        if self.is_empty() != True:
            temp = self.list.pop()
            return temp

    def clear(self):
        self.list = []