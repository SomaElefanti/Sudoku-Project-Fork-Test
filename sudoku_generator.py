import math, random, pygame
from constants import *


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(row_length)] for j in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()

    def valid_in_row(self, row, num):
        for i in range(self.row_length):
            if num in self.board[row]:
                isin = False
                break
            else:
                isin = True
        return isin

    def valid_in_col(self, col, num):
        column = [row[col] for row in self.board]
        for i in range(self.row_length):
            if num in column:
                isin = False
                break
            else:
                isin = True
        return isin

    def valid_in_box(self, row_start, col_start, num):
        box = [[self.board[i][j] for j in range(col_start, col_start+2)] for i in range(row_start, row_start+3)]
        for i in range(len(box)):
            if num in box[i]:
                isin = False
                break
            else:
                isin = True
        return isin

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num):
            if self.valid_in_col(col, num):
                if row in range(0, 3):
                    row_start = 0
                elif row in range(3, 6):
                    row_start = 3
                elif row in range(6, 9):
                    row_start = 6
                if col in range(0, 3):
                    col_start = 0
                elif col in range(3, 6):
                    col_start = 3
                elif col in range(6, 9):
                    col_start = 6
                if self.valid_in_box(row_start, col_start, num):
                    validity = True
                else:
                    validity = False
            else:
                validity = False
        else:
            validity = False
        return validity

    def fill_box(self, row_start, col_start):
        used_numbers = set()
        box = [[self.board[i][j] for j in range(col_start, col_start + 2)] for i in range(row_start, row_start + 3)]
        for i in range(len(box)):
            for j in range(len(box[i])):
                if box[i][j] != 0:
                    used_numbers.add(box[i][j])
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                available_numbers = set(set(range(1, 10)) - used_numbers)
                random_number = int(random.sample(sorted(available_numbers), 1)[0])
                self.board[i][j] = random_number
                used_numbers.add(random_number)

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell
	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining
	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again
	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        cell_num = self.removed_cells
        while cell_num > 0:
            row_num = random.randrange(0, 9)
            col_num = random.randrange(0, 9)
            if self.board[row_num][col_num] != 0:
                self.board[row_num][col_num] = 0
                cell_num -= 1
            else:
                continue


class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        if self.selected:
            line_colour = (153, 12, 12)
        else:
            line_colour = LINE_COLOR
        num_font = pygame.font.SysFont("comicsansms", 70)
        pygame.draw.rect(self.screen, BG_COLOR, (self.col * 70, self.row * 70, 70, 70))
        pygame.draw.line(self.screen, line_colour, (self.col * 70, self.row * 70),
                         (self.col * 70, (self.row + 1) * 70), 5)
        pygame.draw.line(self.screen, line_colour, (self.col * 70, self.row * 70),
                         ((self.col + 1) * 70, self.row * 70), 5)
        pygame.draw.line(self.screen, line_colour, ((self.col + 1) * 70, self.row * 70),
                         ((self.col + 1) * 70, (self.row + 1) * 70), 5)
        pygame.draw.line(self.screen, line_colour, (self.col * 70, (self.row + 1) * 70),
                         ((self.col + 1) * 70, (self.row + 1) * 70), 5)

        if self.value != 0:
            num_surf = num_font.render(str(self.value), 1, (0, 0, 0))
            num_rect = num_surf.get_rect(center=((self.col * 70) + 70 // 2,
                                                 (self.row * 70) + 70 // 2))
            self.screen.blit(num_surf, num_rect)

        elif self.value == 0 and self.sketched_value is not None:
            sketch_font = pygame.font.SysFont("comicsansms", 40)
            sketch_surf = sketch_font.render(str(self.sketched_value), 1, (130, 122, 122))
            sketch_rect = sketch_surf.get_rect(center=((self.col * 70) + 70 // 4,
                                                       (self.row * 70) + 70 // 4))
            self.screen.blit(sketch_surf, sketch_rect)


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.generated = generate_sudoku(9, difficulty)
        self.board = self.generated[1]
        self.solved = self.generated[0]
        self.original = [row[:] for row in self.board]
        self.cells = [[Cell(self.board[row][col], row, col, self.screen)
                       for col in range(9)]
                      for row in range(9)]

    def draw(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()
        for i in range(0, 4):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), 10)
        for i in range(0, 4):
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH), 10)

    def select(self, row, col):
        if 0 <= row <= 8 and 0 <= col <= 8:
            self.cells[row][col].selected = True
            return self.cells[row][col]

    def click(self, x, y):
        if 0 <= x <= 630 and 0 <= y <= 630:
            row = y // 70
            col = x // 70
            return row, col
        else:
            return None

    def clear(self, row, col):
        if self.original[row][col] == 0:
            self.cells[row][col].value = 0
            self.cells[row][col].sketched_value = None

    def sketch(self, value, row, col):
        self.cells[row][col].sketched_value = value

    def place_number(self, value, row, col):
        self.cells[row][col].value = value
        self.cells[row][col].sketched_value = None

    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].value = self.original[row][col]

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col

    def check_board(self):
        if self.board != self.solved:
            return False
        return True

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution
Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)
Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board_solved = sudoku.get_board()
    board_before = [row[:] for row in board_solved]
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board_before, board

