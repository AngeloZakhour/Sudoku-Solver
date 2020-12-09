import pygame
import SudokuSolver
import datetime

pygame.init()

SCREEN_WIDTH = 699
SCREEN_HEIGHT = 775

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sudoku Solver')

# Board Color Variables
bg = (255, 255, 255)
gridColor = (0, 0, 0)
gridTextColor = (0, 0, 0)
highlight = (255, 255, 128)
baseColor = (255, 255, 255)
solvedCellsColor = (163, 205, 255)

# Board Variables
cellSize = 65
gridX = 57
gridY = 57
cellFont = pygame.font.SysFont('TimesNewRoman', 50)
wrongColor = (235, 21, 21)

# Button Color Variables
buttonColor = (0, 114, 252)
pressedButtonColor = (129, 185, 252)
currentButtonColor = buttonColor
buttonTextColor = (0, 0, 0)

# Button Variables
buttonX = gridX + (3*cellSize)
buttonY = gridY + (9*cellSize)+35
buttonWidth = 3*cellSize
buttonHeight = 60
buttonRect = (buttonX, buttonY, buttonWidth, buttonHeight)
buttonFont = pygame.font.SysFont('TimesNewRoman', 35)
buttonText = buttonFont.render("SOLUTION", True, buttonTextColor)

# Other Variables
selectedCells = []
broken = False
grid = [[] for x in range(9)]


class Cell(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = 0
        self.color = baseColor
        self.previousColor = baseColor

    def draw(self, win):
        pygame.draw.rect(win, self.color,
                         (gridX + (self.col * cellSize), gridY + (self.row * cellSize), cellSize, cellSize))
        if self.value > 0:
            text = cellFont.render(str(self.value), True, (0, 0, 0))
            win.blit(text, (gridX + (self.col*cellSize) + 20, gridY + (self.row*cellSize) + 5))


def redrawGameWindow():
    global cellList
    win.fill(bg)

    for row in cellList:
        for cell in row:
            cell.draw(win)

    for i in range(9):
        for j in range(9):
            pygame.draw.rect(win, gridColor, (gridX + (j * cellSize), gridY + (i * cellSize), cellSize, cellSize), 1)
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(win, gridColor,
                             (gridX + (j * 3 * cellSize), gridY + (i * 3 * cellSize), 3 * cellSize, 3 * cellSize), 3)

    pygame.draw.rect(win, currentButtonColor, buttonRect)
    pygame.draw.rect(win, gridColor, buttonRect, 2)
    win.blit(buttonText, (buttonX + 10, buttonY+10))

    pygame.display.update()


def allCellsWhite():
    global cellList
    for row in cellList:
        for cell in row:
            cell.color = baseColor


# initialization of grid Cells
cellList = [[]for i in range(9)]
for i in range(9):
    for j in range(9):
        cellList[i].insert(j, Cell(i, j))

# main loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                for cell in selectedCells:
                    cellList[cell[0]][cell[1]].color = baseColor
                    selectedCells.remove(cell)
                if gridX <= pos[0] <= gridX + (9*cellSize) and gridY <= pos[1] <= gridY + (9*cellSize):
                    colpos = (pos[0]-gridX) // cellSize
                    rowpos = (pos[1]-gridY) // cellSize
                    cellList[rowpos][colpos].color = highlight
                    selectedCells.append([rowpos, colpos])
                if buttonX <= pos[0] <= buttonX + buttonWidth and buttonY <= pos[1] <= buttonY + buttonHeight:
                    currentButtonColor = pressedButtonColor
        if event.type == pygame.MOUSEBUTTONUP:
            if not pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if buttonX <= pos[0] <= buttonX + buttonWidth and buttonY <= pos[1] <= buttonY + buttonHeight:
                    currentButtonColor = buttonColor
                    start = datetime.datetime.now()
                    for i in range(9):
                        for j in range(9):
                            grid[i].insert(j, cellList[i][j].value)
                    for i in range(9):
                        for j in range(9):
                            if grid[i][j] != 0:
                                if not SudokuSolver.valid(grid, i, j, grid[i][j]):
                                    broken = True
                                    cellList[i][j].color = wrongColor
                    if not broken:
                        SudokuSolver.solved = False
                        solution_grid = SudokuSolver.getSolution(grid)
                        if solution_grid:
                            for i in range(9):
                                for j in range(9):
                                    cellList[i][j].value = solution_grid[i][j]
                                    if solution_grid[i][j] != grid[i][j]:
                                        cellList[i][j].color = solvedCellsColor
                    broken = False
                    finish = datetime.datetime.now()
                    print(finish - start)


        keys = pygame.key.get_pressed()

        if keys[pygame.K_1] or keys[pygame.K_KP1]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 1
            allCellsWhite()
        if keys[pygame.K_2] or keys[pygame.K_KP2]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 2
            allCellsWhite()
        if keys[pygame.K_3] or keys[pygame.K_KP3]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 3
            allCellsWhite()
        if keys[pygame.K_4] or keys[pygame.K_KP4]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 4
            allCellsWhite()
        if keys[pygame.K_5] or keys[pygame.K_KP5]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 5
            allCellsWhite()
        if keys[pygame.K_6] or keys[pygame.K_KP6]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 6
            allCellsWhite()
        if keys[pygame.K_7] or keys[pygame.K_KP7]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 7
            allCellsWhite()
        if keys[pygame.K_8] or keys[pygame.K_KP8]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 8
            allCellsWhite()
        if keys[pygame.K_9] or keys[pygame.K_KP9]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 9
            allCellsWhite()
        if keys[pygame.K_DELETE] or keys[pygame.K_BACKSPACE]:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].value = 0
            allCellsWhite()

        if keys[pygame.K_UP] and selectedCells and selectedCells[0][0] > 0:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].color = cellList[cell[0]][cell[1]].previousColor

            selectedCells = [selectedCells[0]]
            selectedCells[0][0] -= 1

            selectedCell = cellList[selectedCells[0][0]][selectedCells[0][1]]
            selectedCell.previousColor = selectedCell.color
            selectedCell.color = highlight

        if keys[pygame.K_DOWN] and selectedCells and selectedCells[0][0] < 8:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].color = cellList[cell[0]][cell[1]].previousColor

            selectedCells = [selectedCells[0]]
            selectedCells[0][0] += 1

            selectedCell = cellList[selectedCells[0][0]][selectedCells[0][1]]
            selectedCell.previousColor = selectedCell.color
            selectedCell.color = highlight

        if keys[pygame.K_LEFT] and selectedCells and selectedCells[0][1] > 0:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].color = cellList[cell[0]][cell[1]].previousColor

            selectedCells = [selectedCells[0]]
            selectedCells[0][1] -= 1

            selectedCell = cellList[selectedCells[0][0]][selectedCells[0][1]]
            selectedCell.previousColor = selectedCell.color
            selectedCell.color = highlight

        if keys[pygame.K_RIGHT] and selectedCells and selectedCells[0][1] < 8:
            for cell in selectedCells:
                cellList[cell[0]][cell[1]].color = cellList[cell[0]][cell[1]].previousColor

            selectedCells = [selectedCells[0]]
            selectedCells[0][1] += 1

            selectedCell = cellList[selectedCells[0][0]][selectedCells[0][1]]
            selectedCell.previousColor = selectedCell.color
            selectedCell.color = highlight

        if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
            start = datetime.datetime.now()
            for i in range(9):
                for j in range(9):
                    grid[i].insert(j, cellList[i][j].value)
            for i in range(9):
                for j in range(9):
                    if grid[i][j] != 0:
                        if not SudokuSolver.valid(grid, i, j, grid[i][j]):
                            broken = True
                            cellList[i][j].color = wrongColor
            if not broken:
                SudokuSolver.solved = False
                solution_grid = SudokuSolver.getSolution(grid)
                if solution_grid:
                    for i in range(9):
                        for j in range(9):
                            cellList[i][j].value = solution_grid[i][j]
                            if solution_grid[i][j] != grid[i][j]:
                                cellList[i][j].color = solvedCellsColor
            broken = False
            finish = datetime.datetime.now()
            print(finish - start)

        if keys[pygame.K_ESCAPE]:
            grid = [[] for x in range(9)]
            for row in range(9):
                for col in range(9):
                    cellList[row][col].value = 0
                    cellList[row][col].color = baseColor

    redrawGameWindow()

pygame.quit()

