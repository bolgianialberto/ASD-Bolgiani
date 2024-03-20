import pygame

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CELL_SIZE = 20

def print_gui_grid(grid, screen):
    obstacles = grid.get_obstacles()

    rows = grid.get_rows()
    cols = grid.get_cols()

    # Draw the grid
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if (row, col) not in obstacles:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

            # Draw the black lines between the cells
            pygame.draw.line(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE), ((col + 1) * CELL_SIZE, row * CELL_SIZE), 1)
            pygame.draw.line(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE), (col * CELL_SIZE, (row + 1) * CELL_SIZE), 1)

    # Draw additional black lines for the last row and last column
    for col in range(cols):
        pygame.draw.line(screen, BLACK, (col * CELL_SIZE, rows * CELL_SIZE), ((col + 1) * CELL_SIZE, rows * CELL_SIZE), 1)
    for row in range(rows):
        pygame.draw.line(screen, BLACK, (cols * CELL_SIZE, row * CELL_SIZE), (cols * CELL_SIZE, (row + 1) * CELL_SIZE), 1)
