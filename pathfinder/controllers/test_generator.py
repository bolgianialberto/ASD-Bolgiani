import matplotlib.pyplot as plt
from controllers.profile_generator import Profile
from controllers.instance_generator import instance_generator
from controllers.grid_generator import grid_generator
from models.path import Path
from algorithm.reach_goal import reach_goal

class Automated_test:
    def __init__(self, rows, cols, traversability, cluster_factor, n_agents, use_reach_goal):
        self.rows = rows
        self.cols = cols
        self.traversability = traversability
        self.cluster_factor = cluster_factor
        self.n_agents = n_agents
        self.use_reach_goal = use_reach_goal

        self.results = []

    def run_tests(self, min_size, max_size, step):
        dim = list(range(min_size, max_size+1, step))
        for dimension in dim:
            profile = Profile()
            profile.start_screening()

            grid = grid_generator(dimension, dimension, self.traversability, self.cluster_factor)
            
            instance = instance_generator(grid, self.n_agents, self.use_reach_goal)
            
            new_path, nodeDict, closed = reach_goal(instance.get_graph(), instance.get_init(), instance.get_goal(), instance.get_paths(), instance.get_goals_init_last_instant(), instance.get_max())
            
            if new_path is None:
                print("No new path found")
            
            profile.stop_screening()

            profile.set_values(dimension, dimension, self.traversability, self.cluster_factor, self.use_reach_goal, instance, new_path, nodeDict, closed)

            profile.print_profile()
        