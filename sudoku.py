import pygame, sys
from constants import *
from sudoku_generator import *

def draw_game_start(screen):
    # Initialize title font
    start_title_font_1 = pygame.font.SysFont("comicsansms", 60)
    start_title_font_2 = pygame.font.SysFont("comicsansms", 35)
    button_font = pygame.font.SysFont("comicsansms", 70)
    screen.fill(BG_COLOR)
    # Initialize and draw title
    title_surface_1 = start_title_font_1.render("Welcome to Sudoku", 0, (0, 0, 0))
    title_rectangle_1 = title_surface_1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 350))
    screen.blit(title_surface_1, title_rectangle_1)
    title_surface_2 = start_title_font_2.render("Select Game Mode:", 0, (0, 0, 0))
    title_rectangle_2 = title_surface_2.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface_2, title_rectangle_2)
    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))
    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))
    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 175))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 325))
    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30
                elif medium_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50
        pygame.display.update()


def draw_game_over():
    screen.fill(BG_COLOR)
    font = pygame.font.SysFont("comicsansms", 100)
    if board_surf.check_board():
        end_text = "Game Won!"
    else:
        end_text = "Game Over!"
    end_surf = font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(end_surf, end_rect)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Sudoku 111")
    icon = pygame.image.load("sudokuicon.png")
    # Source: https://www.flaticon.com/free-icon/pastime_3401126?term=sudoku&related_id=3401126
    pygame.display.set_icon(icon)
    num_font = pygame.font.SysFont("comicsansms", 200)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    difficulty = draw_game_start(screen)
    screen.fill(BG_COLOR)

    board_surf = Board(WIDTH, HEIGHT, screen, difficulty)
    board_surf.draw()
    previous_cell = None
    row = None
    col = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // 70
                col = x // 70
                cell_selected = board_surf.select(row, col)
                if previous_cell is not None:
                    previous_cell.selected = False
                    previous_cell.draw()
                if 0 <= row <= 8 and 0 <= col <= 8:
                    cell_selected.draw()
                    previous_cell = cell_selected
                if 0 <= x <= 630 and 0 <= y <= 630:
                    pass
                if 0 <= x <= 630 and 0 <= y <= 630:
                    pass
                if 0 <= x <= 630 and 0 <= y <= 630:
                    pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    value = 1
                if event.key == pygame.K_2:
                    value = 2
                if event.key == pygame.K_3:
                    value = 3
                if event.key == pygame.K_4:
                    value = 4
                if event.key == pygame.K_5:
                    value = 5
                if event.key == pygame.K_6:
                    value = 6
                if event.key == pygame.K_7:
                    value = 7
                if event.key == pygame.K_8:
                    value = 8
                if event.key == pygame.K_9:
                    value = 9
                if row is not None and col is not None and board_surf.cells[row][col].value == 0:
                    board_surf.sketch(value, row, col)
                    board_surf.cells[row][col].draw()
                if event.key == pygame.K_RETURN and board_surf.cells[row][col].sketched_value is not None:
                    board_surf.place_number(board_surf.cells[row][col].sketched_value, row, col)
                    board_surf.update_board()
                    board_surf.cells[row][col].draw()

        if board_surf.is_full():
            pygame.display.update()
            pygame.time.delay(1000)
            draw_game_over()

        pygame.display.update()


