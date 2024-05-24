from models.path import Path

def reconstruct_path(init, goal_node, t_end, goals_init_last_instant):
    print("inizio reconstruct_path")
    result_path = Path(init, goal_node.vertex)
    result_path.set_weight(goal_node.get_g())

    current = goal_node

    while current.parent:
        if current.vertex in goals_init_last_instant:
            goals_init_last_instant[current.vertex] = (goals_init_last_instant[current.vertex][0], max(goals_init_last_instant[current.vertex][1], t_end))

        result_path.add_node(t_end, current.vertex)
        current = current.parent
        t_end -= 1
    
    result_path.add_node(t_end, current.vertex)
    
    return result_path
