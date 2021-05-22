class Board:
    def __init__(self, board):
        self.board = board

    def printBoard(self):
        rows = len(self.board)
        cols = len(self.board[0])

        for i in range(rows):

            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - -")

            for j in range(cols):
                
                if j % 3 == 0 and j != 0:
                    print("| ", end = '')

                if self.board[i][j] == 0:
                    print("0 ", end = '')
                else:
                    print(str(self.board[i][j]) + " ", end = '')

            print()


    def findEmpty(self):
        rows = len(self.board)
        cols = len(self.board[0])

        for i in range(rows):
            for j in range(cols):
                if self.board[i][j] == 0:
                    return i, j     # row, col

        return None


    def valid(self, num, position):

        rows = len(self.board)
        cols = len(self.board[0])

        currRow, currCol = position

        # Check row
        for i in range(cols):
            if self.board[currRow][i] == num and i != currCol:
                return False

        # Check column
        for i in range(rows):
            if self.board[i][currCol] == num and i != currRow:
                return False

        # Check subgrid
        subgrid_x = currCol // 3
        subgrid_y = currRow // 3

        for i in range(subgrid_y * 3, subgrid_y * 3 + 3):
            for j in range(subgrid_x * 3, subgrid_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != (currRow, currCol):
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
                self.board[row][col] = i

                if self.solve():
                    return True
                
                self.board[row][col] = 0
        
        return False
