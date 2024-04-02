from models.path import Path
from algorithm.reach_goal import reach_goal
import random
from collections import deque

def initial_paths_generator(graph, grid, initials, goals, goals_last_instant, use_reach_goal = False):
    # paths will contain a list of paths
    paths = set()

    # reachables is a list of couples (init, goal) that are reachable
    reachables = check_reachability(graph, grid, initials, goals)

    # Create n paths
    for initial, goal in reachables:
        path = path_generator(graph, initial, goal, paths, goals_last_instant, use_reach_goal)
        paths.add(path)
    
    Path.set_goal_last_instant(goals_last_instant)
    return paths

def path_generator(graph, init, goal, previous_paths, goals_last_instant, use_reach_goal = False):
    if use_reach_goal:
        path, _, _ = reach_goal(graph, init, goal, previous_paths, goals_last_instant)

    else:
        path = Path(init, goal)
        sequence = random_sequence_generator(graph, path, previous_paths, goals_last_instant)
        path.set_sequence(sequence)

    return path

def random_sequence_generator(graph, path, previous_paths, goals_last_instant):
    sequence = []

    actual_weight = 0

    init = path.get_init()
    goal = path.get_goal()

    sequence.append(init)
    
    current_vertex = init
    instant = 1

    linked_vertexes = graph.get_linked_vertexes()

    # Generate the sequence of moves
    while current_vertex != goal:
        if instant > 10:
            # TODO: sto provando a impostare un nuovo goal se continua a cercare senza trovare
            path.set_goal(current_vertex)
            goals_last_instant[current_vertex] = instant-1
            del goals_last_instant[goal]
            break
        # TODO: Continuo a prendere il migliore anche se non posso? (ostacolo oppure goal irraggiungibile)

        next_vertex, weight = get_next_random_vertex(linked_vertexes, current_vertex)
        
        # If the next_vertex is the goal, I have to check if it is passed by other paths after the last instant
        if next_vertex == goal:
            if goals_last_instant[goal] > instant:
                while next_vertex == goal:
                    next_vertex, weight = get_next_random_vertex(linked_vertexes, current_vertex)

        # Check if there are conflicts
        if check_next_vertex(current_vertex, next_vertex, instant, previous_paths):
            sequence.append(next_vertex)
            current_vertex = next_vertex
            actual_weight += weight

            # If the next vertex is one of the other goal, I have to update the last instant it was crossed
            if current_vertex in goals_last_instant and current_vertex != goal:
                goals_last_instant[current_vertex] = instant
            
            instant += 1
    
    # The real value of instant 
    instant -= 1

    # Set the weight to the path
    path.set_weight(actual_weight)

    return sequence

def get_next_random_vertex(linked_vertexes, current_vertex):
    return random.choice(linked_vertexes[tuple(current_vertex)])
      
def check_next_vertex(current_vertex, next_vertex, instant, previous_paths):
    for previous in previous_paths:
        previous_sequence = previous.get_sequence()

        if instant < len(previous_sequence):
            if next_vertex == previous_sequence[instant]:
                return False
            if previous_sequence[instant-1] == next_vertex and previous_sequence[instant] == current_vertex:
                return False
        else:
            # if the next vertex is the goal of another path
            if next_vertex == previous.get_goal():
                return False
    
    return True

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

def check_reachability(graph, grid, initials, goals):
    grid_representation = create_grid_representation(grid)
    linked_vertexes = graph.get_linked_vertexes()
    rows = grid.get_rows()
    cols = grid.get_cols()

    # Find islands using BFS
    def find_islands():
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

    islands = find_islands()

    # Build a map from points to islands
    point_to_island = {}
    for i, island in enumerate(islands):
        for point in island:
            point_to_island[point] = i

    # Check reachability
    reachables = []
    for initial, goal in zip(initials, goals):
        initial_island = point_to_island.get(initial)
        goal_island = point_to_island.get(goal)
        if initial_island is not None and goal_island is not None and initial_island == goal_island:
            reachables.append((initial, goal))

    return reachables
