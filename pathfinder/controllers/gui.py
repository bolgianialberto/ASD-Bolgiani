from controllers.instance_generator import instance_generator
from controllers.grid_generator import grid_generator
from algorithm.reach_goal import reach_goal
from views.grid_visualization import print_gui_grid
from views.path_visualization import print_gui_paths, print_gui_path
from views.checkbox import Checkbox
from controllers.profile_generator import Profile
import pygame
from tkinter import messagebox
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREY = (211, 211, 211)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230) 

WIDTH = 1000
HEIGHT = 700

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 40
PADDING_LEFT = 40
PADDING_TOP = 40

BUTTON_SURFACE_WIDTH = 200

CUSTOM_FONT = 'Roboto-Regular.ttf'

BOX_WIDTH = 50
BOX_HEIGHT = 20

class Gui():
    
    def __init__(self):
        self.grid = None
        self.instance = None
        self.new_path = None
        self.profile = Profile()
    
    def run(self, rows, cols, traversability, cluster_factor, n_agents, cell_size, seed):
        pygame.init()

        # display
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Path Finder")
        screen.fill(WHITE)

        button_surface = pygame.Surface((BUTTON_SURFACE_WIDTH, HEIGHT))
        button_surface.fill(WHITE)
        grid_surface = pygame.Surface((WIDTH - BUTTON_SURFACE_WIDTH, HEIGHT))
        grid_surface.fill(WHITE)

        # variables
        global generate_button_clicked
        global add_agents_button_clicked

        generate_button_clicked = False
        add_agents_button_clicked = False

        rows_input_value = str(rows)
        cols_input_value = str(cols)
        fcr_input_value = str(traversability)
        agglo_input_value = str(cluster_factor)
        na_input_value = str(n_agents)
        seed_input_value = '' if not seed else str(seed)

        rows_active = False
        cols_active = False
        fcr_active = False
        agglo_active = False
        na_active = False
        seed_active = False

        # Input boxes
        rows_input_box_rect = pygame.Rect(PADDING_LEFT + 100, PADDING_TOP, BOX_WIDTH, BOX_HEIGHT)
        cols_input_box_rect = pygame.Rect(PADDING_LEFT + 100, PADDING_TOP + 30, BOX_WIDTH, BOX_HEIGHT)
        fcr_input_box_rect = pygame.Rect(PADDING_LEFT + 100, PADDING_TOP + 60, BOX_WIDTH, BOX_HEIGHT)
        agglo_input_box_rect = pygame.Rect(PADDING_LEFT + 100, PADDING_TOP + 90, BOX_WIDTH, BOX_HEIGHT)
        seed_input_box_rect = pygame.Rect(PADDING_LEFT + 100, PADDING_TOP + 120, BOX_WIDTH, BOX_HEIGHT)
        na_input_box_rect = pygame.Rect(PADDING_LEFT + 100, PADDING_TOP + 310, BOX_WIDTH, BOX_HEIGHT)
        checkbox_rg = Checkbox(button_surface, 140, 320, label="use reach goal")
    
        # Font
        font_button = pygame.font.Font(CUSTOM_FONT, 20)
        font_attributes = pygame.font.Font(CUSTOM_FONT, 15)

        # Buttons
        generate_button_rect = pygame.Rect(PADDING_LEFT, PADDING_TOP + 150, BUTTON_WIDTH, BUTTON_HEIGHT)
        add_agents_button_rect = pygame.Rect(PADDING_LEFT, PADDING_TOP + 340, BUTTON_WIDTH, BUTTON_HEIGHT)
        add_new_button_rect = pygame.Rect(PADDING_LEFT, PADDING_TOP + 530, BUTTON_WIDTH, BUTTON_HEIGHT)

        draw_button(button_surface, BLUE, font_button, "Generate", generate_button_rect)
        draw_button(button_surface, BLUE, font_button, "Add Agents", add_agents_button_rect)
        draw_button(button_surface, BLUE, font_button, "Add New", add_new_button_rect)

        # Main loop
        while True:
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                checkbox_rg.handle_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    if rows_input_box_rect.collidepoint(x, y):
                        rows_active = True
                        cols_active = False
                        fcr_active = False
                        agglo_active = False
                        na_active = False
                        seed_active = False
                    
                    if cols_input_box_rect.collidepoint(x, y):
                        cols_active = True
                        rows_active = False
                        fcr_active = False
                        agglo_active = False
                        na_active = False
                        seed_active = False
                    
                    if fcr_input_box_rect.collidepoint(x, y):
                        fcr_active = True
                        cols_active = False
                        rows_active = False
                        agglo_active = False
                        na_active = False
                        seed_active = False

                    if agglo_input_box_rect.collidepoint(x, y):
                        agglo_active = True
                        fcr_active = False
                        cols_active = False
                        rows_active = False
                        na_active = False
                        seed_active = False

                    if na_input_box_rect.collidepoint(x, y):
                        na_active = True
                        fcr_active = False
                        cols_active = False
                        rows_active = False
                        agglo_active = False
                        seed_active = False

                    if seed_input_box_rect.collidepoint(x, y):
                        seed_active = True
                        na_active = False
                        fcr_active = False
                        cols_active = False
                        rows_active = False
                        agglo_active = False

                    if generate_button_rect.collidepoint(x, y):
                        generate_button_clicked = True
                        add_agents_button_clicked = False

                        rows_I = int(rows_input_value) if rows_input_value else rows
                        cols_I = int(cols_input_value) if cols_input_value else cols
                        traversability_I = float(fcr_input_value) if fcr_input_value else traversability
                        cluster_factor_I = float(agglo_input_value) if agglo_input_value else cluster_factor
                        seed_factor = int(seed_input_value) if seed_input_value else seed

                        # set profile parameters
                        self.profile.set_rows(rows_I)
                        self.profile.set_cols(cols_I)
                        self.profile.set_traversability(traversability_I)
                        self.profile.set_cluster_factor(cluster_factor_I)
                        self.profile.set_seed(seed_factor)
                        #

                        if seed_factor:
                            random.seed(seed_factor)

                        if rows_I > 25 or cols_I > 28 or rows_I < 1 or cols_I < 1 or traversability_I < 0 or traversability_I > 1 or cluster_factor_I < 0 or cluster_factor_I > 1:
                            messagebox.showinfo("Attention!", "Please insert valid values: \n- rows: 1-25 \n- cols: 1-28 \n- free cell ratio: 0-1 \n- cluster factor: 0-1")
                            continue
                        else:
                            self.profile.start_screening()
                            self.grid = grid_generator(rows_I, cols_I, traversability_I, cluster_factor_I)
                            self.profile.stop_screening("grid")

                            print_gui_grid(self.grid, grid_surface, cell_size, PADDING_LEFT, PADDING_TOP)
                        

                    if add_agents_button_rect.collidepoint(x, y) and generate_button_clicked and not add_agents_button_clicked:
                        add_agents_button_clicked = True
                        use_reach_goal = checkbox_rg.checked
                        n_agents_I = int(na_input_value) if na_input_value else n_agents


                        self.profile.start_screening()
                        self.instance = instance_generator(self.grid, n_agents_I, use_reach_goal)
                        self.profile.stop_screening("instance")

                        #set profile parameters
                        self.profile.set_use_reach_goal(use_reach_goal)
                        self.profile.set_n_agents(n_agents_I)
                        self.profile.set_instance(self.instance)
                        #

                        paths = self.instance.get_paths()
                        if not paths:
                            messagebox.showinfo("Attention!", "No paths found! Please generate a new grid.")

                        print_gui_paths(paths, grid_surface, cell_size, PADDING_LEFT, PADDING_TOP)

                    if add_new_button_rect.collidepoint(x, y) and add_agents_button_clicked:
                        self.profile.start_screening()
                        self.new_path, nodeDict, closed = reach_goal(self.instance.get_graph(), self.instance.get_init(), self.instance.get_goal(), self.instance.get_paths(), self.instance.get_time_new_goal_get_passed(), self.instance.get_max())
                        self.profile.stop_screening("path")

                        # set profile parameters
                        self.profile.set_new_path(self.new_path)
                        self.profile.set_nodeDict(nodeDict)
                        self.profile.set_closed(closed)
                        #

                        if self.new_path:
                            print_gui_path(self.new_path, grid_surface, cell_size, PADDING_LEFT, PADDING_TOP)
                        else:
                            messagebox.showinfo("Error", "Impossible to find a path!")
                        
                        self.profile.print_results_on_file()
                        
                    
                if event.type == pygame.KEYDOWN:
                    if rows_active:
                        if event.key == pygame.K_BACKSPACE:
                            rows_input_value = rows_input_value[:-1]
                        else:
                            rows_input_value += event.unicode

                    if cols_active:
                        if event.key == pygame.K_BACKSPACE:
                            cols_input_value = cols_input_value[:-1]
                        else:
                            cols_input_value += event.unicode

                    if fcr_active:
                        if event.key == pygame.K_BACKSPACE:
                            fcr_input_value = fcr_input_value[:-1]
                        else:
                            fcr_input_value += event.unicode

                    if agglo_active:
                        if event.key == pygame.K_BACKSPACE:
                            agglo_input_value = agglo_input_value[:-1]
                        else:
                            agglo_input_value += event.unicode
                    
                    if na_active:
                        if event.key == pygame.K_BACKSPACE:
                            na_input_value = na_input_value[:-1]
                        else:
                            na_input_value += event.unicode

                    if seed_active:
                        if event.key == pygame.K_BACKSPACE:
                            seed_input_value = seed_input_value[:-1]
                        else:
                            seed_input_value += event.unicode
            
            color = LIGHT_BLUE if rows_active else LIGHT_GREY
            draw_text("rows:", font_attributes, button_surface, PADDING_LEFT, PADDING_TOP)
            draw_input_box(button_surface, color, font_attributes, rows_input_value, rows_input_box_rect)
            
            color = LIGHT_BLUE if cols_active else LIGHT_GREY
            draw_text("cols:", font_attributes, button_surface, PADDING_LEFT, PADDING_TOP + 30)
            draw_input_box(button_surface, color, font_attributes, cols_input_value, cols_input_box_rect) 

            color = LIGHT_BLUE if fcr_active else LIGHT_GREY
            draw_text("free cell ratio:", font_attributes, button_surface, PADDING_LEFT, PADDING_TOP + 60)
            draw_input_box(button_surface, color, font_attributes, fcr_input_value, fcr_input_box_rect)  

            color = LIGHT_BLUE if agglo_active else LIGHT_GREY
            draw_text("cluster factor:", font_attributes, button_surface, PADDING_LEFT, PADDING_TOP + 90)
            draw_input_box(button_surface, color, font_attributes, agglo_input_value, agglo_input_box_rect)

            color = LIGHT_BLUE if na_active else LIGHT_GREY
            draw_text("n° of agents:", font_attributes, button_surface, PADDING_LEFT, PADDING_TOP + 310)
            draw_input_box(button_surface, color, font_attributes, na_input_value, na_input_box_rect)

            color = LIGHT_BLUE if seed_active else LIGHT_GREY
            draw_text("seed:", font_attributes, button_surface, PADDING_LEFT, PADDING_TOP + 120)
            draw_input_box(button_surface, color, font_attributes, seed_input_value, seed_input_box_rect)

            screen.blit(button_surface, (0, 0))  # Posiziona la superficie dei bottoni a sinistra
            screen.blit(grid_surface, (BUTTON_SURFACE_WIDTH, 0))

            checkbox_rg.draw()

            pygame.display.flip()

def draw_button(layout, color, font, text, button_rect):
    pygame.draw.rect(layout, color, button_rect)
    pygame.draw.rect(layout, BLACK, button_rect, 1)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    layout.blit(text_surface, text_rect)

def draw_input_box(layout, color, font, input_value, input_rect):
    pygame.draw.rect(layout, color, input_rect)
    pygame.draw.rect(layout, BLACK, input_rect, 1)
    text_surface = font.render(input_value, True, BLACK)
    layout.blit(text_surface, (input_rect.left + 1, input_rect.top + 1))

def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
