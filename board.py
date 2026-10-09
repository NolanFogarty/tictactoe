# Source - https://stackoverflow.com/a/6586061
# Posted by Kevin Chou
# Retrieved 2026-10-09, License - CC BY-SA 4.
class colors: # You may need to change color settings
    RED = '\033[31m'
    END = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

class Board:
    def __init__(self, n: int):
        self.grid = self.create_grid(n)
        self.winner = None
        self.num_moves = 0
        self.tie = False

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
                elif value == "x":
                    line += "[" + colors.BLUE + str(value) + colors.END +  "]"
                else:
                    line += "[" + colors.RED + str(value) + colors.END +  "]"
            lines.append(line)
        return "\n".join(lines)

    def valid_move(self, n):
        in_grid = (n > 0) and (n <= len(self.grid)**2)
        if not in_grid:
            return False
        row, col = self.num_to_grid(n)
        not_taken = not self.grid[row][col]
        return not_taken

    def move(self, n, character):
        row, col = self.num_to_grid(n)
        self.grid[row][col] = character
        self.num_moves += 1
        self.winner = self.win_check()
        if self.num_moves == len(self.grid)**2 and not self.winner:
            self.tie = True

    def num_to_grid(self, n):
        length = len(self.grid)
        x = (n-1) // length
        y = (n-1) % length
        return (x, y)

    def win_check(self):
        n = len(self.grid)

        # check rows
        for row in range(n):
            first = self.grid[row][0]
            count = 0
            for col in range(n):
                if first is not None and self.grid[row][col] == first:
                    count += 1
            if count == n:
                return True

        # check cols
        for col in range(n):
            first = self.grid[0][col]
            count = 0
            for row in range(n):
                if first is not None and self.grid[row][col] == first:
                    count += 1
            if count == n:
                return True

        # check diagonals
        first = self.grid[0][0]
        count = 0
        for i in range(n):
            if first is not None and self.grid[i][i] == first:
                count += 1
        if count == n:
            return True

        first = self.grid[0][n - 1]
        count = 0
        for i in range(n):
            if first is not None and self.grid[i][n - 1 - i] == first:
                count += 1
        if count == n:
            return True

        return False
