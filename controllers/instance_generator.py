from controllers.graph_generator import graph_generator
from controllers.paths_generator import initial_paths_generator
from models.instance import Instance
from algorithm.reach_goal import max_generator
import random
from models.path import Path

def instance_generator(grid, n_agents, use_reach_goal):    
    # Create a graph from the grid
    graph = graph_generator(grid)

    # Create all the initials and goals
    initials = random.sample(graph.vertexes, n_agents + 1)
    goals = []
    goals_last_instant = {}

    for initial in initials:
        g = random.choice(graph.vertexes)
        while g == initial or g in goals:
            g = random.choice(graph.vertexes)
        goals.append(g)
        goals_last_instant[g] = 0
        
    Path.set_goal_last_instant(goals_last_instant)

    # Create a set of paths
    paths = initial_paths_generator(graph, grid, initials[:-1], goals[:-1], goals_last_instant, use_reach_goal)

    # Create an initial state
    init = initials[-1]

    # Create a goal state
    goal = goals[-1]

    # Compute max
    max = max_generator(graph, paths)

    # Create an instance
    instance = Instance(grid, graph, paths, init, goal, max)

    return instance

