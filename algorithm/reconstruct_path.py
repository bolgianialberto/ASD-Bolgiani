from models.path import Path

def reconstruct_path(init, goal_node, t_end):
    result_path = Path(init, goal_node.vertex)
    result_path.set_weight(goal_node.get_g())

    current = goal_node
    t = t_end

    while current.parent:
        result_path.add_node(t, current.vertex)
        current = current.parent
        t -= 1
    
    result_path.add_node(t, current.vertex)
    
    return result_path
