import random
import time
class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def choose_move(self) -> int:
        try:
            return int(input(f"Select a move ({self.symbol}): "))
        except ValueError:
            return -1

class AI(Player):
    def __init__(self, symbol, board):
        self.symbol = symbol
        self.board = board
    def choose_move(self):
        return random.choice(self.board.valid_positions)
