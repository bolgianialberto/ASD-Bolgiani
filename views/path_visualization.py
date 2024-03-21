import pygame
import random

BLACK = (0, 0, 0)

GREEN = (0, 255, 0)
AQUA = (0, 255, 255)
MAGENTA = (255, 0, 255)

RED = (255, 0, 0)

COLORS = [AQUA, GREEN, MAGENTA]

# TODO: mettere la cell size solo in una parte
CELL_SIZE = 20

def print_gui_paths(paths, screen):
    # Draw the paths
    for path in paths:
        color = random.choice(COLORS)
        
        for vertex in path.get_sequence():
            row, col = vertex
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1) 

def print_gui_path(path, screen):
    # Draw the path
    color = RED
    
    for vertex in path.get_sequence():
        row, col = vertex
        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)