import numpy as np
import datetime

start = datetime.datetime.now()

solved = False


def valid(grid, row, col, n):
    for x in range(9):
        if col != x and grid[row][x] == n:
            return False
    for x in range(9):
        if row != x and grid[x][col] == n:
            return False

    boxRow = row - row%3
    boxCol = col - col%3

    for x in range(3):
        for y in range(3):
            if x+boxRow != row and y+boxCol != col and grid[boxRow+x][boxCol+y] == n:
                return False
    return True


def solve(grid):
    global solution
    global solved

    if solved:
        return
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for n in range(1, 10):
                    if valid(grid, row, col, n):
                        grid[row][col] = n
                        solve(grid)
                        grid[row][col] = 0
                return

    solved = True
    solution = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            solution[i].insert(j, grid[i][j])
    print('In-Function Solution: \n', np.matrix(solution))


def getSolution(grid):
    function_start = datetime.datetime.now()
    global solution
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0 and not valid(grid, i, j, grid[i][j]):
                return []

    solve(grid)
    solution_copy = [[] for x in range(9)]
    for i in range(9):
        for j in range(9):
            solution_copy[i].insert(j, solution[i][j])
    function_finish = datetime.datetime.now()
    print('In-Function time: ', function_finish - function_start)

    return solution_copy

