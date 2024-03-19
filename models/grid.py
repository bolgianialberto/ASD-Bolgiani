class Grid:
    def __init__(self, rows, cols, obstacles):
        self.rows = rows
        self.cols = cols
        self.obstacles = obstacles

    def get_rows(self):
        return self.rows
    
    def set_rows(self, rows):
        self.rows = rows

    def set_cols(self, cols):
        self.cols = cols
    
    def get_cols(self):
        return self.cols
    
    def get_obstacles(self):
        return self.obstacles
    
    def print(self):
        print("Grid")

        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in self.obstacles:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print()
        
    


