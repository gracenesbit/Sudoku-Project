import pygame
import sys
from board import Board
from sudoku_generator import SudokuGenerator
from cell import Cell

pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_WIDTH = 600
GRID_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")

# Fonts
font = pygame.font.SysFont("arialblack", 73)
sub_font = pygame.font.SysFont("arialblack", 60)
button_font = pygame.font.SysFont("Copperplate", 50)

# Colors
TEXT_COLOR = (0, 0, 0)
BG_COLOR = (144, 213, 255)
BUTTON_COLOR = (255, 172, 28)
BUTTON_TEXT_COLOR = (0, 0, 0)

button_width = 200
button_height = 50

# Buttons for difficulty selection and controls
easy_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + 50, button_width, button_height)
medium_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + 120, button_width, button_height)
hard_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + 190, button_width, button_height)
reset_button = pygame.Rect(712 - button_width // 2, SCREEN_HEIGHT // 2 - 150, button_width - 20, button_height)
restart_button = pygame.Rect(712 - button_width // 2, SCREEN_HEIGHT // 2, button_width - 20, button_height)
exit_button = pygame.Rect(712 - button_width // 2, SCREEN_HEIGHT // 2 + 150, button_width - 20, button_height)


def draw_text(text, font, color, x, y, surface):
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, (x, y))


def draw_start_screen():
    screen.fill(BG_COLOR)
    title_surface = font.render("Welcome to Sudoku", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    select_surface = sub_font.render("Select Game Mode", 0, (0, 0, 0))
    select_rectangle = select_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
    screen.blit(select_surface, select_rectangle)

    # Draw buttons
    pygame.draw.rect(screen, BUTTON_COLOR, easy_button)
    pygame.draw.rect(screen, BUTTON_COLOR, medium_button)
    pygame.draw.rect(screen, BUTTON_COLOR, hard_button)

    easy_text = button_font.render("Easy", 0, (0, 0, 0))
    screen.blit(easy_text, easy_text.get_rect(center=easy_button.center))
    medium_text = button_font.render("Medium", 0, (0, 0, 0))
    hard_text = button_font.render("Hard", 0, (0, 0, 0))
    screen.blit(easy_text, easy_text.get_rect(center=easy_button.center))
    screen.blit(medium_text, medium_text.get_rect(center=medium_button.center))
    screen.blit(hard_text, hard_text.get_rect(center=hard_button.center))

    pygame.display.flip()


def draw_game_over_screen(won):
    screen.fill(BG_COLOR)
    if won:
        draw_text("You Won!", font, TEXT_COLOR, 250, 250, screen)
    else:
        draw_text("Game Over!", font, TEXT_COLOR, 200, 250, screen)

    draw_text("Press R to Restart", button_font, TEXT_COLOR, 175, 425, screen)
    pygame.display.flip()


def main():
    running = True
    game_in_progress = False
    game_paused = False
    board = None

    while running:
        if not game_in_progress:
            draw_start_screen()
        
        else:
            screen.fill(BG_COLOR)
            board.draw()


            pygame.draw.rect(screen, BUTTON_COLOR, reset_button)
            pygame.draw.rect(screen, BUTTON_COLOR, restart_button)
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)

            #draw_text("Reset", button_font, BUTTON_TEXT_COLOR, 175, 810, screen)
            #draw_text("Restart", button_font, BUTTON_TEXT_COLOR, 355, 810, screen)
            #draw_text("Exit", button_font, BUTTON_TEXT_COLOR, 640, 810, screen)
            reset_text = button_font.render("Reset", 0, (0, 0, 0))
            screen.blit(reset_text, reset_text.get_rect(center=reset_button.center))
            restart_text = button_font.render("Restart", 0, (0, 0, 0))
            exit_text = button_font.render("Exit", 0, (0, 0, 0))
            screen.blit(restart_text, restart_text.get_rect(center=restart_button.center))
            screen.blit(exit_text, exit_text.get_rect(center=exit_button.center))


            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle start screen input
            if not game_in_progress and not game_paused and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(mouse_pos):
                    difficulty = "easy"
                    puzzle = SudokuGenerator.generate_sudoku(9, 30)  # Easy: 30 cells removed
                elif medium_button.collidepoint(mouse_pos):
                    difficulty = "medium"
                    puzzle = SudokuGenerator.generate_sudoku(9, 40)  # Medium: 40 cells removed
                elif hard_button.collidepoint(mouse_pos):
                    difficulty = "hard"
                    puzzle = SudokuGenerator.generate_sudoku(9, 50)  # Hard: 50 cells removed
                else:
                    continue


                board = Board(GRID_WIDTH, GRID_HEIGHT, screen, difficulty)
                board.board = [
                    [Cell(value=puzzle[r][c], row=r, col=c, screen=screen) for c in range(9)]
                    for r in range(9)
                ]
                board.original_board = [
                    [Cell(value=puzzle[r][c], row=r, col=c, screen=screen) for c in range(9)]
                    for r in range(9)
                ]
                game_in_progress = True



            if game_in_progress and not game_paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()


                    if reset_button.collidepoint(mouse_pos) and board:
                        board.reset_to_original()
                    elif restart_button.collidepoint(mouse_pos):
                        game_in_progress = False
                        board = None  # Reset board
                    elif exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()


                    if board:
                        selected = board.click(*mouse_pos)
                        if selected:
                            row, col = selected
                            board.select(row, col)

                if event.type == pygame.KEYDOWN and board and board.selected:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        board.sketch(event.key - pygame.K_0)
                    elif event.key == pygame.K_RETURN:
                        row, col = board.selected
                        sketched_value = board.board[row][col].sketched_value
                        board.place_number(sketched_value)
                    elif event.key == pygame.K_BACKSPACE:
                        board.clear()

                    # Check for game completion
                    if board.is_full() and board.check_board():
                        draw_game_over_screen(won='m')
                        pygame.time.wait(5000)
                        game_in_progress = False
                        board = None
                    elif board.is_full() and not board.check_board():
                        draw_game_over_screen(won=None)
                        pygame.time.wait(5000)
                        game_in_progress = False
                        board = None

        pygame.display.flip()


if __name__ == "__main__":
    main()
