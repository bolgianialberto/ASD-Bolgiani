import heapq
from algorithm.heuristics import diagonal_distance
from algorithm.reconstruct_path import reconstruct_path
from models.node import Node
from models.path import Path

def compute_h(v, goal):
    return diagonal_distance(v, goal)

def reach_goal(graph, init, goal, paths, last_time_goal_passed, time_limit):
    open_heap = []
    open_set = set()

    closed = set()

    nodeDict = {}
    first_h = compute_h(init, goal)
    nodeDict[(init, 0)] = Node(init, 0, None, first_h, first_h, 0)

    heapq.heappush(open_heap, nodeDict[(init, 0)])
    open_set.add((init, 0))

    while open_heap:
        current_node = heapq.heappop(open_heap)
        open_set.remove((current_node.vertex, current_node.time))

        v = current_node.vertex
        t = current_node.time
       
        closed.add((v, t))

        if v == goal and t > last_time_goal_passed:
            goal_node = current_node
            p = reconstruct_path(init, goal_node, t)
            return p, nodeDict, closed
        
        if t < time_limit:
            available_moves = graph.get_neighbors(v)
            moves = Path.remove_unreachable_moves(v, available_moves, paths, t+1)

            for neighbor, weight in moves:
                if (neighbor, t+1) not in closed:
                    neighbor_node = nodeDict.get((neighbor, t+1))

                    if not neighbor_node:
                        neighbor_node = Node(neighbor, t+1, None, 0, 0)
                        nodeDict[(neighbor, t+1)] = neighbor_node   

                    if current_node.g + weight < nodeDict[(neighbor, t+1)].get_g():
                        neighbor_node.set_g(current_node.g + weight)
                        neighbor_node.set_h(compute_h(neighbor, goal))
                        neighbor_node.set_f(neighbor_node.get_g() + neighbor_node.get_h())
                        neighbor_node.set_parent(current_node)
                
                    if (neighbor, t+1) not in open_set:
                        heapq.heappush(open_heap, neighbor_node)
                        open_set.add((neighbor_node.vertex, neighbor_node.time))
        else:
            break
    
    return None, None, None
            