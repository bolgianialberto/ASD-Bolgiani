from collections import defaultdict
from math import sqrt

class Path:
    def __init__ (self, init, goal):
        self.init = init
        self.goal = goal
        self.weight = 0
        self.sequence = {}

    def add_node(self, t, node, weight = 0):
        self.sequence[t] = node
        self.weight += weight

    def set_sequence(self, sequence):
        self.sequence = sequence
    
    def get_sequence(self):
        return self.sequence

    def get_init(self):
        return self.init
    
    def get_goal(self):
        return self.goal
    
    def set_goal(self, goal):
        self.goal = goal

    def get_weight(self):
        return self.weight
    
    def set_weight(self, weight):
        self.weight = weight

    def is_path_ended(self, t):
        return t in self.sequence
     
    # collisione con altri path -> allo stesso tempo hanno lo stesso nodo
    def collide_at_same_time(self, next_other,  t):
        return self.sequence[t] == next_other

    # incrocio con altri path -> al tempo t-1 uno è in a e l'altro in b e al tempo t uno è in b e l'altro in a
    def collide_place_exchange(self, current_other, next_other, t):
        if self.sequence.get(t-1, None) and self.sequence.get(t, None):
            return self.sequence[t-1] == next_other and self.sequence[t] == current_other
        return True

    # passa su un goal -> al tempo t il percorso p è finito e il nodo è il goal di p
    def is_collision_free(self, current, next, t):
        return not self.collide_at_same_time(next, t) and not self.collide_place_exchange(current, next, t)

    @staticmethod
    def is_move_good(current, next, paths, t):
        for path in paths:
            ended = not path.is_path_ended(t)
            if (ended and current == path.get_goal()) or (not ended and not path.is_collision_free(current, next, t)):
                return False
        
        return True

    @staticmethod
    def remove_unreachable_moves(current, available_moves, paths, t):
        # available_moves è un set di vicini di un nodo
        available_moves = [next for next in available_moves if Path.is_move_good(current, next, paths, t)]

    @staticmethod
    def get_nsew_moves():
        return [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    @staticmethod
    def get_diagonal_moves():
        return [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    @staticmethod
    def get_still_move():
        return [(0, 0)]
    
    @staticmethod
    def get_all_moves():
        return Path.get_nsew_moves() + Path.get_diagonal_moves() + Path.get_still_move()
    
    @staticmethod
    def get_nsew_still_weight():
        return 1
    
    @staticmethod
    def get_still_weight():
        return 1
    
    @staticmethod
    def get_nswe_weight():
        return 1
    
    @staticmethod
    def get_diagonal_weight():
        return sqrt(2)

    def print_path(self):
        print("Path")
        print("Init: " + str(self.init))
        print("Goal: " + str(self.goal))
        print("Weight: " + str(self.weight))
        t = 0
        while t < len(self.sequence):
            print(str(t) + ": " + str(self.sequence[t]))
            t += 1