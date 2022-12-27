import msvcrt
from os import system
from copy import deepcopy

# generic game object which contains a row, column and a character
class GenericObject:
    def __init__(self, row:int, column:int, character:str):
        self.row = row
        self.column = column
        self.character = character

# player which inherits from GenericObject and has a move function
class Player(GenericObject):
    def __init__(self, row: int, column: int, character: str, gridSize:tuple):
        super().__init__(row, column, character)
        self.gridSize = gridSize
        self.color = "\033[91m"

    def up(self, amount):
        self.row -= amount if self.row > 0 else 0
        self.character = "▲"

    def down(self, amount):
        self.row += amount if self.row < self.gridSize[0] - 1 else 0
        self.character = "▼"
        
    def left(self, amount):
        self.column -= amount if self.column > 0 else 0
        self.character = "◄"

    def right(self, amount):
        self.column += amount if self.column < self.gridSize[1] - 1 else 0
        self.character = "►"

# get direct input from user without having to use input(), eliminates 
# the use of 'enter' -> https://docs.python.org/3/library/msvcrt.html#msvcrt.getch
def getDirectInput():
    return msvcrt.getch().decode("utf-8")

# clear screen to print over it
# -> https://itnext.io/overwrite-previously-printed-lines-4218a9563527
def clearLine(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)

# generates and empty grid with dots
def generateGrid(size):
    rows, columns = size
    grid = []
    for i in range(rows):
        subGrid = []
        for j in range(columns):
            subGrid.append("\033[90m◦\033[0m")
        
        grid.append(subGrid)

    return grid

# formats the grid, adding spacing and removing brackets and commas
def formatGridRows(grid):
    formattedGrid = []
    for row in grid:
        formattedRow = []
        for character in row:
            formattedRow.append(f" {character} ")
        
        formattedGrid.append("".join(formattedRow))

    return formattedGrid

# renders the grid with all objects included, adding a border and info
def renderScreen(grid, objects):
    system("cls")
    newGrid = deepcopy(grid)
    for object in objects:
        newGrid[object.row][object.column] = f"{object.color}{object.character}\033[0m"
    
    formattedRows = formatGridRows(newGrid)

    print("━" * (GRIDSIZE[1] * 3 + 2))
    for row in formattedRows:
        print(f"┃{row}┃")
    print("━" * (GRIDSIZE[1] * 3 + 2))

    print("Controls: W - up | S - down | A - left | D - right | Q - quit")

# actual game stuff
if __name__ == "__main__":
    system("title ConsoleScreen")
    GRIDSIZE = (16, 24)

    gameGrid = generateGrid(GRIDSIZE)

    gameObjects = []

    player = Player(2, 4, "▲", GRIDSIZE)
    gameObjects.append(player)

    renderScreen(gameGrid, gameObjects)

    done = False
    while not done:
        action = getDirectInput().lower()

        match action:
            case "q":
                done = True
            case "w":
                player.up(1)
            case "s":
                player.down(1)
            case "a":
                player.left(1)
            case "d":
                player.right(1)

        renderScreen(gameGrid, gameObjects)