from board import Board

def main():
    # size = input("Please select a board size: ")
    board = Board(3)
    while True:
        square = int(input("Select a move: "))
        if board.valid_move(square):
            board.move(square)
        else:
            print("Invalid move. Please try again.")
        print(board)
    # board.print_board()

if __name__ == "__main__":
    main()
