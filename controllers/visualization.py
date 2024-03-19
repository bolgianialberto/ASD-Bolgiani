import pygame
from views.grid_visualization import print_gui_grid

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

CELL_SIZE = 20

MIN_WIDTH = 340

def print_gui(instance):
    generate_button_clicked = False
    add_agents_button_clicked = True

    grid = instance.get_grid()
    paths = instance.get_paths()

    rows = grid.get_rows()
    cols = grid.get_cols()

    # Initialize pygame
    pygame.init()

    # Set up the display
    screen_width = max(cols * CELL_SIZE, MIN_WIDTH)
    screen_height = rows * CELL_SIZE + 60
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Instance GUI")
    screen.fill(WHITE)

    # generate button
    generate_button_rect = pygame.Rect(10, rows * CELL_SIZE + 10, 100, 40)
    pygame.draw.rect(screen, GREY, generate_button_rect)
    font = pygame.font.Font(None, 20)
    text = font.render("Generate", True, WHITE)
    text_rect = text.get_rect(center=generate_button_rect.center)
    screen.blit(text, text_rect)

    # add agents button
    add_agents_button_rect = pygame.Rect(120, rows * CELL_SIZE + 10, 100, 40)
    pygame.draw.rect(screen, GREY, add_agents_button_rect)
    font = pygame.font.Font(None, 20)
    text = font.render("Add Agents", True, WHITE)
    text_rect = text.get_rect(center=add_agents_button_rect.center)
    screen.blit(text, text_rect)

    # add new button
    add_new_button_rect = pygame.Rect(230, rows * CELL_SIZE + 10, 100, 40)
    pygame.draw.rect(screen, GREY, add_new_button_rect)
    font = pygame.font.Font(None, 20)
    text = font.render("Add New", True, WHITE)
    text_rect = text.get_rect(center=add_new_button_rect.center)
    screen.blit(text, text_rect)

    # Main loop
    while True:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if generate_button_rect.collidepoint(x, y):
                    generate_button_clicked = True
                    add_agents_button_clicked = False
                    print_gui_grid(grid, screen)

        pygame.display.flip()

    