import random 
class stack:
    def __init__(self, Capacity = 1 ):
        self.top = -1
        self.Capacity = Capacity
        self.A= [None]*Capacity
        