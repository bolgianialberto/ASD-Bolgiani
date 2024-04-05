import random
from models.path import Path
from controllers.reachability import check_reachability, find_islands

TIME_LIMIT = 10

def create_random_initial_paths(goals_init_last_instant, graph, grid):
    paths = set()

    islands = find_islands(graph, grid)

    for init, (goal, _) in list(goals_init_last_instant.items())[:-1]:
        if check_reachability(islands, init, goal):
            path = Path(init, goal)
            current = init
            path.add_node(0, current)
            t = 1

            while current != goal:
                # TODO: cambia time_limit in base alla dimensione
                if t > TIME_LIMIT:
                    path.set_goal(current)
                    goals_init_last_instant[init] = (current, t-1)
                    break
                
                available_moves = graph.get_neighbors(current)

                Path.remove_unreachable_moves(current, available_moves, paths, t)

                next, weight = random.choice(available_moves)

                # TODO: cambia goals_init_last_instant[goal] ci va messo init credo
                if next != goal or goals_init_last_instant[goal][1] < t:
                    path.add_node(t, next, weight)
                    current = next
                    t += 1
            
            paths.add(path)
    
    return paths

def initial_paths_generator(graph, grid, goals_init_last_instant, initials, n_agents, use_reach_goal = False):
    if not use_reach_goal:
        paths = create_random_initial_paths(goals_init_last_instant, graph, grid)
    
    return paths
