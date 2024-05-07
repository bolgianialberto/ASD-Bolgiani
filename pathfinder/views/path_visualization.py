import pygame
import random

BLACK = (0, 0, 0)

GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (220, 165, 0)
BROWN = (165, 42, 42)
NAVY = (0, 0, 128)
INDIGO = (75, 0, 130)
DARK_GREEN = (0, 100, 0)
OLIVE = (128, 128, 0)
DARK_CYAN = (0, 128, 128)
DARK_MAGENTA = (128, 0, 128)


COLORS = [GREEN, MAGENTA, BLUE, PURPLE, ORANGE, BROWN, NAVY, INDIGO, DARK_GREEN, OLIVE, DARK_CYAN, DARK_MAGENTA]

RED = (255, 0, 0)

def print_gui_paths(paths, screen, cell_size, padding_left, padding_top):
    # Draw the paths
    for path in paths:
        color = random.choice(COLORS)
        print_gui_path(path, screen, cell_size, padding_left, padding_top, color)

def print_gui_path(path, screen, cell_size, padding_left, padding_top, color = RED):
    starting_point = padding_left + 20

    sequence = path.get_sequence()

    start_point = sequence[0]
    start_pixel = (starting_point + start_point[1] * cell_size + cell_size // 2, padding_top + start_point[0] * cell_size + cell_size // 2)
    pygame.draw.circle(screen, color, start_pixel, cell_size // 3) 

    for i in range(len(sequence) - 1):
        start_point = sequence[i]
        end_point = sequence[i+1]
        start_pixel = (starting_point + start_point[1] * cell_size + cell_size // 2, padding_top + start_point[0] * cell_size + cell_size // 2)
        end_pixel = (starting_point + end_point[1] * cell_size + cell_size // 2, padding_top + end_point[0] * cell_size + cell_size // 2)
        pygame.draw.line(screen, color, start_pixel, end_pixel, 3)

    end_point = sequence[len(sequence) - 1]
    end_pixel = (starting_point + end_point[1] * cell_size + cell_size // 2, padding_top + end_point[0] * cell_size + cell_size // 2)
    pygame.draw.polygon(screen, color, [(end_pixel[0], end_pixel[1] - cell_size // 3), 
                                         (end_pixel[0] + cell_size // 5, end_pixel[1] + cell_size // 5),
                                         (end_pixel[0] - cell_size // 5, end_pixel[1] + cell_size // 5)], 3)