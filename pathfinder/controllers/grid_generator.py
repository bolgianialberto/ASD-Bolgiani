from math import floor
import random
from models.grid import Grid
from models.path import Path

nsew_directions = Path.get_nsew_moves()

def grid_generator(rows, cols, traversability, cluster_factor):
    grid = Grid(rows, cols)

    add_obstacles(grid, traversability, cluster_factor)

    return grid

def add_obstacles(grid, traversability, cluster_factor):
    n_obstacles = int((1 - traversability) * grid.get_rows() * grid.get_cols())

    if n_obstacles > 0:
        n_cluster = int(cluster_factor * n_obstacles)

        if n_cluster > 0:
            add_cluster(grid, n_cluster)

        grid.add_random_obstacles(n_obstacles - n_cluster)

def add_cluster(grid, n_cluster):
    initial_r = random.randint(0, grid.get_rows() - 1)
    initial_c = random.randint(0, grid.get_cols() - 1)

    grid.add_obstacle((initial_r, initial_c))

    while len(grid.get_obstacles()) < n_cluster:
        (r, c) = random.choice(list(grid.get_obstacles()))
        direction = random.choice(nsew_directions)

        next_r, next_c = r + direction[0], c + direction[1]

        if 0 <= next_r < grid.get_rows() and 0 <= next_c < grid.get_cols() and grid.is_free(next_r, next_c):
            grid.add_obstacle((next_r, next_c))