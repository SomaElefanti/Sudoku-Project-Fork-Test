import math, random


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

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        pass


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        pass

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

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
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board