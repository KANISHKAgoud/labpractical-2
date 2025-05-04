def print_solution(board, n):
    print("\nOne solution:")
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))

def solve_n_queens_branch_and_bound(n):
    def backtrack(row):
        if row == n:
            print_solution(board, n)
            return True

        for col in range(n):
            if not cols[col] and not diag1[row - col] and not diag2[row + col]:
                board[row][col] = 1
                cols[col] = diag1[row - col] = diag2[row + col] = True

                if backtrack(row + 1):
                    return True

                board[row][col] = 0
                cols[col] = diag1[row - col] = diag2[row + col] = False

        return False

    board = [[0] * n for _ in range(n)]
    cols = [False] * n
    diag1 = {}
    diag2 = {}
    for i in range(-n + 1, n): diag1[i] = False
    for i in range(2 * n): diag2[i] = False

    backtrack(0)

# Run the function
solve_n_queens_branch_and_bound(4)
