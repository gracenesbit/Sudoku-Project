import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        cell_width = 600 / 9
        cell_height = 600 / 9
        x = self.col * cell_width
        y = self.row * cell_height

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_width, cell_height), 3)

        if self.value != 0:
            font = pygame.font.SysFont("arial", 40)
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + cell_width / 2, y + cell_height / 2))
            self.screen.blit(text, text_rect)

        elif self.sketched_value != 0:
            font = pygame.font.SysFont("arial", 20)
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x + 5, y + 5))
