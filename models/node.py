import math

class Node:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time

        self.parent = None
        self.f = 0
        self.h = 0
        self.g = math.inf
    
    def set_f(self, f):
        self.f = f

    def set_h(self, h):
        self.h = h

    def set_g(self, g):
        self.g = g
    
    def get_g(self):
        return self.g
    
    def set_parent(self, parent):
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f
