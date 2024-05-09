from collections import deque

# TODO costa O(1) cercare nel set giusto?
def check_reachability(islands, initial, goal):
    for island in islands:
            if (initial in island and goal not in island) or (initial not in island and goal in island):
                return False
    return True

def find_islands(graph, grid):
    linked_vertexes = graph.get_linked_vertexes()
    rows = grid.get_rows()
    cols = grid.get_cols()

    visited = set()
    islands = []
    for r in range(rows):
        for c in range(cols):
            if grid.is_free(r, c) and (r, c) not in visited:
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