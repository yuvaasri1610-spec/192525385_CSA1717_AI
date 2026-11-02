N = 8

def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve(board, row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            board[row] = -1

    return False

board = [-1] * N

if solve(board, 0):
    print("Solution for 8-Queen Problem:")
    print_board(board)
else:
    print("No solution exists.")
