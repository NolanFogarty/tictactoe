import subprocess
from board import Board
from player import Player

def render(board, message=""):
    subprocess.run("clear", shell=True)
    print(board)
    if message:
        print(message)

def main():
    board = Board(3)
    players = [Player("x"), Player("o")]
    turn = 0
    message = ""
    while not board.winner and not board.tie:
        render(board, message)
        message = ""
        player = players[turn % len(players)]
        square = player.choose_move()
        if board.valid_move(square):
            board.move(square, player.symbol)
            turn += 1
        else:
            message = "Invalid move. Please try again."
        if board.winner:
            render(board)
            print(f"{player.symbol.upper()} wins!")
        elif board.tie:
            render(board)
            print("It's a tie!")

if __name__ == "__main__":
    main()
