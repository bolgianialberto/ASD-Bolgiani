from models.path import Path

def reconstruct_path(init, goal_node, goals_last_instant):
    result_path = Path(init, goal_node.vertex)
    result_path.set_weight(goal_node.get_g())

    sequence = []
    current = goal_node
    while current.parent:
        update_goals_last_instant(goals_last_instant, current.vertex, current.time)
        sequence.append(current.vertex)
        current = current.parent
    sequence.append(current.vertex)

    Path.set_goal_last_instant(goals_last_instant)

    result_path.set_sequence(sequence[::-1])
    
    return result_path

def update_goals_last_instant(goals_last_instant, vertex, time):
    if vertex in goals_last_instant:
        goals_last_instant[vertex] = time