class Grid:
    def __init__(self, rows, cols, obstacles):
        self.rows = rows
        self.cols = cols
        self.obstacles = obstacles
        self.grid_representation = self.create_grid_representation(rows, cols, obstacles)

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
    
    def get_grid_representation(self):
        return self.grid_representation
    
    def create_grid_representation(self, rows, cols, obstacles):
        grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                if (i, j) in obstacles:
                    row.append("X")
                else:
                    row.append(".")
            grid.append(row)
        return grid

    def __str__(self):
        res = "Grid\n"
        for row in self.grid_representation:
            res += " ".join(row) + "\n"
        return res
        
    


