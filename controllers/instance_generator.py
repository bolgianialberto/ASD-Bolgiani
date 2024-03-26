from controllers.graph_generator import graph_generator
from controllers.paths_generator import initial_paths_generator
from models.instance import Instance
from algorithm.reach_goal import max_generator
import random

def instance_generator(grid, n_agents):    
    # Create a graph from the grid
    graph = graph_generator(grid)

    # Create a set of paths
    paths = initial_paths_generator(graph, grid, n_agents)

    # Create an initial state
    init = init_generator(graph, paths)

    # Create a goal state
    goal = goal_generator(graph, paths, init)

    # Compute max
    max = max_generator(graph, paths)

    # Create an instance
    instance = Instance(grid, graph, paths, init, goal, max)

    return instance

def init_generator(graph, paths):
    init = random.choice(graph.vertexes)
    while init in [path.get_init() for path in paths]:
        init = random.choice(graph.vertexes)
    return init

def goal_generator(graph, paths, init):
    goal = random.choice(graph.vertexes)
    while goal in [path.get_goal() for path in paths] or goal == init:
        goal = random.choice(graph.vertexes)
    return goal

