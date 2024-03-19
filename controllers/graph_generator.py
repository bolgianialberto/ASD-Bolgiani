from math import sqrt
from models.graph import Graph
from models.path import Path

def graph_generator(grid):
    # Define all vertexes
    all_vertexes = [(i, j) for i in range(grid.rows) for j in range(grid.cols) if (i, j) not in grid.obstacles]
    
    # Compute all arcs
    arcs = create_arcs(all_vertexes)

    # Compute linked vertexes
    linked_vertexes = create_linked_vertexes(all_vertexes, arcs)

    # Create a graph
    graph = Graph(all_vertexes, linked_vertexes)

    return graph

def create_arcs(all_vertexes):
    arcs = []

    nsew_directions = Path.get_nsew_moves()
    diagonal_directions = Path.get_diagonal_moves()
    still_direction = Path.get_still_move()
    nsew_still_weight = Path.get_nsew_still_weight()
    diagonal_weight = Path.get_diagonal_weight()
    
    for vertex in all_vertexes:
        for direction in nsew_directions + diagonal_directions + still_direction:
            new_vertex = (vertex[0] + direction[0], vertex[1] + direction[1])
            if new_vertex in all_vertexes:
                    arcs.append((vertex, new_vertex, diagonal_weight if direction in diagonal_directions else nsew_still_weight))
    
    return arcs

def create_linked_vertexes(all_vertexes, arcs):
    linked_vertexes = {}

    for vertex in all_vertexes:
        linked_vertexes[vertex] = []

        for arc in arcs:
            if vertex == arc[0]:
                couple = []
                couple.append(arc[1])
                couple.append(arc[2])
                linked_vertexes[vertex].append(couple)
        
    return linked_vertexes