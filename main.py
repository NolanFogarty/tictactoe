from board import Board

def main():
    # size = input("Please select a board size: ")
    board = Board(3)
    print(board)
    player1 = True
    while True:
        square = int(input("Select a move: "))
        if board.valid_move(square):
            if player1:
                board.move(square, "x")
            else:
                board.move(square, "o")
            player1 = not player1
        else:
            print("Invalid move. Please try again.")
        print(board)
    # board.print_board()

if __name__ == "__main__":
    main()
