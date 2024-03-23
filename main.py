from controllers.gui import Gui
from controllers.instance_generator import instance_generator
from controllers.grid_generator import grid_generator
from controllers.reach_goal import reach_goal
import argparse

ROWS = 15
COLS = 15
TRAVERSABILITY = 0.4
CLUSTER_FACTOR = 0.1
N_AGENTS = 3

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="Mode can be 'cli' or 'gui'", nargs='?', default='cli')
    parser.add_argument("--rows", type=int, help="number of rows")
    parser.add_argument("--cols", type=int, help="number of columns")
    parser.add_argument("--fcr", type=int, help="free cell ratio")
    parser.add_argument("--cf", type=int, help="cluster factor")
    parser.add_argument("--n_a", type=int, help="number of agents")

    args = parser.parse_args()

    rows = args.rows or ROWS
    cols = args.cols or COLS
    traversability = args.fcr or TRAVERSABILITY
    cluster_factor = args.cf or CLUSTER_FACTOR
    n_agents = args.n_a or N_AGENTS
        
    if args.mode == 'gui':
        gui_command(rows, cols, traversability, cluster_factor, n_agents)
    else:
        cli_command(rows, cols, traversability, cluster_factor, n_agents)

def cli_command(rows, cols, traversability, cluster_factor, n_agents):
    # Create a grid
    grid = grid_generator(rows, cols, traversability, cluster_factor)
    grid.print()

    # Create an instance
    instance = instance_generator(grid, n_agents)
    instance.print()

    # Add a new path
    new_path = reach_goal(instance)
    
    if new_path is None:
        print("No new path found")
        return

    # Print the new path
    print()
    print("New path")
    new_path.print()

def gui_command(rows, cols, traversability, cluster_factor, n_agents):
    # Create a GUI
    gui = Gui()
    gui.run(rows, cols, traversability, cluster_factor, n_agents)

if __name__ == "__main__":
    main()