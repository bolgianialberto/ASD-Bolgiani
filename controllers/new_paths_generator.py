import random
from models.path import Path
from algorithm.new_reach_goal import reach_goal
from controllers.reachability import check_reachability, find_islands

TIME_LIMIT = 7

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
                if next != goal or goals_init_last_instant[init][1] < t:
                    path.add_node(t, next, weight)
                    current = next
                    t += 1
            
            paths.add(path)
    
    return paths

def create_reach_goal_paths(goals_init_last_instant, graph):
    paths = []

    for init, (goal, time_goal_get_passed) in list(goals_init_last_instant.items())[:-1]:
        path, _, _ = reach_goal(graph, init, goal, paths, time_goal_get_passed, TIME_LIMIT)
        # TODO: perchèèèèè
        if path:
            paths.append(path) 
    
    return paths

def initial_paths_generator(graph, grid, goals_init_last_instant, use_reach_goal = False):
    if use_reach_goal:
        return create_reach_goal_paths(goals_init_last_instant, graph)
    else:
        return create_random_initial_paths(goals_init_last_instant, graph, grid)

