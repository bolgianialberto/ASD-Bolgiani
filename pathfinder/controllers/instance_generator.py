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

    # Add the number of verteces
    max_length += grid.get_rows()

    return max_length

def time_limit_generator(grid):
    return floor((grid.get_rows() + grid.get_cols()) / 4)

def create_inits_goals(graph, n_agents):
    verteces = list(graph.get_linked_verteces().keys())
    goals_init_last_instant = defaultdict(tuple)
    
    initials = set(random.sample(verteces, n_agents + 1))
    assigned_goals = set()
    
    for init in initials:
        goal = random.choice(verteces)
        while goal == init or goal in assigned_goals:
            goal = random.choice(verteces)
        goals_init_last_instant[goal] = (init, -1)
        assigned_goals.add(goal)
    
    return goals_init_last_instant

def instance_generator(grid, n_agents, use_reach_goal):
    # Create a graph
    graph = graph_generator(grid)

    goals_init_last_instant = create_inits_goals(graph, n_agents)
    last_key = list(goals_init_last_instant.keys())[-1]

    # Create a set of paths
    time_limit = time_limit_generator(grid)
    paths = initial_paths_generator(graph, grid, goals_init_last_instant, time_limit, use_reach_goal)

    # Get the initial and goal verteces
    # goal, (init, last_time_goal_passed) = goals_init_last_instant.popitem()

    # Compute max
    max = max_generator(grid, paths)

    goal, (init, _) = last_key, goals_init_last_instant[last_key]

    # Create an instance
    instance = Instance(grid, graph, paths, init, goal, max, goals_init_last_instant, time_limit)

    return instance

