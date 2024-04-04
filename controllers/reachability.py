from collections import deque

def check_reachability(islands, initial, goal):
    for island in islands:
            if (initial in island and goal not in island) or (initial not in island and goal in island):
                return False
    return True

def find_islands(graph, grid):
    linked_vertexes = graph.get_linked_vertexes()
    rows = grid.get_rows()
    cols = grid.get_cols()
    grid_representation = create_grid_representation(grid)

    visited = set()
    islands = []
    for r in range(rows):
        for c in range(cols):
            if grid_representation[r][c] == "." and (r, c) not in visited:
                island = set()
                queue = deque([(r, c)])
                while queue:
                    node_r, node_c = queue.popleft()
                    if (node_r, node_c) in visited:
                        continue
                    visited.add((node_r, node_c))
                    island.add((node_r, node_c))
                    for neighbor in linked_vertexes[(node_r, node_c)]:
                        queue.append(neighbor[0])
                islands.append(island)
    return islands

def create_grid_representation(grid):
    rows = grid.get_rows()
    cols = grid.get_cols()
    obstacles = grid.get_obstacles()

    grid_representation = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i, j) in obstacles:
                row.append("X")
            else:
                row.append(".")
        grid_representation.append(row)

    return grid_representation
