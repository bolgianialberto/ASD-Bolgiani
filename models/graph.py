class Graph:
    def __init__(self, vertexes, linked_vertexes):
        self.vertexes = vertexes
        self.linked_vertexes = linked_vertexes

    def get_vertexes(self):
        return self.vertexes
    
    def get_linked_vertexes(self):
        return self.linked_vertexes
    
    def get_neighbors(self, vertex):
        return self.linked_vertexes[vertex]
    
    def __str__(self):
        res = "Graph\n"
        for vertex in self.vertexes:
            res += "(" + str(vertex[0]) + ", " + str(vertex[1]) + ")" + " " + str(self.linked_vertexes[vertex]) + "\n"
        
        return res