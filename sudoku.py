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
cell_surf = Cell('4', 1, 2, screen)
cell_surf.draw()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


