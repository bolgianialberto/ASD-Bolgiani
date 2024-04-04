from collections import defaultdict
from math import sqrt

class Path:
    def __init__ (self, init, goal):
        self.init = init
        self.goal = goal
        self.weight = 0
        self.sequence = defaultdict(tuple)

    def is_path_ended(self, t):
        return t in self.sequence
    
    # has to wait se è arrivato al goal ma qualcuno passa per il goal dopo 
    def has_to_wait(self, t, max_t):
        return t < max_t
    
    # collisione con altri path -> allo stesso tempo hanno lo stesso nodo
    def collide_at_same_time(self, t, path):
        return self.sequence[t] == path.get_sequence()[t]

    # incrocio con altri path -> al tempo t-1 uno è in a e l'altro in b e al tempo t uno è in b e l'altro in a

    # passa su un goal -> al tempo t il percorso p è finito e il nodo è il goal di p

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

    def __str__(self):
        res = "Path\n"
        res += "Init: " + str(self.init) + "\n"
        res += "Goal: " + str(self.goal) + "\n"
        res += "Weight: " + str(self.weight) + "\n"
        res += "Sequence: " + str(self.sequence) + "\n"
        return res