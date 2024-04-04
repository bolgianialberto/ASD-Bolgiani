from collections import defaultdict
from controllers.graph_generator import graph_generator
from controllers.paths_generator import initial_paths_generator
from models.instance import Instance
from algorithm.reach_goal import max_generator
import random
from models.path import Path

random.seed(0)

def create_inits_goals(graph, n_agents):
    vertexes = list(graph.get_linked_vertexes().keys())
    goals_init_last_instant = defaultdict(tuple)
    initials = []
    
    goals = set(random.sample(vertexes, n_agents + 1))
    
    for goal in goals:
        init = random.choice(vertexes)
        while init == goal:
            init = random.choice(vertexes)
        goals_init_last_instant[goal] = (init, -1)
        initials.append(init)
    
    return goals_init_last_instant, initials
        

def instance_generator(grid, n_agents, use_reach_goal):    
    # Create a graph
    graph = graph_generator(grid)
    
    goal_init_last_instant, initials = create_inits_goals(graph, n_agents)
    
    # Create a set of paths
    paths = initial_paths_generator(graph, grid, goal_init_last_instant, initials, n_agents, use_reach_goal)
    
    # Get the initial and goal vertexes
    goal, (init, time_new_goal_get_passed) = goal_init_last_instant.popitem()

    # Compute max
    max = max_generator(graph, paths)

    # Create an instance
    instance = Instance(grid, graph, paths, init, goal, max, time_new_goal_get_passed)

    return instance

