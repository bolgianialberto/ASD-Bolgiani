class Instance:
    
    def __init__(self, grid, graph, paths, init, goal, max):
        self.grid = grid
        self.graph = graph
        self.paths = paths
        self.init = init
        self.goal = goal
        self.max = max
    
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

    def print(self):
        print("INSTANCE")

        self.grid.print()

        print()

        for path in self.paths:
            print(f"Path number {self.paths.index(path) + 1}")
            path.print()
            print()

        print("Init:", self.init, "\n")

        print("Goal:", self.goal, "\n")

        print("Max:", self.max)
            
    
    
    
