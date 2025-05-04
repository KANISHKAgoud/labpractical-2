def is_safe(board, row, col, n):
    # Check vertical (column)
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_backtracking(board, row, n):
    if row == n:
        print_solution(board, n)
        return True  # Return True to show at least one solution exists

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            if solve_n_queens_backtracking(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False

def print_solution(board, n):
    print("\nOne solution:")
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))


n = 4
board = [[0] * n for _ in range(n)]
solve_n_queens_backtracking(board, 0, n)
