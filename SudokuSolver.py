import pygame
pygame.font.init()


# Grid represents the entire sudoku board
class Grid:

    def __init__(self, window, board):
        
        # Declaring final variables
        self.rows, self.cols = 9, 9
        self.width, self.height = 540, 540

        self.tiles = [[Tile(board[i][j], i, j, self.width, self.height) for j in range(self.cols)] for i in range(self.rows)]
        
        self.board = None
        self.update_board()
        self.window = window


    def update_board(self):
        self.board = [[self.tiles[i][j].value for j in range(self.cols)] for i in range(self.rows)]


    def draw(self):
        padding = self.width / 9
        
        # Draw grid lines
        for i in range(self.rows + 1):
            
            # Draws thicker lines separating each subgrid
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1

            pygame.draw.line(self.window, pygame.Color('#808080'), (0, i * padding), (self.width, i * padding), thickness)
            pygame.draw.line(self.window, pygame.Color('#808080'), (i * padding, 0), (i * padding, self.height), thickness)

        # Draw Tile objects
        for i in range(self.rows):
            for j in range(self.cols):
                self.tiles[i][j].draw(self.window)

    def solve(self):
        self.update_board()

        nextSpace = findEmpty(self.board)

        # if no empty spaces left on board, algorithm is complete
        if not nextSpace:
            return True

        else:
            row, col = nextSpace
        
        # Check through possible values for each position
        for i in range(1, 10):
            if valid(self.board, i, (row,col)):
                self.board[row][col] = i
                self.tiles[row][col].setValue(i)
                self.tiles[row][col].draw_update(self.window, True)
                self.update_board()
                pygame.display.update()
                pygame.time.delay(100)

                if self.solve():
                    return True
                
                self.board[row][col] = 0
                self.tiles[row][col].setValue(0)
                self.update_board()
                self.tiles[row][col].draw_update(self.window, False)
                pygame.display.update()
                pygame.time.delay(100)
        
        return False

# END Grid Class #


# Tile represents a single square on the sudoku board
class Tile:

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.fnt = pygame.font.SysFont("comicsans", 40)

    def draw(self, window):
        padding = self.width / 9
        x = self.col * padding
        y = self.row * padding

        if(self.value != 0):
            text = self.fnt.render(str(self.value), 1, pygame.Color('white'))
            window.blit(text, (x + (padding / 2 - text.get_width() / 2), y + (padding / 2 - text.get_height() / 2)))


    def draw_update(self, window, solved=True):
        padding = self.width / 9
        x = self.col * padding
        y = self.row * padding

        pygame.draw.rect(window, pygame.Color('#111111'), (x, y, padding, padding), 0)

        text = self.fnt.render(str(self.value), 1,  pygame.Color('white'))
        window.blit(text, (x + (padding / 2 - text.get_width() / 2), y + (padding / 2 - text.get_height() / 2)))
        
        if solved:
            # Displays green bordering
            pygame.draw.rect(window, (0, 255, 0), (x, y, padding, padding), 3)
        else:
            # Displays red bordering when backtracking
            pygame.draw.rect(window, (255, 0, 0), (x, y, padding, padding), 3)

    def setValue(self, val):
        self.value = val

# END Tile Class #


# Finds the next empty tile on the board
def findEmpty(board):
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 0:
                    return i, j     # row, col

        return None


# Determines if a supposed number is valid in a given position
def valid(board, num, position):

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


def redraw_window(window, board):
    window.fill(pygame.Color('#111111'))
    board.draw()


def main():

    # Declaring window size and board
    window_size = (540, 540)

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

    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Sudoku")
    board = Grid(window, board)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.solve()

        redraw_window(window, board)
        pygame.display.update()

main()
pygame.quit()
