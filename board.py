import pygame, sys
from cell import *
pygame.init()

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    def draw(self):
        reset = pygame.font.SysFont('Arial', 30)
        reset_screen = reset.render('Reset', False, (0, 0, 0))
        self.screen.blit(reset_screen, (55, 620))

        restart = pygame.font.SysFont('Arial', 30)
        restart_screen = restart.render('Restart', False, (0, 0, 0))
        self.screen.blit(restart_screen, (250, 620))

        exit = pygame.font.SysFont('Arial', 30)
        exit_screen = exit.render('Exit', False, (0, 0, 0))
        self.screen.blit(exit_screen, (475, 620))

        # horizontal lines
        for i in range(0, 4):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 200), (600, i * 200), 4)
        # vertical lines
        for i in range(0, 4):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 200, 0), (i * 200, 600), 4)
        # smaller horizontal lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 600 / 9), (600, i * 600 / 9, 600), 2)
        # smaller vertical lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 600 / 9, 0), (i * 600 / 9, 600), 2)

    def select(self, row, col):
        width = 600 / 9
        height = 600 / 9
        x = col * width
        y = row * height
        pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_width, cell_height), 3)

    def click(self, row, col):
        mousex, mousey = event.pos
        if mousex in range(0, 600) and mousey in range(0, 600):
            row = mousey // 600
            col = mousex // 600
            return (row, col)
        return None
    def clear(self):
        pass
    def sketch(self, value):
        xval, yval = self.click
        font = pygame.font.Font(None, 10)
        text = font.render(value, True, (211, 211, 211))
        screen.blit(text, ((xval*200) + 5, (yval*200) + 5)
        pygame.display.update()

    def place_number(self, value):
        pass
    def reset_to_original(self):
        self.current_board = [row[:] for row in self.original_board]
        print("Board is reset.")
    def is_full(self):
        pass
    def update_board(self):
        pass
    def find_empty(self):
        for row in self.cells:
            for cell in row:
                self.board[cell.row][cell.col] = cell.value
    def check_board(self):
        pass

