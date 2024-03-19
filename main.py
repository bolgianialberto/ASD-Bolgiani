from controllers.instance_generator import instance_generator
from controllers.visualization import print_gui
from controllers.reach_goal import reach_goal
import random

ROWS = 15
COLS = 15
TRAVERSABILITY = 0.9
CLUSTER_FACTOR = 0.1
N_AGENTS = 2

def main():
    # Create an instance
    instance = instance_generator(ROWS, COLS, TRAVERSABILITY, CLUSTER_FACTOR, N_AGENTS)

    # # Add a new path
    # new_path = reach_goal(instance)

    # # Check if the new path is valid
    # if new_path is None:
    #     print("No path found")
    #     return
    # else:
    #     # Print the new path
    #     new_path.print()

    # Print
    print_gui(instance) # poi anche new_path

if __name__ == "__main__":
    main()