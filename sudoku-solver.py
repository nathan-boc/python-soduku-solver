class Board:
    def __init__(self, board):
        self.board = board

    def printBoard(self):
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


    def findEmpty(self):
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 0:
                    return i, j     # row, col

        return None


    def valid(self, num, position):

        rows = len(board)
        cols = len(board[0])

        currRow, currCol = position

        # Check row
        for i in range(cols):
            if board[currRow][i] == num and i != currCol:
                return False

        # Check column
        for i in range(rows):
            if board[i][currCol] == num and i != currRow:
                return False

        # Check subgrid
        subgrid_x = currCol // 3
        subgrid_y = currRow // 3

        for i in range(subgrid_y * 3, subgrid_y * 3 + 3):
            for j in range(subgrid_x * 3, subgrid_x * 3 + 3):
                if board[i][j] == num and (i, j) != (currRow, currCol):
                    return False

        return True
        

    def solve(self):
        nextSpace = self.findEmpty()

        # if no empty spaces left on board, algorithm is complete
        if not nextSpace:
            return True

        else:
            row, col = nextSpace
        
        # Check through possible values for each position
        for i in range(1, 10):
            if self.valid(i, (row,col)):
                board[row][col] = i

                if self.solve():
                    return True
                
                board[row][col] = 0
        
        return False


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
   
game = Board(board)

print("INITIAL BOARD")
print("_______________")
game.printBoard()

print("\n\n")

game.solve()

print("SOLVED BOARD")
print("_______________")
game.printBoard()