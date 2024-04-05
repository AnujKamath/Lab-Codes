def create_board():
    return [[' ']*7 for _ in range(6)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-'*13)

def drop_piece(board, col, piece):
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = piece
            break

def is_full_column(board, col):
    return board[0][col] != ' '

def is_board_full(board):
    return all(is_full_column(board, col) for col in range(7))

def check_winner(board, piece):
    for row in range(6):
        for col in range(4):
            if all(board[row][col+c] == piece for c in range(4)):
                return True
    for row in range(3):
        for col in range(7):
            if all(board[row+r][col] == piece for r in range(4)):
                return True
    for row in range(3):
        for col in range(4):
            if all(board[row+r][col+c] == piece for r, c in zip(range(4), range(4))):
                return True
    for row in range(3):
        for col in range(3, 7):
            if all(board[row+r][col-c] == piece for r, c in zip(range(4), range(4))):
                return True
    return False

def main():
    board = create_board()
    player = 1
    print_board(board)
    while True:
        col = int(input(f"Player {player}, select a column (0-6): "))
        if col < 0 or col > 6 or is_full_column(board, col):
            continue
        drop_piece(board, col, 'X' if player == 1 else 'O')
        print_board(board)
        if check_winner(board, 'X'):
            print("Player 1 wins!")
            break
        elif check_winner(board, 'O'):
            print("Player 2 wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        player = 2 if player == 1 else 1

if __name__ == "__main__":
    main()

