import random
from models.path import Path
from algorithm.reach_goal import reach_goal
from controllers.reachability import check_reachability, find_islands

def create_random_initial_paths(goals_init_last_instant, graph, grid, time_limit):
    paths = set()

    islands = find_islands(graph, grid)

    for init, (goal, _) in list(goals_init_last_instant.items())[:-1]:
        if check_reachability(islands, init, goal):
            path = Path(init, goal)
            current = init
            path.add_node(0, current)
            t = 1

            while current != goal:
                if t > time_limit:
                    path.set_goal(current)
                    goals_init_last_instant[init] = (current, t-1)
                    break
                
                available_moves = graph.get_neighbors(current)
                available_moves = Path.remove_unreachable_moves(current, available_moves, paths, t)

                if not available_moves:
                    path.set_goal(current)
                    goals_init_last_instant[init] = (current, t-1)
                    break
                
                next, weight = random.choice(available_moves)

                if next != goal or goals_init_last_instant[init][1] < t:
                    path.add_node(t, next, weight)
                    current = next
                    t += 1
            
            paths.add(path)
    
    return paths

def create_reach_goal_paths(goals_init_last_instant, graph, time_limit):
    paths = set()

    for init, (goal, time_goal_get_passed) in list(goals_init_last_instant.items())[:-1]:
        path, _, _ = reach_goal(graph, init, goal, paths, time_goal_get_passed, time_limit)

        if path:
            paths.add(path) 
    
    return paths

def initial_paths_generator(graph, grid, goals_init_last_instant, time_limit, use_reach_goal = False):
    if use_reach_goal:
        paths = create_reach_goal_paths(goals_init_last_instant, graph, time_limit)
    else:
        paths = create_random_initial_paths(goals_init_last_instant, graph, grid, time_limit)

    return paths

