from collections import defaultdict

class Graph:
    def __init__(self):
        self.linked_verteces = defaultdict(set)

    def add_linked_vertex(self, vertex, neighbor, weight):
        self.linked_verteces[vertex].add((neighbor, weight))
    
    def get_linked_verteces(self):
        return self.linked_verteces
    
    def get_neighbors(self, vertex):
        return self.linked_verteces[vertex]
    
    def __str__(self):
        res = "Graph\n"
        for vertex in self.linked_verteces:
            res += str(vertex) + " -> " + str(self.linked_verteces[vertex]) + "\n"
        return res
    