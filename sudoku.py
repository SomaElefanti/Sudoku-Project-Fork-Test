import sudoku_generator

board1 = sudoku_generator.SudokuGenerator(9, 30)

sudoku_generator.SudokuGenerator.print_board(board1)

print(sudoku_generator.SudokuGenerator.valid_in_row(board1, 2, 0))
print(sudoku_generator.SudokuGenerator.valid_in_row(board1, 2, 3))

print(sudoku_generator.SudokuGenerator.valid_in_col(board1, 2, 0))
print(sudoku_generator.SudokuGenerator.valid_in_col(board1, 2, 3))
