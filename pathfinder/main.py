from controllers.gui import Gui
from controllers.instance_generator import instance_generator
from controllers.grid_generator import grid_generator
from algorithm.reach_goal import reach_goal
from controllers.profile_generator import Profile
import argparse
import random
import json

def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="Mode can be 'cli' or 'gui'", nargs='?', default='cli')
    parser.add_argument("--rows", type=int, help="number of rows")
    parser.add_argument("--cols", type=int, help="number of columns")
    parser.add_argument("--fcr", type=float, help="free cell ratio")
    parser.add_argument("--cf", type=float, help="cluster factor")
    parser.add_argument("--na", type=int, help="number of agents")
    parser.add_argument("--rg", action='store_true', help="use reach goal for initial paths")
    parser.add_argument("--seed", type=int, help="set seed for random number generator")

    return parser.parse_args()

# def set_default_parameters():
#     global ROWS, COLS, TRAVERSABILITY, CLUSTER_FACTOR, N_AGENTS, USE_REACH_GOAL, SEED
#     ROWS = 24
#     COLS = 28
#     TRAVERSABILITY = 0.7
#     CLUSTER_FACTOR = 0.2
#     N_AGENTS = 10
#     USE_REACH_GOAL = False
#     SEED = None

def set_parameters_from_file():
    global ROWS, COLS, TRAVERSABILITY, CLUSTER_FACTOR, N_AGENTS, USE_REACH_GOAL, SEED

    with open('parameters.json') as f:
        data = json.load(f)
        ROWS = data['rows']
        COLS = data['cols']
        TRAVERSABILITY = data['traversability']
        CLUSTER_FACTOR = data['cluster_factor']
        N_AGENTS = data['n_agents']
        USE_REACH_GOAL = data['use_reach_goal']
        SEED = data['seed']

def cli_command(rows, cols, traversability, cluster_factor, n_agents, use_reach_goal, seed):
    if seed:
        random.seed(seed)

    profile = Profile() # create a profile object to profile the execution time and memory usage of the algorithm
    # profile_grid_generator = Profile() # create a profile object to profile the grid generation
    # profile_instance_generator = Profile() # create a profile object to profile the instance generation
    # profile_path_generator = Profile() # create a profile object to profile the path generation

    # start screening
    profile.start_screening()

    # profile_grid_generator.start_screening()
    grid = grid_generator(rows, cols, traversability, cluster_factor)
    # profile_grid_generator.stop_screening()
    
    # profile_instance_generator.start_screening()
    instance = instance_generator(grid, n_agents, use_reach_goal)
    # profile_instance_generator.stop_screening()

    # profile_path_generator.start_screening()
    new_path, nodeDict, closed = reach_goal(instance.get_graph(), instance.get_init(), instance.get_goal(), instance.get_paths(), instance.get_goals_init_last_instant(), instance.get_max())
    # profile_path_generator.stop_screening()

    # stop screening
    profile.stop_screening()

    profile.set_values(rows, cols, traversability, cluster_factor, use_reach_goal, instance, new_path, nodeDict, closed, seed)

    profile.print_results_on_file()
    profile.print_profile()
        

def gui_command(rows, cols, traversability, cluster_factor, n_agents, seed, use_reach_goal):
    cell_size = 25

    gui = Gui()
    gui.run(rows, cols, traversability, cluster_factor, n_agents, cell_size, seed, use_reach_goal)

def main():
    # set_default_parameters()
    set_parameters_from_file()

    # run the automated tests
    # automated_test = Automated_test(ROWS, COLS, TRAVERSABILITY, CLUSTER_FACTOR, N_AGENTS, USE_REACH_GOAL)
    # automated_test.run_tests(10, 250, 10)

    # get the command line arguments
    args = get_cli_args()
    rows = args.rows or ROWS
    cols = args.cols or COLS
    traversability = args.fcr or TRAVERSABILITY
    cluster_factor = args.cf or CLUSTER_FACTOR
    n_agents = args.na or N_AGENTS
    use_reach_goal = args.rg or USE_REACH_GOAL
    seed = args.seed or SEED
        
    if args.mode == 'gui':
        gui_command(rows, cols, traversability, cluster_factor, n_agents, seed, use_reach_goal)
    else:
        cli_command(rows, cols, traversability, cluster_factor, n_agents, use_reach_goal, seed)
    
if __name__ == "__main__":
    main()