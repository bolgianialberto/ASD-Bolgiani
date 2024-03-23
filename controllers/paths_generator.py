from models.path import Path
import math
import random

def initial_paths_generator(graph, grid, n_agents):
    # paths will contain a list of paths
    paths = []

    # goals_last_instant will track the last instant each goal was crossed by any path
    goals_last_instant = {}

    # Generate pairs of distinct vertices for init and goal
    initials = random.sample(graph.vertexes, n_agents)
    goals = []

    for initial in initials:
        g = random.choice(graph.vertexes)
        while g == initial or g in goals:
            g = random.choice(graph.vertexes)
        goals.append(g)
        goals_last_instant[g] = 0

    # Check if the goals are reachable
    # reachables is a list of couples (init, goal) that are reachable
    reachables = check_reachability(graph, grid, initials, goals)

    # Create n paths
    for initial, goal in reachables:
        path = path_generator(graph, initial, goal, paths, goals_last_instant)
        paths.append(path)
    
    return paths

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

def path_generator(graph, init, goal, previous_paths, goals_last_instant):
    # Initialize the path
    path = Path(init, goal)

    # Generate the sequence of moves
    sequence = random_sequence_generator(graph, path, previous_paths, goals_last_instant)

    # Set the sequence of moves to the path
    path.set_sequence(sequence)

    return path

def random_sequence_generator(graph, path, previous_paths, goals_last_instant):
    # sequence will contain a list of moves
    sequence = []

    # Initialize the actual weight
    actual_weight = 0

    # Get init and goal
    init = path.get_init()
    goal = path.get_goal()

    # Add start to sequence
    sequence.append(init)
    
    # Initialize the current vertex (instant = 0)
    current_vertex = init
    
    # Initialize the instant
    instant = 1

    # Get the linked vertexes
    linked_vertexes = graph.get_linked_vertexes()

    # Generate the sequence of moves
    while current_vertex != goal:
        if instant > 5:
            # TODO: sto provando a impostare un nuovo goal se continua a cercare senza trovare
            path.set_goal(current_vertex)
            goals_last_instant[current_vertex] = instant-1
            del goals_last_instant[goal]
            break
        # TODO: Continuo a prendere il migliore anche se non posso? (ostacolo oppure goal irraggiungibile)

        # Get the next vertex and weight
        
        next_vertex, weight = get_next_random_vertex(linked_vertexes, current_vertex)
        
        # If the next_vertex is the goal, I have to check if it is passed by other paths after the last instant
        if next_vertex == goal:
            if goals_last_instant[goal] > instant:
                while next_vertex == goal:
                    # next_vertex, weight = get_next_best_vertex(linked_vertexes, current_vertex, goal)
                    next_vertex, weight = get_next_random_vertex(linked_vertexes, current_vertex)

        # Check if there are conflicts
        if check_next_vertex(current_vertex, next_vertex, instant, previous_paths):
            sequence.append(next_vertex)
            current_vertex = next_vertex
            actual_weight += weight

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


def get_next_best_vertex(linked_vertexes, current_vertex, goal):
    # Get the possible vertices
    possible_vertices = linked_vertexes[current_vertex]

    # Compute the distance between the possible vertices and the goal
    distances = [(vertex, weight, euclidean_distance(vertex, goal)) for vertex, weight in possible_vertices]
    
    # Order the vertices by distance
    sorted_vertices = sorted(distances, key=lambda x: x[2])
    
    vertex, weight, _ = sorted_vertices[0]
    # Select the closest vertex
    return vertex, weight

def euclidean_distance(vertex, goal):
    # Compute the Euclidian dinstance between two vertexes
    x1, y1 = vertex
    x2, y2 = goal
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)      
    
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
