import random

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.obstacles = set()

    def get_rows(self):
        return self.rows
    
    def set_rows(self, rows):
        self.rows = rows

    def set_cols(self, cols):
        self.cols = cols
    
    def get_cols(self):
        return self.cols
    
    def is_free(self, r, c):
        return not self.is_obstacle(r, c)
    
    def is_obstacle(self, r, c):
        return (r, c) in self.obstacles

    def add_obstacle(self, obstacle):
        self.obstacles.add(obstacle)

    def get_obstacles(self):
        return self.obstacles
    
    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
    
    def add_random_obstacles(self, n_obstacles):
        for i in range(n_obstacles):
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)

            while (r,c) in self.obstacles:
                r = random.randint(0, self.rows-1)
                c = random.randint(0, self.cols-1)

            self.add_obstacle((r, c))
    

    # TODO: togli questi due
    def create_grid_representation(self):
        grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if (i, j) in self.obstacles:
                    row.append("X")
                else:
                    row.append(".")
            grid.append(row)
        return grid

    def print_grid_representation(self):
        grid = self.create_grid_representation()
        for row in grid:
            print(row)

    
        
    


