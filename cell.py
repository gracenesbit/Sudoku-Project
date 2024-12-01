import pygame, sys
pygame.init()

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
    def find_dimensions(self, row, col):
        x_exact = (col * (600/9)) -600/18 - 9
        y_exact = (row * (600/9)) -600/18 - 20
        return x_exact, y_exact
    def draw(self, color):
        number = pygame.font.SysFont('Arial', 40)
        place_num = number.render(str(self.value), False, color)
        x, y = self.find_dims(self.row, self.col)
        self.screen.blit(place_num, (x, y))