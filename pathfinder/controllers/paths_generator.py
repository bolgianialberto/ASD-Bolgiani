import random
from models.path import Path
from algorithm.reach_goal import reach_goal
from controllers.reachability import check_reachability, find_islands

def create_random_initial_paths(goals_init_last_instant, graph, grid, time_limit):
    paths = set()

    keys = list(goals_init_last_instant.keys())[:-1]

    for key in keys:
        goal, (init, _) = key, goals_init_last_instant[key]
        found = False # flag per capire se ho trovato il goal originale

        if check_reachability(graph, grid, init, goal):
            path = Path(init, goal)
            current = init
            path.add_node(0, current)
            t = 1

            while t <= time_limit:
                available_moves = graph.get_neighbors(current)
                available_moves = Path.remove_unreachable_moves(current, available_moves, paths, t)

                if not available_moves:
                    break

                next, weight = random.choice(available_moves)

                # se trovo il goal esco dal while e, fuori dal while, non cambio il goal
                if next == goal:
                    if t > goals_init_last_instant[goal][1]:
                        found = True
                        goals_init_last_instant[goal] = (init, t)
                        path.add_node(t, next, weight)
                        break
                    if len(available_moves) == 1:
                        break

                else:
                    if next in goals_init_last_instant:
                        goals_init_last_instant[next] = (goals_init_last_instant[next][0], max(goals_init_last_instant[next][1], t))

                    path.add_node(t, next, weight)
                    current = next
                    t += 1

            # se non ho trovato il goal originale, cambio il goal
            if not found: 
                path.set_goal(current)
                del goals_init_last_instant[goal]
                goals_init_last_instant[current] = (init, t-1)
            
            paths.add(path)
            # while current != goal:
            #     if t > time_limit:
            #         path.set_goal(current)
            #         del goals_init_last_instant[goal]
            #         goals_init_last_instant[current] = (init, t-1)
            #         break
                
            #     available_moves = graph.get_neighbors(current)
            #     available_moves = Path.remove_unreachable_moves(current, available_moves, paths, t)

            #     if not available_moves:
            #         path.set_goal(current)
            #         del goals_init_last_instant[goal]
            #         goals_init_last_instant[init] = (current, t-1)
            #         break
                
            #     next, weight = random.choice(available_moves)

            #     if next != goal or goals_init_last_instant[goal][1] < t:
            #         path.add_node(t, next, weight)
            #         current = next
            #         t += 1
            
            
            # print(f"path: {path.get_sequence()}")

    return paths

def create_reach_goal_paths(goals_init_last_instant, graph, time_limit):
    paths = set()

    for goal, (init, time_goal_get_passed) in list(goals_init_last_instant.items())[:-1]:
        path, _, _ = reach_goal(graph, init, goal, paths, goals_init_last_instant, time_limit)

        if path:
            paths.add(path) 
    
    return paths

def initial_paths_generator(graph, grid, goals_init_last_instant, time_limit, use_reach_goal = False):
    if use_reach_goal:
        paths = create_reach_goal_paths(goals_init_last_instant, graph, time_limit)
    else:
        paths = create_random_initial_paths(goals_init_last_instant, graph, grid, time_limit)

    return paths

