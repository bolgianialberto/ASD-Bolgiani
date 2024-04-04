import random
from models.path import Path
from controllers.reachability import check_reachability, find_islands

TIME_LIMIT = 10

def random_sequence_generator(graph, path, paths, goals_init_last_instant):
    pass

def create_random_initial_paths(n_agents, initials, goals_init_last_instant, graph, grid):
    paths = set()

    islands = find_islands(graph, grid)

    for goal, (init, _) in list(goals_init_last_instant.items())[:-1]:
        if check_reachability(islands, init, goal):
            path = Path(init, goal)
            current = init
            path.add_node(0, current)
            t = 1

            while current != goal:
                if t > TIME_LIMIT:
                    path.set_goal(current)
                    goals_init_last_instant[current] = (goals_init_last_instant[goal][0], t)
                    del goals_init_last_instant[goal]
                    break
                
                available_moves = graph.get_neighbors(current)

                Path.remove_unreachable_moves(available_moves, paths, t)

                next, weight = random.choice(available_moves)

                if next != goal or goals_init_last_instant[goal][1] < t:
                    path.add_node(t, next, weight)
                    current = next
                    t += 1
            
            paths.add(path)
    
    return paths


        

def initial_paths_generator(graph, grid, goals_init_last_instant, initials, n_agents, use_reach_goal = False):
    if not use_reach_goal:
        create_random_initial_paths(n_agents, initials, goals_init_last_instant, graph, grid)
