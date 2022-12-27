import msvcrt
from os import system
from copy import deepcopy

# generic game object which contains a row, column and a character
class GenericObject:
    def __init__(self, row:int, column:int, character:str) -> None:
        self.row = row
        self.column = column
        self.character = character

# player which inherits from GenericObject and has a move function
class Player(GenericObject):
    def up(self, amount):
        self.row -= amount

    def down(self, amount):
        self.row += amount
        
    def left(self, amount):
        self.column -= amount

    def right(self, amount):
        self.column += amount

# get direct input from user without having to use input(), eliminates 
# the use of 'enter' -> https://docs.python.org/3/library/msvcrt.html#msvcrt.getch
def getDirectInput():
    return msvcrt.getch().decode("utf-8")

# generates and empty grid with dots
def generateGrid(rows, columns):
    grid = []
    for i in range(rows):
        subGrid = []
        for j in range(columns):
            subGrid.append("∙")
        
        grid.append(subGrid)

    return grid

# formats the grid, adding spacing and removing brackets and commas
def formatGrid(grid):
    formattedGrid = []
    for row in grid:
        formattedRow = []
        for character in row:
            formattedRow.append(f" {character} ")
        
        formattedGrid.append("".join(formattedRow))

    return "\n".join(formattedGrid)

# renders the grid with all objects included
def renderScreen(grid, objects):
    system("cls")
    newGrid = deepcopy(grid)
    for object in objects:
        newGrid[object.row][object.column] = object.character
    
    print(formatGrid(newGrid))


# actual game stuff
gameGrid = generateGrid(15, 20)

gameObjects = []

player = Player(2, 4, "O")
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