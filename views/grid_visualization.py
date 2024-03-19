import pygame
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

GREEN = (0, 255, 0)
AQUA = (0, 255, 255)
MAGENTA = (255, 0, 255)

RED = (255, 0, 0)


COLORS = [AQUA, GREEN, MAGENTA]

def print_gui_grid(grid, screen):
    obstacles = grid.get_obstacles()

    rows = grid.get_rows()
    cols = grid.get_cols()

    # Draw the grid
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * 20, row * 20, 20, 20)
            if (row, col) not in obstacles:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

            # Draw the black lines between the cells
            pygame.draw.line(screen, BLACK, (col * 20, row * 20), ((col + 1) * 20, row * 20), 1)
            pygame.draw.line(screen, BLACK, (col * 20, row * 20), (col * 20, (row + 1) * 20), 1)

    # Draw additional black lines for the last row and last column
    for col in range(cols):
        pygame.draw.line(screen, BLACK, (col * 20, rows * 20), ((col + 1) * 20, rows * 20), 1)
    for row in range(rows):
        pygame.draw.line(screen, BLACK, (cols * 20, row * 20), (cols * 20, (row + 1) * 20), 1)

def print_instance_gui(instance):
    grid = instance.get_grid()
    paths = instance.get_paths()

    rows = grid.get_rows()
    cols = grid.get_cols()

    # Initialize pygame
    pygame.init()

    # Set up the display
    screen_width = cols * 20
    screen_height = rows * 20
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Instance GUI")

    # Draw the grid
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * 20, row * 20, 20, 20)
            if (row, col) not in grid.get_obstacles():
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)
            # Disegna le righe nere tra le celle
            pygame.draw.line(screen, BLACK, (col * 20, row * 20), ((col + 1) * 20, row * 20), 1)
            pygame.draw.line(screen, BLACK, (col * 20, row * 20), (col * 20, (row + 1) * 20), 1)

    # Draw the paths
    for path in paths:
        color = random.choice(COLORS)
        COLORS.remove(color)
        
        for i, vertex in enumerate(path.get_sequence()):
            row, col = vertex
            rect = pygame.Rect(col * 20, row * 20, 20, 20)

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1) 

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()