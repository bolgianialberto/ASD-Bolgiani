import math

def diagonal_distance(v, goal):
    dx = abs(v[0] - goal[0])
    dy = abs(v[1] - goal[1])
    D = 1  
    D2 = math.sqrt(2) 
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)