# agents/random_agent.py

import random

class RandomAgent:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        valid_moves = [col for col in range(7) if board[0][col] == ' ']
        return random.choice(valid_moves)
