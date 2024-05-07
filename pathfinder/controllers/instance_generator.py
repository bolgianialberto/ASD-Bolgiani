from collections import defaultdict
from math import floor
from controllers.graph_generator import graph_generator
from controllers.paths_generator import initial_paths_generator
from models.instance import Instance
import random

def max_generator(grid, paths):
    max_length = 0
    # Get the longest path
    for path in paths:
        if len(path.get_sequence()) > max_length:
            max_length = len(path.get_sequence())

    # Add the number of vertexes
    max_length += grid.get_rows()

    return max_length

def time_limit_generator(grid):
    return floor((grid.get_rows() + grid.get_cols()) / 4)

def create_inits_goals(graph, n_agents):
    vertexes = list(graph.get_linked_vertexes().keys())
    goals_init_last_instant = defaultdict(tuple)
    
    initials = set(random.sample(vertexes, n_agents + 1))
    
    for init in initials:
        goal = random.choice(vertexes)
        while goal == init:
            goal = random.choice(vertexes)
        goals_init_last_instant[init] = (goal, -1)
    
    return goals_init_last_instant

def instance_generator(grid, n_agents, use_reach_goal):    
    # Create a graph
    graph = graph_generator(grid)
    
    goal_init_last_instant = create_inits_goals(graph, n_agents)
    
    # Create a set of paths
    time_limit = time_limit_generator(grid)
    paths = initial_paths_generator(graph, grid, goal_init_last_instant, time_limit, use_reach_goal)
    
    # Get the initial and goal vertexes
    init, (goal, time_new_goal_get_passed) = goal_init_last_instant.popitem()

    # Compute max
    max = max_generator(grid, paths)

    # Create an instance
    instance = Instance(grid, graph, paths, init, goal, max, time_new_goal_get_passed, time_limit)

    return instance

