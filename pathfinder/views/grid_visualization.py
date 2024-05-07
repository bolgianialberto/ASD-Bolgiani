import pygame

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def print_gui_grid(grid, screen, cell_size, padding_left, padding_top):
    starting_point = padding_left + 20

    obstacles = grid.get_obstacles()

    rows = grid.get_rows()
    cols = grid.get_cols()

    screen.fill(WHITE)

    # Draw the grid
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(starting_point+ col * cell_size, padding_top + row * cell_size, cell_size, cell_size)
            if (row, col) not in obstacles:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

            # Draw the black lines between the cells
            pygame.draw.line(screen, BLACK, (starting_point + col * cell_size, padding_top + row * cell_size), (starting_point + (col + 1) * cell_size, padding_top + row * cell_size), 1)
            pygame.draw.line(screen, BLACK, (starting_point + col * cell_size, padding_top + row * cell_size), (starting_point + col * cell_size, padding_top + (row + 1) * cell_size), 1)

    # Draw additional black lines for the last row and last column
    for col in range(cols):
        pygame.draw.line(screen, BLACK, (starting_point + col * cell_size, padding_top + rows * cell_size), (starting_point + (col + 1) * cell_size, padding_top + rows * cell_size), 1)
    for row in range(rows):
        pygame.draw.line(screen, BLACK, (starting_point + cols * cell_size, padding_top + row * cell_size), (starting_point + cols * cell_size, padding_top +  (row + 1) * cell_size), 1)
