import math
import heapq
from controllers.paths_generator import check_next_vertex   
from models.node import Node   
from models.path import Path  

def reach_goal(instance):
    graph = instance.get_graph()
    linked_vertexes = graph.get_linked_vertexes()
    paths = instance.get_paths()
    init = instance.get_init()
    goal = instance.get_goal()
    max = instance.get_max()
    current_node = None

    # Create initial node
    init_node = Node(init[0], init[1], 0)

    # Initialize g(init, 0) = 0 
    init_node.set_g(0)

    # Initialize f(init, 0) = h(init, goal)
    h = compute_h(init, goal)
    init_node.set_h(h)
    init_node.set_f(h)

    # # Create goal node
    # goal_node = Node(goal[0], goal[1], 0)

    # Define Closed = []
    closed = set()

    # Define Open = [(init, 0)]
    open = []
    heapq.heappush(open, init_node)
            
    while open:
        previous_node = current_node

        # Get the vertex with the lowest f
        current_node = heapq.heappop(open)

        # Get the vertex and the instant
        v = (current_node.x, current_node.y)
        t = current_node.time
       
        # Add (v, t) to Closed
        closed.add(current_node)

        if v == goal:
            goal_node = current_node

            # Create the path
            result_path = Path(init, goal)
            result_path.set_sequence(reconstruct_path(goal_node))
            result_path.set_weight(goal_node.get_g())

            return result_path

        if t < max:
            # Get the neighbors of v
            neighbors = get_neighbors(v, linked_vertexes, t)

            for neighbor, weight in neighbors:
                if neighbor not in closed:
                    traversable = True

                    # Check if there are conflicts
                    next = (neighbor.x, neighbor.y)
                    if not check_next_vertex(v, next, t+1, paths):
                        traversable = False
                    
                    if traversable:
                        if current_node.g + weight < neighbor.g:
                            neighbor.set_g(current_node.g + weight)
                            neighbor.set_h(compute_h(next, goal))
                            neighbor.set_f(neighbor.g + neighbor.h)
                            neighbor.set_parent(current_node)
                    
                        if neighbor not in open:
                            # Add (n, t+1) to Open
                            heapq.heappush(open, neighbor)
    return None

def compute_h(v, goal):
    return diagonal_distance(v, goal)

def diagonal_distance(v, goal):
    dx = abs(v[0] - goal[0])
    dy = abs(v[1] - goal[1])
    D = 1  
    D2 = math.sqrt(2) 
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

def get_lowest_f(f, open):
    lowest = math.inf
    vertex = None
    instant = None
    for v, t in open:
        if f[(v, t)] < lowest:
            lowest = f[(v, t)]
            vertex = v
            instant = t
    return vertex, instant

def reconstruct_path(goal):
    path = []
    current = goal
    while current.parent:
        path.append((current.x, current.y))
        current = current.parent
    path.append((current.x, current.y))

    return path[::-1]

def get_neighbors(v, linked_vertexes, time):
    neighbors = []
    for n, w in linked_vertexes[v]:
        new_node = Node(n[0], n[1], time+1)
        neighbors.append((new_node, w))

    return neighbors

