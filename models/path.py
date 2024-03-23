from math import sqrt

class Path:
    def __init__ (self, init, goal):
        self.init = init
        self.goal = goal
        self.weight = 0
        self.sequence = []

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

    def print(self):
        print("Weight:", self.weight)
        print("Sequence:")
        for instant, move in enumerate(self.sequence):
            print(f"Instant {instant}: {move}")