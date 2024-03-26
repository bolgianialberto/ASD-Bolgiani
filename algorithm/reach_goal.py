import heapq
from models.node import Node   
from models.path import Path 
from algorithm.heuristics import diagonal_distance

# mi serve un dizionario dove salvare i nodi già creati (vertice, tempo) -> nodo
# un vertice è composto da x e y (quindi va bene anche una tupla)
# un nodo è composto da vertice, tempo, parent, f, h, g

#TODO: ma lo controllo se i percorsi precedenti non vanno sul goal del nuovo path? (edit: si ci vanno)
#TODO: ma il nuovo percorso inizia con gli altri???

def reach_goal(graph, init, goal, paths, goals_last_instant, max = 0):
    if max == 0:
        max = max_generator(graph, paths)

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

        if v == goal and t > goals_last_instant[goal]:
            goal_node = current_node

            # Create the path
            result_path = Path(init, goal)
            result_path.set_sequence(reconstruct_path(goal_node, goals_last_instant))
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

def max_generator(graph, paths):
    max = 0
    # Get the longest path
    for path in paths:
        if len(path.get_sequence()) > max:
            max = len(path.get_sequence())

    # Add the number of vertexes
    max += len(graph.vertexes) 

    return max


def compute_h(v, goal):
    return diagonal_distance(v, goal)

def reconstruct_path(goal, goals_last_instant):
    path = []
    current = goal
    while current.parent:
        update_goals_last_instant(goals_last_instant, current.vertex, current.time)
        path.append(current.vertex)
        current = current.parent
    path.append(current.vertex)

    Path.set_goal_last_instant(goals_last_instant)

    return path[::-1]

def update_goals_last_instant(goals_last_instant, vertex, time):
    if vertex in goals_last_instant:
        goals_last_instant[vertex] = time

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