import pygame, sys
from constants import *
from sudoku_generator import *


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


pygame.init()
pygame.display.set_caption('Sudoku 111')
icon = pygame.image.load('sudokuicon.png')
# Source: https://www.flaticon.com/free-icon/pastime_3401126?term=sudoku&related_id=3401126
pygame.display.set_icon(icon)
num_font = pygame.font.SysFont("comicsansms", 200)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)

board_surf = Board(WIDTH, HEIGHT, screen, 30)
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
            cell_selected.draw()
            previous_cell = cell_selected

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


