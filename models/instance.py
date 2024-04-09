class Instance:
    
    def __init__(self, grid, graph, paths, init, goal, max, time_new_goal_get_passed, time_limit_agents):
        self.grid = grid
        self.graph = graph
        self.paths = paths
        self.init = init
        self.goal = goal
        self.max = max
        self.time_new_goal_get_passed = time_new_goal_get_passed
        self.time_limit_agents = time_limit_agents+1
    
    def get_time_limit_agents(self):
        return self.time_limit_agents

    def get_grid(self):
        return self.grid
    
    def get_graph(self):
        return self.graph
    
    def get_paths(self):
        return self.paths
    
    def get_init(self):
        return self.init
    
    def get_goal(self):
        return self.goal
    
    def get_max(self):
        return self.max
    
    def get_time_new_goal_get_passed(self):
        return self.time_new_goal_get_passed

    def print_instance(self):
        print("Instance")
        for path in self.paths:
            path.print_path()
        print("Init: " + str(self.init))
        print("Goal: " + str(self.goal))
        print("Max: " + str(self.max))
            
    
    
    
