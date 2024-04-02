import time
import tracemalloc

class Profile():
    def __init__(self):
        self.rows = None
        self.cols = None
        self.traversability = None
        self.cluster_factor = None
        self.use_reach_goal = None
        
        self.instance = None
        self.new_path = None

        self.nodeDict = None
        self.closed = None

        self.start_time = None
        self.total_time = None

        self.peak_memory = None

    def start_screening(self):
        self.start_time = time.time()
        tracemalloc.start()
    
    def stop_screening(self):
        self.total_time = time.time() - self.start_time
        
        mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        self.peak_memory = mem[1]/1024/1024

    def set_values(self, rows, cols, traversability, cluster_factor, use_reach_goal, instance, new_path, nodeDict, closed):
        self.rows = rows
        self.cols = cols
        self.traversability = traversability
        self.cluster_factor = cluster_factor
        self.use_reach_goal = use_reach_goal
        self.instance = instance
        self.new_path = new_path
        self.nodeDict = nodeDict
        self.closed = closed

    def print_profile(self):
        print("Parameters:")
        print(f"rows: {self.rows}")
        print(f"cols: {self.cols}")
        print(f"free cell ratio: {self.traversability}")
        print(f"cluster factor: {self.cluster_factor}")
        print()

        print("Instance:")
        print(f"pre existing pahts use reach goal: {self.use_reach_goal}")
        print(f"pre existing paths number: {len(self.instance.get_paths())}")
        for i, path in enumerate(self.instance.get_paths()):
            print(f"path {i} lenght: {len(path.get_sequence())}")
        print()

        if not self.new_path:
            print("No new path found")
            print()
        else:
            print("New Path:")
            print(f"Init: {self.new_path.get_init()}")
            print(f"Goal: {self.new_path.get_goal()}")
            print(f"Weight: {self.new_path.get_weight()}")
            print(f"Max lenght: {self.instance.get_max()}")
            print(f"Lenght: {len(self.new_path.get_sequence())}")
            print(f"Open lenght: {len(self.nodeDict)}")
            print(f"Closed lenght: {len(self.closed)}")
            print()

        print("Time and Memory:")
        print(f"total time: {self.total_time} seconds")
        print(f"peak memory: {self.peak_memory} MB")

    
