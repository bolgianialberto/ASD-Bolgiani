import random
from models.grid import Grid
from models.path import Path

def grid_generator(rows, cols, traversability, cluster_factor):
    # Define all cells
    all_cells = [(i, j) for i in range(rows) for j in range(cols)]

    # Create a list of obstacles
    obstacles = create_obstacles(all_cells, traversability, cluster_factor)

    # Create a grid
    grid = Grid(rows, cols, obstacles)

    return grid

def create_obstacles(all_cells, traversability, cluster_factor):
    # Compute number of traversable cells
    n_traversable = int(traversability * len(all_cells))

    # Compute number of obstacles
    n_obstacles = len(all_cells) - n_traversable

    # Compute number of cells in a cluster
    n_cluster = int(cluster_factor * n_obstacles)

    # At first create a cluster of obstacles
    cluster = create_cluster(all_cells, n_cluster)

    # Create a list of obstacles
    obstacles = cluster + random.sample(set(all_cells) - set(cluster), n_obstacles - n_cluster)
    
    return obstacles

def create_cluster(all_cells, n_cluster):
    cluster = []

    nsew_directions = Path.get_nsew_moves()

    if n_cluster > 0:
        cell = random.choice(all_cells)
        n_cluster -= 1
        cluster.append(cell)
        
        while n_cluster > 0:
            cell = random.choice(cluster)
            dir = random.choice(nsew_directions)
            new_vertex = (cell[0] + dir[0], cell[1] + dir[1])
            if new_vertex in all_cells and new_vertex not in cluster:
                cluster.append(new_vertex)
                n_cluster -= 1
    
    return cluster
