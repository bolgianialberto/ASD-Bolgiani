import time
import tracemalloc

class Profile():
    def __init__(self):
        self.rows = None
        self.cols = None
        self.traversability = None
        self.cluster_factor = None
        self.use_reach_goal = None
        self.seed = None
        
        self.instance = None
        self.new_path = None

        self.nodeDict = None
        self.closed = None

        self.start_time = None
        self.total_time = None
        self.total_grid_time = None
        self.total_instance_time = None
        self.total_path_time = None
        self.wait_counter = None

        self.peak_memory = None
        self.peak_memory_grid = None
        self.peak_memory_instance = None
        self.peak_memory_path = None
    
    def set_rows(self, rows):
        self.rows = rows

    def set_cols(self, cols):
        self.cols = cols

    def set_traversability(self, traversability):
        self.traversability = traversability

    def set_cluster_factor(self, cluster_factor):
        self.cluster_factor = cluster_factor

    def set_use_reach_goal(self, use_reach_goal):
        self.use_reach_goal = use_reach_goal

    def set_instance(self, instance):
        self.instance = instance
    
    def set_n_agents(self, n_agents):
        self.n_agents = n_agents

    def set_new_path(self, new_path):
        self.new_path = new_path

    def set_nodeDict(self, nodeDict):
        self.nodeDict = nodeDict

    def set_closed(self, closed):
        self.closed = closed
    
    def set_seed(self, seed):
        self.seed = seed

    def set_values(self, rows, cols, traversability, cluster_factor, use_reach_goal, instance, new_path, nodeDict, closed, seed):
        self.rows = rows
        self.cols = cols
        self.traversability = traversability
        self.cluster_factor = cluster_factor
        self.seed = seed
        self.use_reach_goal = use_reach_goal
        self.instance = instance
        if new_path:
            self.new_path = new_path
            self.nodeDict = nodeDict
            self.closed = closed
            self.wait_counter = self.count_wait_moves(self.new_path)

    def start_screening(self):
        self.start_time = time.perf_counter()
        tracemalloc.start()
    
    def stop_screening(self, mode="normal"):
        end_time = time.perf_counter()
        elapsed_time = end_time - self.start_time

        mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        if mode == "normal":
            self.peak_memory = mem[1]/1024/1024
            self.total_time = elapsed_time
        if mode == "grid":
            self.peak_memory_grid = mem[1]/1024/1024
            self.total_grid_time = elapsed_time
        if mode == "instance":
            self.peak_memory_instance = mem[1]/1024/1024
            self.total_instance_time = elapsed_time
        if mode == "path":
            self.peak_memory_path = mem[1]/1024/1024
            self.total_path_time = elapsed_time

    def count_wait_moves(self, path):
        wait_counter = 0
        for i in range(1, len(path.get_sequence()) - 1):
            if path.get_sequence()[i] == path.get_sequence()[i - 1]:
                wait_counter += 1
        return wait_counter

    def print_results_on_file(self):
        output_file = 'results.txt'
        
        with open(output_file, 'w') as f:
            f.write(self.get_profile_string())

    def print_profile(self):
        print("PARAMETERS:")
        print(f"rows: {self.rows}")
        print(f"cols: {self.cols}")
        print(f"free cell ratio: {self.traversability}")
        print(f"cluster factor: {self.cluster_factor}")
        print(f"seed: {self.seed}")
        print()

        print("INSTANCE:")
        print(f"agents use reach goal: {self.use_reach_goal}")
        print(f"agents' number: {len(self.instance.get_paths())}")
        print(f"agents' max length: {self.instance.get_time_limit_agents()}")

        # for i, path in enumerate(self.instance.get_paths()):
        #     print(f"Path {i+1}: sequence: {path.get_sequence()}, length: {len(path.get_sequence())}, weight: {path.get_weight()}")
            
        print()

        if not self.new_path:
            print("No new path found")
            print()
        else:
            print("NEW PATH:")
            print(f"Init: {self.new_path.get_init()}")
            print(f"Goal: {self.new_path.get_goal()}")
            print(f"Weight: {self.new_path.get_weight()}")
            print(f"Max lenght: {self.instance.get_max()+1}")
            print(f"Lenght: {len(self.new_path.get_sequence())}")
            print(f"Open lenght: {len(self.nodeDict)}")
            print(f"Closed lenght: {len(self.closed)}")
            print(f"Wait moves: {self.wait_counter}")
            print(f"Sequence: {self.new_path.get_sequence()}")
            print()

        if self.peak_memory_grid:
            print("TIME AND MEMORY:")
            self.print_time()
            self.print_memory()
            print()
    
        elif self.peak_memory_grid:
            print("TIME AND MEMORY GRID GENERATION:")
            print(f"grid generation time: {self.total_grid_time} seconds")
            print(f"grid generation memory: {self.peak_memory_grid} MB")
            print()
        
        elif self.peak_memory_instance:
            print("TIME AND MEMORY INSTANCE GENERATION:")
            print(f"instance generation time: {self.total_instance_time} seconds")
            print(f"instance generation memory: {self.peak_memory_instance} MB")
            print()
        
        elif self.peak_memory_path:
            print("TIME AND MEMORY PATH GENERATION:")
            print(f"path generation time: {self.total_path_time} seconds")
            print(f"path generation memory: {self.peak_memory_path} MB")
            print()

        elif self.peak_memory:
            print("TIME AND MEMORY:")
            self.print_time()
            self.print_memory()
            print()

    def print_time(self):
        print(f"total time: {self.total_time} seconds")

    def print_memory(self):
        print(f"total memory: {self.peak_memory} MB")

    def get_profile_string(self):
        result = ""

        result += "PARAMETERS:\n"
        result += f"rows: {self.rows}\n"
        result += f"cols: {self.cols}\n"
        result += f"free cell ratio: {self.traversability}\n"
        result += f"cluster factor: {self.cluster_factor}\n\n"
        result += f"seed: {self.seed}\n\n"

        result += "INSTANCE:\n"
        result += f"agents use reach goal: {self.use_reach_goal}\n"
        result += f"agents' number: {len(self.instance.get_paths())}\n"
        result += f"agents' max length: {self.instance.get_time_limit_agents()}\n"

        for i, path in enumerate(self.instance.get_paths()):
            result += f"length agent {i+1}: {len(path.get_sequence())}\n"
            
        result += "\n"

        if not self.new_path:
            result += "No new path found\n\n"
        else:
            result += "NEW PATH:\n"
            result += f"Init: {self.new_path.get_init()}\n"
            result += f"Goal: {self.new_path.get_goal()}\n"
            result += f"Weight: {self.new_path.get_weight()}\n"
            result += f"Max lenght: {self.instance.get_max()+1}\n"
            result += f"Lenght: {len(self.new_path.get_sequence())}\n"
            result += f"Open lenght: {len(self.nodeDict)}\n"
            result += f"Closed lenght: {len(self.closed)}\n"
            result += f"Wait moves: {self.wait_counter}\n"
            result += f"Sequence: {self.new_path.get_sequence()}\n\n"

        result += "TIME AND MEMORY:\n"
        result += f"total time: {self.total_time} seconds\n"
        result += f"total memory: {self.peak_memory} MB\n"

        return result


    
