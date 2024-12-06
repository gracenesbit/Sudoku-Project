import pygame, sys
from cell import *
pygame.init()

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected = None
        self.board = [[0] * 9 for i in range(9)]
        self.original_board = [[0] * 9 for i in range(9)]
    def draw(self):
        reset = pygame.font.SysFont('Arial', 30)
        reset_screen = reset.render('Reset', False, (0, 0, 0))
        self.screen.blit(reset_screen, (55, 620))

        restart = pygame.font.SysFont('Arial', 30)
        restart_screen = restart.render('Restart', False, (0, 0, 0))
        self.screen.blit(restart_screen, (250, 620))


        exit_screen = reset.render('Exit', False, (0, 0, 0))
        self.screen.blit(exit_screen, (475, 620))

        # horizontal lines
        for i in range(0, 4):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 200), (600, i * 200), 4)
        # vertical lines
        for i in range(0, 4):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 200, 0), (i * 200, 600), 4)
        # smaller horizontal lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 600 / 9), (600, i * 600 / 9), 2)
        # smaller vertical lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 600 / 9, 0), (i * 600 / 9, 600), 2)

    def select(self, row, col):
        width = 600 / 9
        height = 600 / 9
        x = col * width
        y = row * height
        pygame.draw.rect(self.screen, (255, 0, 0), (x, y, width, height), 3)

    def click(self, row, col):
        mousex, mousey = row, col
        if 0 <= mousex < self.width and 0 <= mousey < self.height:
            row = int(mousey // ( self.height/9))
            col = int(mousex // (self.width/9))
            self.selected = (row, col)
            return self.selected
        else:
            self.selected = None
            return None
    def clear(self):
        if self.selected:
            row, col = self.selected
            if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]):
                if self.board[row][col] == 0:
                    self.board[row][col] = 0
    def sketch(self, value):
       if self.selected:
           row, col = self.selected
           if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]):
               font = pygame.font.Font(None, 20)
               text = font.render(str(value), True, (211, 211, 211))
               xval = col (600/9) +5
               yval = row (600/9) +5
               self.screen.blit(text, xval, yval)
               pygame.display.update()

    def place_number(self, value):
        if self.selected:
            row, col = self.selected
            if self.original_board[row][col] == 0:
                self.board[row][col] = value
                self.draw()
                font = pygame.font.SysFont('Arial', 40)
                text = font.render(str(value), True, (255, 255, 255))
                x = col * (600 / 9) + ((600 / 9) / 2) - (text.get_width() / 2)
                y = row * (600 / 9) + ((600 / 9) / 2) - (text.get_height() / 2)
                self.screen.blit(text, (x, y))
                pygame.display.update()
    def reset_to_original(self):
        if self.original_board:
            self.board = [row[:] for row in self.original_board]
    def is_full(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def update_board(self):
        if self.original_board and self.board:
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    self.original_board [row][col] = self.board[row][col]
    def find_empty(self):
         for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
    def check_board(self):
         for row in range(len(self.board)):
            value = set()
            for num in self.board[row]:
                if num != 0:
                    if num in value or not (1 <= num <= 9):
                        return False
                    value.add(num)
            for col in range(len(self.board[0])):
                value = set()
                for row in range(len(self.board)):
                    num = self.board[row][col]
                    if num != 0:
                        if num in value or not (1 <= num <= 9):
                            return False
                        value.add(num)
            for start_row in range(0,len(self.board), 3):
                for start_col in range(0, len(self.board[0]), 3):
                    value = set()
                    for row in range(3):
                        for col in range(3):
                            num = self.board[start_row + row][start_col + col]
                            if num != 0:
                                if num in value or not (1 <= num <= 9):
                                    return False
                                value.add(num)
            return True
