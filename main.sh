#import board
#import cell
#import sudoku_generator
import pygame, sys

def draw_start_screen(screen):
    width = 600
    height = 600
    # Initialize title font
    start_title_font = pygame.font.SysFont("Copperplate", 60)
    select_font = pygame.font.SysFont("Copperplate", 45)
    button_font = pygame.font.SysFont("Copperplate", 30)
    # Make screen white
    screen.fill((144, 213, 255))

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(
        center=(width // 2, height // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    select_surface = select_font.render("Select Game Mode", 0, (0, 0, 0))
    select_rectangle = select_surface.get_rect(
        center=(width // 2, height // 2 - 50))
    screen.blit(select_surface, select_rectangle)



    easy = pygame.font.SysFont('Copperplate', 30)
    easy_text = easy.render('Easy', False, (0, 0, 0))
    #screen.blit(easy_text, (55, 450))

    medium = pygame.font.SysFont('Copperplate', 30)
    medium_text = medium.render('Medium', False, (0, 0, 0))
    #screen.blit(medium_text, (250, 450))

    hard = pygame.font.SysFont('Copperplate', 30)
    hard_text = hard.render('Hard', False, (0, 0, 0))
    #screen.blit(hard_text, (475, 450))

    #initialize buttons
    button_width = 200
    button_height = 50
    easy_button = pygame.Rect(width // 2 - button_width // 2, height // 2 + 50, button_width, button_height)
    medium_button = pygame.Rect(width // 2 - button_width // 2, height // 2 + 120, button_width, button_height)
    hard_button = pygame.Rect(width // 2 - button_width // 2, height // 2 + 190, button_width, button_height)

    #draw the buttons
    pygame.draw.rect(screen, (255, 172, 28), easy_button)
    pygame.draw.rect(screen, (255, 172, 28), medium_button)
    pygame.draw.rect(screen, (255, 172, 28), hard_button)

    #add text to buttons
    screen.blit(easy_text, easy_text.get_rect(center=easy_button.center))
    screen.blit(medium_text, medium_text.get_rect(center=medium_button.center))
    screen.blit(hard_text, hard_text.get_rect(center=hard_button.center))

def main():
    try:
        # Initialize Pygame
        pygame.init()
        window_size = (600, 600)
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Sudoku Game")

        # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if easy_button.collidepoint(event.pos):
                        #create easy board
                    elif medium_button.collidepoint(event.pos):
                        #create medium board
                    elif hard_button.collidepoint(event.pos):
                        #create hard board
            draw_start_screen(screen)

            # Update the display
            pygame.display.flip()

    finally:
        pygame.quit()

# Entry point
if __name__ == "__main__":
    main()
