import Board

def main():
    board = [
        [3, 0, 0, 6, 1, 0, 0, 0, 8],
        [0, 0, 2, 0, 3, 0, 7, 6, 0],
        [0, 0, 0, 7, 5, 0, 2, 9, 0],
        [0, 9, 0, 8, 0, 0, 0, 1, 0],
        [0, 4, 0, 1, 7, 3, 0, 5, 0],
        [0, 5, 0, 0, 0, 9, 0, 2, 0],
        [0, 3, 7, 0, 4, 1, 0, 0, 0],
        [0, 2, 5, 0, 8, 0, 9, 0, 0],
        [4, 0, 0, 0, 9, 7, 0, 0, 2]
    ]

    game = Board.Board(board)

    print("INITIAL BOARD")
    print("_______________")
    game.printBoard()

    print("\n\n")

    game.solve()

    print("SOLVED BOARD")
    print("_______________")
    game.printBoard()


if __name__ == '__main__':
    main()