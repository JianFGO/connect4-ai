
ROWS = 6
COLS = 7

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('  ' + '   '.join(map(str, range(COLS))))

def drop_disc(board, col, symbol):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = symbol
            return True
    return False  # Column is full

def check_win(board, symbol):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == symbol for i in range(4)):
                return True

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == symbol for i in range(4)):
                return True

    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == symbol for i in range(4)):
                return True

    # Diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == symbol for i in range(4)):
                return True

    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    board = create_board()
    current_player = 1
    symbols = {1: '●', 2: '○'}

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn ({symbols[current_player]}).")
        try:
            col = int(input("Choose a column (0-6): "))
            if col < 0 or col >= COLS:
                print("Invalid column. Try again.")
                continue
            if not drop_disc(board, col, symbols[current_player]):
                print("Column full. Try another.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        if check_win(board, symbols[current_player]):
            print_board(board)
            print(f"Player {current_player} ({symbols[current_player]}) wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 2 if current_player == 1 else 1
