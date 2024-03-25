from controllers.instance_generator import instance_generator
from controllers.grid_generator import grid_generator
from algorithm.reach_goal import reach_goal
from views.grid_visualization import print_gui_grid
from views.path_visualization import print_gui_paths, print_gui_path
import pygame
from tkinter import messagebox

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

WIDTH = 1000
HEIGHT = 700

class Gui():
    
    def __init__(self):
        self.grid = None
        self.instance = None
        self.new_path = None
    
    def run(self, rows, cols, traversability, cluster_factor, n_agents, cell_size):
        global generate_button_clicked
        global add_agents_button_clicked

        generate_button_clicked = False
        add_agents_button_clicked = False

        # Initialize pygame
        pygame.init()

        # Set up the display
        screen_width = WIDTH
        screen_height = HEIGHT 
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Instance GUI")
        screen.fill(WHITE)

        # generate button
        generate_button_rect, add_agents_button_rect, add_new_button_rect = draw_buttons(screen, screen_width, screen_height)

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

                        self.grid = grid_generator(rows, cols, traversability, cluster_factor)
                        # self.instance.print()
                        print_gui_grid(self.grid, screen, cell_size)

                    elif add_agents_button_rect.collidepoint(x, y) and generate_button_clicked and not add_agents_button_clicked:
                        add_agents_button_clicked = True

                        self.instance = instance_generator(self.grid, n_agents)
                        paths = self.instance.get_paths()
                        if not paths:
                            messagebox.showinfo("Attention!", "No paths found! Please generate a new grid.")

                        print_gui_paths(paths, screen, cell_size)

                    elif add_new_button_rect.collidepoint(x, y) and add_agents_button_clicked:
                        self.new_path = reach_goal(self.instance)

                        if self.new_path:
                            print_gui_path(self.new_path, screen, cell_size)
                        else:
                            messagebox.showinfo("Error", "Impossible to find a path!")


            pygame.display.flip()

def draw_buttons(screen, screen_width, screen_height):
    # generate button
    generate_button_rect = pygame.Rect(10, screen_height - 50, 100, 40)
    pygame.draw.rect(screen, GREY, generate_button_rect)
    font = pygame.font.Font(None, 20)
    text = font.render("Generate", True, WHITE)
    text_rect = text.get_rect(center=generate_button_rect.center)
    screen.blit(text, text_rect)

    # add agents button
    add_agents_button_rect = pygame.Rect(120, screen_height - 50, 100, 40)
    pygame.draw.rect(screen, GREY, add_agents_button_rect)
    font = pygame.font.Font(None, 20)
    text = font.render("Add Agents", True, WHITE)
    text_rect = text.get_rect(center=add_agents_button_rect.center)
    screen.blit(text, text_rect)

    # add new button
    add_new_button_rect = pygame.Rect(230, screen_height - 50, 100, 40)
    pygame.draw.rect(screen, GREY, add_new_button_rect)
    font = pygame.font.Font(None, 20)
    text = font.render("Add New", True, WHITE)
    text_rect = text.get_rect(center=add_new_button_rect.center)
    screen.blit(text, text_rect)

    return generate_button_rect, add_agents_button_rect, add_new_button_rect

        