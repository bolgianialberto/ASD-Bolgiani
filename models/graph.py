from collections import defaultdict


class Graph:
    def __init__(self):
        self.linked_vertexes = defaultdict(list)

    def add_linked_vertex(self, vertex, neighbor, weight):
        self.linked_vertexes[vertex].append((neighbor, weight))
    
    def get_linked_vertexes(self):
        return self.linked_vertexes
    
    def get_neighbors(self, vertex):
        return self.linked_vertexes[vertex]
    
    def __str__(self):
        res = "Graph\n"
        for vertex in self.linked_vertexes:
            res += str(vertex) + " -> " + str(self.linked_vertexes[vertex]) + "\n"
        return res
    