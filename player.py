class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def choose_move(self) -> int:
        return int(input(f"Select a move ({self.symbol}): "))
