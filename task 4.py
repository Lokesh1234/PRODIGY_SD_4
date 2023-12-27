def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row, column, and 3x3 subgrid
    return (
        all(num != board[row][i] for i in range(9)) and
        all(num != board[i][col] for i in range(9)) and
        all(num != board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] for i in range(9))
    )

def find_empty_location(board):
    # Find the first empty cell in the board (represented by 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    empty_row, empty_col = find_empty_location(board)

    # If no empty cell is found, the Sudoku is solved
    if empty_row is None and empty_col is None:
        return True

    for num in range(1, 10):
        if is_valid(board, empty_row, empty_col, num):
            # Try placing the number in the empty cell
            board[empty_row][empty_col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If the current placement leads to an invalid solution, backtrack
            board[empty_row][empty_col] = 0

    # If no number can be placed in the current cell, backtrack
    return False

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists.")
