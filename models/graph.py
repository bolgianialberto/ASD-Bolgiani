class Graph:
    def __init__(self, vertexes, linked_vertexes):
        self.vertexes = vertexes
        self.linked_vertexes = linked_vertexes

    def print(self):
        print("Graph")
        for vertex in self.vertexes:
            print(vertex, self.linked_vertexes[vertex])

    def get_vertexes(self):
        return self.vertexes
    
    def get_linked_vertexes(self):
        return self.linked_vertexes