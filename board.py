class Board:
    def __init__(self, n: int):
        self.board = self.create_board(n)
        self.winner = False

    def create_board(self, n: int):
        return [[None] * n for _ in range(n)]
    
    def print_board(self):
        index = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                index += 1
                value = self.board[row][col]
                if not value:
                    print("[" + str(index) + "]", end="")
                else:
                    print("[" + str(value) + "]", end="")
            print()

    def valid_move(self, row, col):
        return not self.board[row][col]


    # def winner(board):
    #     n = len(board)
    #
    #     # check rows
    #     for row in range(n):
    #         seen = set()
    #         for col in range(n):
    #             value = board[row][col]
    #             if value not in seen:
    #                 seen.add(value)
    #         if len(seen) == 1:
    #             return True
    #
    #     # check for cols
    #     for col in range(n):
    #         seen = set()
    #         for row in range(n):
    #             value = board[row][col]
    #             if value not in seen:
    #                 seen.add(value)
    #         if len(seen) == 1:
    #             return True
    #
    #     # check diagonals
    #     seen = set()
    #     for i in range(n):
    #         seen.add(board[i][i])
    #     if len(seen) == 1:
    #         return True
    #
    #     seen = set()
    #     j = n-1
    #     for i in range(n):
    #         val = board[i][j]
    #         seen.add(val)
    #         j -= 1
    #     if len(seen) == 1:
    #         return True

