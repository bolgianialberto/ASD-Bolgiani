import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CUSTOM_FONT = 'Lato-Regular.ttf'

WIDTH, HEIGHT = 400, 200

class Checkbox:
    def __init__(self, screen, x, y, width=20, height=20, label=''):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.checked = False
        self.label = label
        self.font = pygame.font.Font(CUSTOM_FONT, 15)

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, self.rect, 1)

        if self.label:
            text_surface = self.font.render(self.label, True, BLACK)
            text_rect = text_surface.get_rect(midleft=(self.rect.right-120, self.rect.centery))
            self.screen.blit(text_surface, text_rect)

        if self.checked:
            pygame.draw.line(self.screen, BLACK, (self.rect.left+2, self.rect.top+2), (self.rect.right-2, self.rect.bottom-2), 2)
            pygame.draw.line(self.screen, BLACK, (self.rect.left+2, self.rect.bottom-2), (self.rect.right-2, self.rect.top+2), 2)
        else:
            pygame.draw.rect(self.screen, WHITE, self.rect)
            pygame.draw.rect(self.screen, BLACK, self.rect, 1)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked