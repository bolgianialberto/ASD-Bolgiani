from itertools import islice
from models.path import Path
from algorithm.reach_goal import reach_goal
import random
from collections import defaultdict, deque
from controllers.reachability import check_reachability, find_islands

def initial_paths_generator(graph, grid, goals_init_last_instant, use_reach_goal = False):
    # paths will contain a list of paths
    paths = set()

    # find islands
    islands = find_islands(graph, grid)

    # reachables is a list of couples (init, goal) that are reachable
    # TODO: non devo farlo dell'ultimo goal
    for goal, (initial, _) in islice(goals_init_last_instant.items(), len(goals_init_last_instant) - 1):
        if check_reachability(islands, initial, goal):
            path = path_generator(graph, initial, goal, paths, goals_init_last_instant, use_reach_goal)
            paths.add(path)

    return paths

def path_generator(graph, init, goal, previous_paths, goals_init_last_instant, use_reach_goal = False):
    if use_reach_goal:
        path, _, _ = reach_goal(graph, init, goal, previous_paths, goals_init_last_instant)
        
        # update goals_init_last_instant with the last instant the goal was crossed
        for t, vertex in enumerate(path.get_sequence()):
            if vertex in goals_init_last_instant:
                goals_init_last_instant[vertex] = (goals_init_last_instant[vertex][0], max(goals_init_last_instant[vertex][1], t))

    else:
        path = Path(init, goal)
        random_sequence_generator(graph, path, previous_paths, goals_init_last_instant)

    return path

def random_sequence_generator(graph, path, previous_paths, goals_init_last_instant):
    init = path.get_init()
    goal = path.get_goal()

    path.add_node(0, init)
    
    current_vertex = init
    instant = 1

    # Generate the sequence of moves
    while current_vertex != goal:
        if instant > 10:
            # TODO: sto provando a impostare un nuovo goal se continua a cercare senza trovare
            path.set_goal(current_vertex)
            goals_init_last_instant[current_vertex] = (goals_init_last_instant[goal][0], instant-1)
            del goals_init_last_instant[goal]
            break
        # TODO: Continuo a prendere il migliore anche se non posso? (ostacolo oppure goal irraggiungibile)

        next_vertex, weight = get_next_random_vertex(graph, current_vertex)
        
        # If the next_vertex is the goal, I have to check if it is passed by other paths after the last instant
        if next_vertex == goal:
            if goals_init_last_instant[goal][1] > instant:
                while next_vertex == goal:
                    next_vertex, weight = get_next_random_vertex(graph, current_vertex)

        # Check if there are conflicts
        if check_next_vertex(current_vertex, next_vertex, instant, previous_paths):
            path.add_node(instant, next_vertex, weight)
            current_vertex = next_vertex

            # If the next vertex is one of the other goal, I have to update the last instant it was crossed
            if current_vertex in goals_init_last_instant and current_vertex != goal:
                goals_init_last_instant[current_vertex] = (goals_init_last_instant[current_vertex][0], instant)
            
            instant += 1
    
    # The real value of instant 
    instant -= 1

def get_next_random_vertex(graph, current_vertex):
    return random.choice(graph.get_neighbors(current_vertex))
      
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
