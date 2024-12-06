import pygame
from cell import Cell


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.original_board = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.selected = None

    def draw(self):
        for i in range(10):
            thickness = 4 if i % 3 == 0 else 2
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.width / 9, 0), (i * self.width / 9, self.height), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.height / 9), (self.width, i * self.height / 9), thickness)

        for row in self.board:
            for cell in row:
                cell.draw()

    def select(self, row, col):

        for r in self.board:
            for cell in r:
                cell.selected = False

        self.board[row][col].selected = True
        self.selected = (row, col)

    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            row = int(y // (self.height / 9))
            col = int(x // (self.width / 9))
            return row, col
        return None

    def clear(self):
        if self.selected:
            row, col = self.selected
            if self.original_board[row][col].value == 0:
                self.board[row][col].set_cell_value(0)
                self.board[row][col].set_sketched_value(0)

    def sketch(self, value):
        if self.selected:
            row, col = self.selected
            self.board[row][col].set_sketched_value(value)

    def place_number(self, value):
        if self.selected:
            row, col = self.selected
            if self.original_board[row][col].value == 0:
                self.board[row][col].set_cell_value(value)
                self.board[row][col].set_sketched_value(0)

    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col].set_cell_value(self.original_board[row][col].value)
                self.board[row][col].set_sketched_value(0)

    def is_full(self):
        return all(cell.value != 0 for row in self.board for cell in row)

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.original_board[row][col].value = self.board[row][col].value

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        for row in range(9):
            values = set()
            for col in range(9):
                num = self.board[row][col].value
                if num != 0:
                    if num in values:
                        return False
                    values.add(num)

        for col in range(9):
            values = set()
            for row in range(9):
                num = self.board[row][col].value
                if num != 0:
                    if num in values:
                        return False
                    values.add(num)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                values = set()
                for row in range(3):
                    for col in range(3):
                        num = self.board[box_row + row][box_col + col].value
                        if num != 0:
                            if num in values:
                                return False
                            values.add(num)

        return True
