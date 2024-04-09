import heapq
from models.node import Node   
from algorithm.reconstruct_path import reconstruct_path
from algorithm.heuristics import diagonal_distance

# mi serve un dizionario dove salvare i nodi già creati (vertice, tempo) -> nodo
# un vertice è composto da x e y (quindi va bene anche una tupla)
# un nodo è composto da vertice, tempo, parent, f, h, g

#TODO: ma lo controllo se i percorsi precedenti non vanno sul goal del nuovo path? (edit: si ci vanno)
#TODO: ma il nuovo percorso inizia con gli altri???

def reach_goal(instance):
    graph = instance.get_graph()
    init = instance.get_init()
    goal = instance.get_goal()
    paths = instance.get_paths()
    time_new_goal_get_passed = instance.get_time_new_goal_get_passed()
    max_length = instance.get_max()

    # Used when reach_goal mode is activated for the previous paths generation
    if max_length == 0:
        max_length = max_generator(graph, paths)

    current_node = None

    open = []
    closed = set()

    nodeDict = {}
    nodeDict[(init, 0)] = Node(init, 0, None, compute_h(init, goal), compute_h(init, goal), 0)

    heapq.heappush(open, nodeDict[(init, 0)])
            
    while open:
        current_node = heapq.heappop(open)

        v = current_node.vertex
        t = current_node.time
       
        closed.add((v, t))

        if v == goal and t > time_new_goal_get_passed:
            goal_node = current_node
            return reconstruct_path(init, goal_node, t), nodeDict, closed

        if t < max_length:
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
    
    return None, None, None

def max_generator(graph, paths):
    max_length = 0
    # Get the longest path
    for path in paths:
        if len(path.get_sequence()) > max_length:
            max_length = len(path.get_sequence())

    # Add the number of vertexes
    max_length += len(graph.get_linked_vertexes()) 

    return max_length

def compute_h(v, goal):
    return diagonal_distance(v, goal)

# TODO: metterlo solo in una parte del codice e non anche in paths_generator.py
def check_next_vertex(current_vertex, next_vertex, instant, previous_paths):
    for previous in previous_paths:
        previous_sequence = previous.get_sequence()

        if instant < len(previous_sequence):
            if next_vertex == previous_sequence[instant]:
                return False
            if previous_sequence[instant-1] == next_vertex and previous_sequence[instant] == current_vertex:
                return False
        else:
            # if the next vertex is the goal of another path
            if next_vertex == previous.get_goal():
                return False
    
    return True