from math import sqrt
from models.graph import Graph
from models.path import Path

nsew_directions = Path.get_nsew_moves()
diagonal_directions = Path.get_diagonal_moves()
still_direction = Path.get_still_move()
nsew_still_weight = Path.get_nsew_still_weight()
diagonal_weight = Path.get_diagonal_weight()

def graph_generator(grid):
    graph = Graph()

    add_linked_vertexes(graph, grid)

    return graph

def add_linked_vertexes(graph, grid):
    rows = grid.rows
    cols = grid.cols

    for r in range(rows):
        for c in range(cols):
            if grid.is_free(r, c):
                for direction in nsew_directions + diagonal_directions + still_direction:
                    new_vertex = (r + direction[0], c + direction[1])
                    if 0 <= new_vertex[0] < rows and 0 <= new_vertex[1] < cols:
                        if grid.is_free(new_vertex[0], new_vertex[1]):
                            graph.add_linked_vertex((r, c), new_vertex, get_weight(direction))

def get_weight(direction):
    if direction in nsew_directions:
        return nsew_still_weight
    else:
        return diagonal_weight
                
                