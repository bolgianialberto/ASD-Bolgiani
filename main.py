from controllers.gui import Gui
from models.path import Path
from controllers.instance_generator import instance_generator
from controllers.grid_generator import grid_generator
from algorithm.reach_goal import reach_goal
import argparse
import time
import os
import psutil

ROWS = 15
COLS = 15   
TRAVERSABILITY = 0.5
CLUSTER_FACTOR = 0.1
N_AGENTS = 3
CELL_SIZE = 25
USE_REACH_GOAL = False

def cli_command(rows, cols, traversability, cluster_factor, n_agents, use_reach_goal):
    grid = grid_generator(rows, cols, traversability, cluster_factor)
    instance = instance_generator(grid, n_agents, use_reach_goal)
    print(instance)

    new_path = reach_goal(instance.get_graph(), instance.get_init(), instance.get_goal(), instance.get_paths(), Path.get_goal_last_instant(), instance.get_max())
    
    if new_path is None:
        print("No new path found")
    else:
        print()
        print("New path")
        print(new_path)

def gui_command(rows, cols, traversability, cluster_factor, n_agents, cell_size):
    gui = Gui()
    gui.run(rows, cols, traversability, cluster_factor, n_agents, cell_size)

def memory_usage():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss
    return mem/1024/1024 # MB

def main():
    start_time = time.time()

    # gui_command(ROWS, COLS, TRAVERSABILITY, CLUSTER_FACTOR, N_AGENTS, CELL_SIZE)
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="Mode can be 'cli' or 'gui'", nargs='?', default='cli')
    parser.add_argument("--rows", type=int, help="number of rows")
    parser.add_argument("--cols", type=int, help="number of columns")
    parser.add_argument("--fcr", type=float, help="free cell ratio")
    parser.add_argument("--cf", type=float, help="cluster factor")
    parser.add_argument("--na", type=int, help="number of agents")
    parser.add_argument("--rg", action='store_true', help="use reach goal for initial paths")

    args = parser.parse_args()

    rows = args.rows or ROWS
    cols = args.cols or COLS
    traversability = args.fcr or TRAVERSABILITY
    cluster_factor = args.cf or CLUSTER_FACTOR
    n_agents = args.na or N_AGENTS
    use_reach_goal = args.rg or USE_REACH_GOAL
        
    if args.mode == 'gui':
        gui_command(rows, cols, traversability, cluster_factor, n_agents, CELL_SIZE)
    else:
        cli_command(rows, cols, traversability, cluster_factor, n_agents, use_reach_goal)
    
    end_time = time.time()
    print("Execution time: " + str(end_time - start_time) + " seconds")
    print("Memory usage: " + str(memory_usage()) + " MB")

if __name__ == "__main__":
    main()