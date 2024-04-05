from collections import defaultdict
from controllers.graph_generator import graph_generator
from controllers.new_paths_generator import initial_paths_generator
from models.instance import Instance
from algorithm.reach_goal import max_generator
import random
from models.path import Path

random.seed(0)

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
    paths = initial_paths_generator(graph, grid, goal_init_last_instant, n_agents, use_reach_goal)
    
    # # Get the initial and goal vertexes
    # init, (goal, time_new_goal_get_passed) = goal_init_last_instant.popitem()

    # # Compute max
    # max = max_generator(graph, paths)

    # # Create an instance
    # instance = Instance(grid, graph, paths, init, goal, max, time_new_goal_get_passed)

    # return instance
    for path in paths:
        print(path)

