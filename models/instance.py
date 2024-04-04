class Instance:
    
    def __init__(self, grid, graph, paths, init, goal, max, time_new_goal_get_passed):
        self.grid = grid
        self.graph = graph
        self.paths = paths
        self.init = init
        self.goal = goal
        self.max = max
        self.time_new_goal_get_passed = time_new_goal_get_passed
    
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

    def __str__(self):
        res = "Instance\n"
        for path in self.paths:
            res += path.__str__() + "\n"
        res += "Init: " + "(" + str(self.init[0]) + ", " + str(self.init[1]) + ")" + "\n"
        res += "Goal: " + "(" + str(self.goal[0]) + ", " + str(self.goal[1]) + ")" + "\n"
        res += "Max: " + str(self.max) + "\n"
        return res
            
    
    
    
