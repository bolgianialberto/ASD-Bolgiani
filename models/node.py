import math

class Node:
    def __init__(self, vertex, time, parent, f, h, g = math.inf):
        self.vertex = vertex
        self.time = time

        self.parent = parent
        self.f = f
        self.h = h
        self.g = g
    
    def set_f(self, f):
        self.f = f

    def set_h(self, h):
        self.h = h
    
    def get_h(self):
        return self.h

    def set_g(self, g):
        self.g = g
    
    def get_g(self):
        return self.g
    
    def set_parent(self, parent):
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

    def __str__(self):
        return "Node: " + self.vertex + " Time: " + str(self.time) + " F: " + str(self.f) + " H: " + str(self.h) + " G: " + str(self.g) + " Parent: " + str(self.parent)
