from models.path import Path
from algorithm.reach_goal import reach_goal
import random

def initial_paths_generator(graph, grid, initials, goals, goals_last_instant, use_reach_goal = False):
    # paths will contain a list of paths
    paths = []

    # reachables is a list of couples (init, goal) that are reachable
    reachables = check_reachability(graph, grid, initials, goals)

    # Create n paths
    for initial, goal in reachables:
        path = path_generator(graph, initial, goal, paths, goals_last_instant, use_reach_goal)
        paths.append(path)
    
    Path.set_goal_last_instant(goals_last_instant)
    return paths

def path_generator(graph, init, goal, previous_paths, goals_last_instant, use_reach_goal = False):
    if use_reach_goal:
        path = reach_goal(graph, init, goal, previous_paths, goals_last_instant)

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

def check_reachability(graph, grid, initials, goals):
    grid_representation = grid.get_grid_representation()

    # reachables is a list of couples (init, goal) that are reachable
    reachables = []

    # visited is a list of set of vertexes belonging to the same island
    islands = []

    # Get the linked vertexes
    linked_vertexes = graph.get_linked_vertexes()

    # Get the rows and the columns
    rows = grid.get_rows()
    cols = grid.get_cols()

    def dfs(r, c, island):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid_representation[r][c] == "X" or (r, c) in island:
            return
        island.add((r, c))
        for vertex in linked_vertexes[(r, c)]:
            dfs(vertex[0][0], vertex[0][1], island)
            
    for r in range(rows):
        for c in range(cols):
            if grid_representation[r][c] == "." and all((r, c) not in island for island in islands):
                island = set()
                dfs(r, c, island)
                islands.append(island)

    for initial, goal in zip(initials, goals):
        for island in islands:
            if initial in island and goal in island:
                reachables.append((initial, goal))
    
    return reachables
