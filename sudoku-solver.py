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

def printBoard(board):
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):

        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(cols):
            
            if j % 3 == 0 and j != 0:
                print("| ", end = '')

            if board[i][j] == 0:
                print("0 ", end = '')
            else:
                print(str(board[i][j]) + " ", end = '')

        print()

def findEmpty(board):
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                return i, j     # row, col

    return None

printBoard(board)