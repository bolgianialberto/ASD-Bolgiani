import heapq
from controllers.paths_generator import check_next_vertex   
from models.node import Node   
from models.path import Path 
from algorithm.heuristics import diagonal_distance

# mi serve un dizionario dove salvare i nodi già creati (vertice, tempo) -> nodo
# un vertice è composto da x e y (quindi va bene anche una tupla)
# un nodo è composto da vertice, tempo, parent, f, h, g

def reach_goal(instance):
    graph = instance.get_graph()
    paths = instance.get_paths()
    init = instance.get_init()
    goal = instance.get_goal()
    max = instance.get_max()
    current_node = None

    open = []
    closed = set()

    nodeDict = {}
    nodeDict[(init, 0)] = Node(init, 0, None, compute_h(init, goal), compute_h(init, goal), 0)

    heapq.heappush(open, nodeDict[(init, 0)])
            
    while open:
        # Get the vertex with the lowest f
        current_node = heapq.heappop(open)

        # Get the vertex and the instant
        v = current_node.vertex
        t = current_node.time
       
        # Add (v, t) to Closed
        closed.add((v, t))

        if v == goal:
            goal_node = current_node

            # Create the path
            result_path = Path(init, goal)
            result_path.set_sequence(reconstruct_path(goal_node))
            result_path.set_weight(goal_node.get_g())

            return result_path

        if t < max:
            # Get the neighbors of v
            neighbors = graph.get_neighbors(v)

            for neighbor, weight in neighbors:
                if (neighbor, t+1) not in closed:
                    traversable = True

                    # Check if there are conflicts
                    if not check_next_vertex(v, neighbor, t+1, paths):
                        traversable = False
                    
                    if traversable:
                        neighbor_node = nodeDict.get((neighbor, t+1))

                        if neighbor_node is None:
                            neighbor_node = Node(neighbor, t+1, None, 0, 0)
                            nodeDict[(neighbor, t+1)] = neighbor_node   

                        if current_node.g + weight < nodeDict[(neighbor, t+1)].get_g():
                            neighbor_node.set_g(current_node.g + weight)
                            neighbor_node.set_h(compute_h(neighbor, goal))
                            neighbor_node.set_f(neighbor_node.get_g() + neighbor_node.get_h())
                            neighbor_node.set_parent(current_node)
                    
                        if neighbor_node not in open:
                            heapq.heappush(open, neighbor_node)
        else:
            break
    
    return None

def compute_h(v, goal):
    return diagonal_distance(v, goal)

def reconstruct_path(goal):
    path = []
    current = goal
    while current.parent:
        path.append(current.vertex)
        current = current.parent
    path.append(current.vertex)

    return path[::-1]


