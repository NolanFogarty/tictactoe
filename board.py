class Board:
    def __init__(self, n: int):
        self.grid = self.create_grid(n)
        self.winner = None

    def create_grid(self, n: int):
        return [[None] * n for _ in range(n)]
    
    def __str__(self):
        lines = []
        index = 0
        for row in range(len(self.grid)):
            line = ""
            for col in range(len(self.grid[0])):
                index += 1
                value = self.grid[row][col]
                if not value:
                    line += "[" + str(index) + "]"
                else:
                    line += "[" + str(value) + "]"
            lines.append(line)
        return "\n".join(lines)

    def valid_move(self, n):
        in_grid = (n >= 0) and (n <= len(self.grid)**2)
        if not in_grid:
            return False
        row, col = self.num_to_grid(n)
        not_taken = not self.grid[row][col]
        return not_taken

    def move(self, n):
        row, col = self.num_to_grid(n)
        self.grid[row][col] = "x"

    def num_to_grid(self, n):
        length = len(self.grid)
        x = (n-1) % length
        y = (n-1) // length
        return (x, y)

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

