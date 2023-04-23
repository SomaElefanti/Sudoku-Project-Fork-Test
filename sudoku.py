import pygame, sys
from constants import *
from sudoku_generator import *

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
            cell_selected.draw()  # select the new cell
            previous_cell = cell_selected

    pygame.display.update()


