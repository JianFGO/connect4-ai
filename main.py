from connect4 import create_board, print_board, drop_disc, check_win, check_draw
from agents.random_agent import RandomAgent

def play_game():
    board = create_board()
    human_symbol = '●'
    ai_symbol = '○'

    ai_player = RandomAgent(ai_symbol)

    current_player = 1  # 1 = Human, 2 = AI

    while True:
        print_board(board)

        if current_player == 1:
            print(f"Your turn ({human_symbol}).")
            try:
                col = int(input("Choose a column (0-6): "))
                if col < 0 or col >= 7:
                    print("Invalid column. Try again.")
                    continue
                if not drop_disc(board, col, human_symbol):
                    print("Column full. Try another.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

        else:
            print(f"AI's turn ({ai_symbol}).")
            col = ai_player.get_move(board)
            drop_disc(board, col, ai_symbol)

        # Check for win or draw
        if check_win(board, human_symbol if current_player == 1 else ai_symbol):
            print_board(board)
            if current_player == 1:
                print("Congratulations! You win!")
            else:
                print("AI wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    play_game()
