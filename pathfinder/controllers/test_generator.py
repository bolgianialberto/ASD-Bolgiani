import matplotlib.pyplot as plt
from controllers.profile_generator import Profile
from controllers.instance_generator import instance_generator
from controllers.grid_generator import grid_generator
from models.path import Path
from algorithm.reach_goal import reach_goal
import numpy as np

class Automated_test:
    def __init__(self, rows, cols, traversability, cluster_factor, n_agents, use_reach_goal):
        self.rows = rows
        self.cols = cols
        self.traversability = traversability
        self.cluster_factor = cluster_factor
        self.n_agents = n_agents
        self.use_reach_goal = use_reach_goal

        self.results = []

    def test_grid_generator(self, min_size_d, max_size_d, step_d, min_size_cf, max_size_cf, step_cf, min_size_t, max_size_t, step_t):
        # dimensions = list(range(min_size_d, max_size_d+1, step_d))
        # time_per_dimension = []
        # memory_per_dimension = []
        profile = Profile()
        # cluster_factor = 0.3
        # traversability = 0.7
        
        # # Test al variare della dimensione
        # for dimension in dimensions:
        #     total_elapsed_time = 0
        #     total_memory_used = 0
        
        #     for _ in range(10):
        #         profile.start_screening()
        #         grid_generator(dimension, dimension, traversability, cluster_factor)
        #         profile.stop_screening()

        #         total_elapsed_time += profile.total_time
        #         total_memory_used += profile.peak_memory
            
        #     average_elapsed_time = total_elapsed_time / 10
        #     average_memory_used = total_memory_used / 10

        #     time_per_dimension.append(average_elapsed_time)
        #     memory_per_dimension.append(average_memory_used)

        #     print(f"Dimension: {dimension}x{dimension} - Average time: {average_elapsed_time:.2f}s - Average memory: {average_memory_used:.2f}KB")
        
        # # Plot del tempo in base alle dimensioni
        # plt.figure(figsize=(10, 5))
        # plt.plot(dimensions, time_per_dimension, marker='o', linestyle='-')
        # plt.title('Grid Generator Test Results')
        # plt.suptitle('Tempo in base alle dimensioni')
        # plt.xlabel('Dimensione')
        # plt.ylabel('Tempo medio (s)')
        # plt.grid(True)
        # plt.show()

        # # Plot della memoria in base alle dimensioni
        # plt.figure(figsize=(10, 5))
        # plt.plot(dimensions, memory_per_dimension, marker='o', linestyle='-')
        # plt.title('Grid Generator Test Results')
        # plt.suptitle('Memoria in base alle dimensioni')
        # plt.xlabel('Dimensione')
        # plt.ylabel('Memoria media (KB)')
        # plt.grid(True)
        # plt.show()

        # Test al variare di traversability con dimensione e cluster factor fissi
        # traversabilities = np.arange(min_size_t, max_size_t + step_t, step_t)
        # time_per_traversability = []
        # memory_per_traversability = []

        # dimension = 100
        # cluster_factor = 0.3

        # for traversability in traversabilities:
        #     total_elapsed_time = 0
        #     total_memory_used = 0
            
        #     for _ in range(10):
        #         profile.start_screening()
        #         grid_generator(dimension, dimension, traversability, cluster_factor)
        #         profile.stop_screening()
                
        #         total_elapsed_time += profile.total_time
        #         total_memory_used += profile.peak_memory
            
        #     average_elapsed_time = total_elapsed_time / 10
        #     average_memory_used = total_memory_used / 10
            
        #     time_per_traversability.append(average_elapsed_time)
        #     memory_per_traversability.append(average_memory_used)
            
        #     print(f"Traversability: {traversability:.2f} - Average time: {average_elapsed_time:.2f}s - Average memory: {average_memory_used:.2f}KB")

        # # Plot del tempo in base alla traversability
        # plt.figure(figsize=(10, 5))
        # plt.plot(traversabilities, time_per_traversability, marker='o', linestyle='-')
        # plt.title('Grid Generator Test Results')
        # plt.suptitle('Tempo in base alla free cell ratio')
        # plt.xlabel('Free cell ratio')
        # plt.ylabel('Tempo medio (s)')
        # plt.grid(True)
        # plt.show()

        # # Plot della memoria in base alla traversability
        # plt.figure(figsize=(10, 5))
        # plt.plot(traversabilities, memory_per_traversability, marker='o', linestyle='-')
        # plt.title('Grid Generator Test Results')
        # plt.suptitle('Memoria in base alla free cell ratio')
        # plt.xlabel('Free cell ratio')
        # plt.ylabel('Memoria media (KB)')
        # plt.grid(True)
        # plt.show()

        # Test al variare del cluster factor con dimensione e traversability fissi
        cluster_factors = np.arange(min_size_cf, max_size_cf + step_cf, step_cf)
        time_per_cluster_factor = []
        memory_per_cluster_factor = []

        dimension = 100
        traversability = 0.7

        for cluster_factor in cluster_factors:
            total_elapsed_time = 0
            total_memory_used = 0
            
            for _ in range(10):
                profile.start_screening()
                grid_generator(dimension, dimension, traversability, cluster_factor)
                profile.stop_screening()
                
                total_elapsed_time += profile.total_time
                total_memory_used += profile.peak_memory
            
            average_elapsed_time = total_elapsed_time / 10
            average_memory_used = total_memory_used / 10
            
            time_per_cluster_factor.append(average_elapsed_time)
            memory_per_cluster_factor.append(average_memory_used)
            
            print(f"Cluster Factor: {cluster_factor:.2f} - Average time: {average_elapsed_time:.2f}s - Average memory: {average_memory_used:.2f}KB")

        # Plot del tempo in base al cluster factor
        plt.figure(figsize=(10, 5))
        plt.plot(cluster_factors, time_per_cluster_factor, marker='o', linestyle='-')
        plt.title('Grid Generator Test Results')
        plt.suptitle('Tempo in base al cluster factor')
        plt.xlabel('Cluster Factor')
        plt.ylabel('Tempo medio (s)')
        plt.grid(True)
        plt.show()

        # Plot della memoria in base al cluster factor
        plt.figure(figsize=(10, 5))
        plt.plot(cluster_factors, memory_per_cluster_factor, marker='o', linestyle='-')
        plt.title('Grid Generator Test Results')
        plt.suptitle('Memoria in base al cluster factor')
        plt.xlabel('Cluster Factor')
        plt.ylabel('Memoria media (KB)')
        plt.grid(True)
        plt.show()

    def test_instance_generator(self, min_size_d, max_size_d, step_d, min_size_n, max_size_n, step_n):
        # dimensions = list(range(min_size_d, max_size_d+1, step_d))
        profile = Profile()
        # traversability = 0.7
        # cluster_factor = 0.3

        # for use_reach_goal in [False, True]:
        #     time_per_dimension = []
        #     memory_per_dimension = []

        #     for dimension in dimensions:
        #         total_elapsed_time = 0
        #         total_memory_used = 0
        #         rows = cols = dimension

        #         for _ in range(10):  
        #             grid = grid_generator(rows, cols, traversability, cluster_factor)
        #             profile.start_screening()
        #             instance = instance_generator(grid, self.n_agents, use_reach_goal)
        #             profile.stop_screening()
                    
        #             total_elapsed_time += profile.total_time
        #             total_memory_used += profile.peak_memory

        #         average_elapsed_time = total_elapsed_time / 10
        #         average_memory_used = total_memory_used / 10
        #         time_per_dimension.append(average_elapsed_time)
        #         memory_per_dimension.append(average_memory_used)

        #         print(f"Dimension: {dimension}x{dimension}, use_reach_goal: {use_reach_goal} - Average time: {average_elapsed_time:.2f}s - Average memory: {average_memory_used:.2f}KB - N. agents: {len(instance.paths)}")

        #     # Plot del tempo in base alle dimensioni
        #     plt.figure(figsize=(10, 5))
        #     plt.plot(dimensions, time_per_dimension, marker='o', linestyle='-')
        #     plt.title('Instance Generator Test Results')
        #     plt.suptitle(f'Tempo in base alle dimensioni (use_reach_goal={use_reach_goal})')
        #     plt.xlabel('Dimensione')
        #     plt.ylabel('Tempo medio (s)')
        #     plt.grid(True)
        #     plt.show()

        #     # Plot della memoria in base alle dimensioni
        #     plt.figure(figsize=(10, 5))
        #     plt.plot(dimensions, memory_per_dimension, marker='o', linestyle='-')
        #     plt.title('Instance Generator Test Results')
        #     plt.suptitle(f'Memoria in base alle dimensioni (use_reach_goal={use_reach_goal})')
        #     plt.xlabel('Dimensione')
        #     plt.ylabel('Memoria media (KB)')
        #     plt.grid(True)
        #     plt.show()

        # Test al variare del numero di agenti con dimensione fissi
        n_agents = np.arange(min_size_n, max_size_n + step_n, step_n)
        time_per_n_agents = []
        memory_per_n_agents = []
        real_agents_number = []

        dimension = 100
        cluster_factor = 0.3
        traversability = 0.7

        for use_reach_goal in [True]:
            for n_agent in n_agents:
                total_elapsed_time = 0
                total_memory_used = 0
                total_n_agents_length = 0

                for _ in range(10):
                    grid = grid_generator(dimension, dimension, traversability, cluster_factor)
                    profile.start_screening()
                    instance = instance_generator(grid, n_agent, use_reach_goal)
                    profile.stop_screening()
                    
                    total_elapsed_time += profile.total_time
                    total_memory_used += profile.peak_memory
                    total_n_agents_length += len(instance.paths)

                average_elapsed_time = total_elapsed_time / 10
                average_memory_used = total_memory_used / 10
                average_n_agents_length = total_n_agents_length / 10
                time_per_n_agents.append(average_elapsed_time)
                memory_per_n_agents.append(average_memory_used)
                real_agents_number.append(average_n_agents_length)

                print(f"N. agents: {len(instance.paths)} -UseReachGoal: {use_reach_goal} -Average time: {average_elapsed_time:.2f}s - Average memory: {average_memory_used:.2f}KB - N. agents: {average_n_agents_length}")

            # Plot del tempo in base al numero di agenti
            plt.figure(figsize=(10, 5))
            plt.plot(n_agents, time_per_n_agents, marker='o', linestyle='-')
            for i, txt in enumerate(real_agents_number):
                plt.annotate(f'{txt:.1f}', (n_agents[i], time_per_n_agents[i]), textcoords="offset points", xytext=(0,10), ha='center')
            plt.title('Instance Generator Test Results')
            plt.suptitle(f'Tempo in base al numero di agenti (use_reach_goal={use_reach_goal})')
            plt.xlabel('N. agents')
            plt.ylabel('Tempo medio (s)')
            plt.grid(True)
            plt.show()

            # Plot della memoria in base al numero di agenti
            plt.figure(figsize=(10, 5))
            plt.plot(n_agents, memory_per_n_agents, marker='o', linestyle='-')
            for i, txt in enumerate(real_agents_number):
                plt.annotate(f'{txt:.1f}', (n_agents[i], memory_per_n_agents[i]), textcoords="offset points", xytext=(0,10), ha='center')
            plt.title('Instance Generator Test Results')
            plt.suptitle(f'Memoria in base al numero di agenti (use_reach_goal={use_reach_goal})')
            plt.xlabel('N. agents')
            plt.ylabel('Memoria media (KB)')
            plt.grid(True)
            plt.show()

    def test_reach_goal(self, min_size_d, max_size_d, step_d, min_size_n, max_size_n, step_n):
        profile = Profile()
        traversability = 0.7
        cluster_factor = 0.3
        use_reach_goal = False

        dimensions = list(range(min_size_d, max_size_d + 1, step_d))
        time_per_dimension = []
        memory_per_dimension = []
        wait_moves_per_dimension = []

        for dimension in dimensions:
            total_elapsed_time = 0
            total_memory_used = 0
            total_wait_moves = 0
            valid_runs = 0
            rows = cols = dimension

            for _ in range(10):
                grid = grid_generator(rows, cols, traversability, cluster_factor)
                instance = instance_generator(grid, self.n_agents, use_reach_goal)

                profile.start_screening()
                new_path, _, _ = reach_goal(
                    instance.get_graph(),
                    instance.get_init(),
                    instance.get_goal(),
                    instance.get_paths(),
                    instance.get_goals_init_last_instant(),
                    instance.get_max()
                )
                profile.stop_screening()

                if new_path:
                    total_elapsed_time += profile.total_time
                    total_memory_used += profile.peak_memory
                    total_wait_moves += profile.count_wait_moves(new_path)
                    valid_runs += 1

            if valid_runs > 0:
                average_elapsed_time = total_elapsed_time / valid_runs
                average_memory_used = total_memory_used / valid_runs
                average_wait_moves = total_wait_moves / valid_runs
            else:
                average_elapsed_time = float('nan')
                average_memory_used = float('nan')
                average_wait_moves = float('nan')

            time_per_dimension.append(average_elapsed_time)
            memory_per_dimension.append(average_memory_used)
            wait_moves_per_dimension.append(average_wait_moves)

            print(f"Dimension: {dimension}x{dimension}, use_reach_goal: {use_reach_goal} - Average time: {average_elapsed_time:.2f}s - Average memory: {average_memory_used:.2f}KB - Average wait moves: {average_wait_moves:.2f}")

        # Plot del tempo in base alle dimensioni
        plt.figure(figsize=(10, 5))
        plt.plot(dimensions, time_per_dimension, marker='o', linestyle='-')
        plt.suptitle(f'Tempo in base alle dimensioni (use_reach_goal={use_reach_goal})')
        plt.title('Reach Goal Test Results')
        plt.xlabel('Dimensione')
        plt.ylabel('Tempo medio (s)')
        plt.grid(True)
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Aggiusta la spaziatura
        plt.show()

        # Plot della memoria in base alle dimensioni
        plt.figure(figsize=(10, 5))
        plt.plot(dimensions, memory_per_dimension, marker='o', linestyle='-')
        plt.suptitle(f'Memoria in base alle dimensioni (use_reach_goal={use_reach_goal})')
        plt.title('Reach Goal Test Results')
        plt.xlabel('Dimensione')
        plt.ylabel('Memoria media (KB)')
        plt.grid(True)
        plt.show()

        # Plot delle wait moves in base alle dimensioni
        plt.figure(figsize=(10, 5))
        plt.plot(dimensions, wait_moves_per_dimension, marker='o', linestyle='-')
        plt.suptitle(f'Wait moves in base alle dimensioni (use_reach_goal={use_reach_goal})')
        plt.title('Reach Goal Test Results')
        plt.xlabel('Dimensione')
        plt.ylabel('Wait moves medie')
        plt.grid(True)
        plt.show()

        # Test al variare del numero di agenti
        dimension = 100
        n_agents = list(range(min_size_n, max_size_n + 1, step_n))
        time_per_n_agents = []
        memory_per_n_agents = []
        wait_moves_per_n_agents = []

        for n_agent in n_agents:
            total_elapsed_time = 0
            total_memory_used = 0
            total_wait_moves = 0
            valid_runs = 0

            for _ in range(10):
                grid = grid_generator(dimension, dimension, traversability, cluster_factor)
                instance = instance_generator(grid, n_agent, use_reach_goal)

                profile.start_screening()
                new_path, _, _ = reach_goal(
                    instance.get_graph(),
                    instance.get_init(),
                    instance.get_goal(),
                    instance.get_paths(),
                    instance.get_goals_init_last_instant(),
                    instance.get_max()
                )
                profile.stop_screening()

                if new_path:
                    total_elapsed_time += profile.total_time
                    total_memory_used += profile.peak_memory
                    total_wait_moves += profile.count_wait_moves(new_path)
                    valid_runs += 1

            if valid_runs > 0:
                average_elapsed_time = total_elapsed_time / valid_runs
                average_memory_used = total_memory_used / valid_runs
                average_wait_moves = total_wait_moves / valid_runs
            else:
                average_elapsed_time = float('nan')
                average_memory_used = float('nan')
                average_wait_moves = float('nan')

            time_per_n_agents.append(average_elapsed_time)
            memory_per_n_agents.append(average_memory_used)
            wait_moves_per_n_agents.append(average_wait_moves)

            print(f"N. agents: {n_agent} - Average time: {average_elapsed_time:.2f}s - Average memory: {average_memory_used:.2f}KB - Average wait moves: {average_wait_moves:.2f}")

        # Plot del tempo in base al numero di agenti
        plt.figure(figsize=(10, 5))
        plt.plot(n_agents, time_per_n_agents, marker='o', linestyle='-')
        plt.suptitle(f'Tempo in base al numero di agenti (use_reach_goal={use_reach_goal})')
        plt.title('Reach Goal Test Results')
        plt.xlabel('Numero di agenti')
        plt.ylabel('Tempo medio (s)')
        plt.grid(True)
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Aggiusta la spaziatura
        plt.show()

        # Plot della memoria in base al numero di agenti
        plt.figure(figsize=(10, 5))
        plt.plot(n_agents, memory_per_n_agents, marker='o', linestyle='-')
        plt.suptitle(f'Memoria in base al numero di agenti (use_reach_goal={use_reach_goal})')
        plt.title('Reach Goal Test Results')
        plt.xlabel('Numero di agenti')
        plt.ylabel('Memoria media (KB)')
        plt.grid(True)
        plt.show()

        # Plot delle wait moves in base al numero di agenti
        plt.figure(figsize=(10, 5))
        plt.plot(n_agents, wait_moves_per_n_agents, marker='o', linestyle='-')
        plt.suptitle(f'Wait moves in base al numero di agenti (use_reach_goal={use_reach_goal})')
        plt.title('Reach Goal Test Results')
        plt.xlabel('Numero di agenti')
        plt.ylabel('Wait moves medie')
        plt.grid(True)
        plt.show()



        