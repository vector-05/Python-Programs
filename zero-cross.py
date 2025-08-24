def print_board(board):
    for row in board:
        print(' '.join(row))

def make_move(board, x, y, player):
    if board[x][y] != ' ':
        return False
    board[x][y] = player
    return True

def has_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # no winner
    return None

def play_game():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    player = 'X'

    while True:
        print_board(board)
        x = int(input('Enter x coordinate: '))
        y = int(input('Enter y coordinate: '))
        if not make_move(board, x, y, player):
            print('Invalid move!')
            continue

        winner = has_winner(board)
        if winner:
            print_board(board)
            print(winner, 'wins!')
            break

        player = 'X' if player == 'O' else 'O'

play_game()
