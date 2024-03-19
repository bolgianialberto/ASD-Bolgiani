from models.path import Path
import math
import random

def initial_paths_generator(graph, n_agents):
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

    # Create n paths
    for _ in range(n_agents):
        path = path_generator(graph, initials.pop(), goals.pop(), paths, goals_last_instant)
        paths.append(path)
    
    return paths

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
        # Get the next vertex and weight
        next_vertex, weight = get_next_vertex(linked_vertexes, current_vertex, goal, instant)

        # If the next_vertex is the goal, I have to check if it is passed by other paths after the last instant
        if next_vertex == goal:
            if goals_last_instant[goal] > instant:
                while next_vertex == goal:
                    next_vertex, weight = get_next_vertex(linked_vertexes, current_vertex, goal, instant)

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

def get_next_vertex(linked_vertexes, current_vertex, goal, instant):
    # random_next_vertex, weight_random_next_vertex = random.choice(linked_vertexes[tuple(current_vertex)])
    # best_vertex, weight_best_vertex = get_next_best_vertex(linked_vertexes[tuple(current_vertex)], goal)

    # if instant %2 == 0:
    #     return random_next_vertex, weight_random_next_vertex

    # return random.choice([(random_next_vertex, weight_random_next_vertex), (best_vertex, weight_best_vertex)])
    return get_next_best_vertex(linked_vertexes[tuple(current_vertex)], goal)


def get_next_best_vertex(possible_vertices, goal):
    # Compute the distance between the possible vertices and the goal
    distances = [(vertex, weight, euclidean_distance(vertex, goal)) for vertex, weight in possible_vertices]
    
    # Order the vertices by distance
    sorted_vertices = sorted(distances, key=lambda x: x[2])
    print("Sorted vertices:", sorted_vertices[0])

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
