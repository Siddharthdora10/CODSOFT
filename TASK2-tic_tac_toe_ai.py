

import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def is_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def minimax(board, depth, is_max):
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)

    for _ in range(9):
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != " ":
            print("Invalid move, try again.")
            continue
        board[row][col] = "X"

        if is_winner(board, "X"):
            print_board(board)
            print("You win!")
            return
        if is_full(board):
            break

        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"
        print("AI played:")
        print_board(board)

        if is_winner(board, "O"):
            print("AI wins!")
            return

    print("It's a draw!")

if __name__ == "__main__":
    play_game()
