#! 2048 clone using  Python graphics

from graphics import *
from random import choice, random
from math import fabs as abs

color_dict = {0: "gray", 2: "#e7e2da", 4: "#e7decf", 8: "#efdcbd", 16: "#f6d49c", 32: "#f1b85b", 64: "#e79613", 128: "#d5c8d4", 256: "#e5a9e1", 512: "#e34fda", 1024: "#e34f73", 2048: "#fa0541", 4096: "#a20128"}

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

"""
grid = [
    [0, 2, 4, 8],
    [0, 4, 4, 8],
    [256, 512, 8, 2048],
    [0, 0, 0, 8]
]
"""

squares = [ [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0] ]
textGrid = [ [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0] ]

def initGrid():  #initializes squares and calls populateEmpty()
    for y in range(4):
        for x in range(4):
            squares[x][y] = Rectangle(Point(x*100,y*100), Point((x+1)*100, (y+1)*100))
    populateEmpty()
    populateEmpty()

def updateGrid(): #updates entire grid
    for y in range(4):
        for x in range(4):
            squares[x][y] = Rectangle(Point(x*100,y*100), Point((x+1)*100, (y+1)*100))
            squares[x][y].setFill(color_dict[abs(grid[x][y])])
            if grid[x][y] != 0:
                if grid[x][y] > 0:
                    textGrid[x][y] = Text(squares[x][y].getCenter(), grid[x][y])
                else:
                    grid[x][y] = -grid[x][y]
                    textGrid[x][y] = Text(squares[x][y].getCenter(), grid[x][y])
                    textGrid[x][y].setStyle("bold italic")
                textGrid[x][y].setSize(20)
            else:
                textGrid[x][y] = Text(squares[x][y].getCenter(), "")

def drawGrid(): #draws entire grid
    for y in range(4):
        for x in range(4):
            squares[x][y].draw(grid_window)
            textGrid[x][y].draw(grid_window)

def left(): #simulates swipe-left
    for y in range(0,4):
        for x in range(0,3):
            if grid[x][y] == 0:
                for z in range(x+1,4):
                    if grid[z][y] != 0:
                        grid[x][y] = grid[z][y]
                        grid[z][y] = 0
                        break
            for z in range(x+1,4):
                if grid[x][y] == grid[z][y]:
                    grid[x][y] = 2 * grid[x][y]
                    grid[z][y] = 0
                    break
                elif grid[z][y] != 0:
                    break

def right(): #simulates swipe-right
    for y in range(0,4):
        for x in range(3,0,-1):
            if grid[x][y] == 0:
                for z in range(x-1,-1,-1):
                    if grid[z][y] != 0:
                        grid[x][y] = grid[z][y]
                        grid[z][y] = 0
                        break
            for z in range(x-1,-1,-1):
                if grid[x][y] == grid[z][y]:
                    grid[x][y] = 2 * grid[x][y]
                    grid[z][y] = 0
                    break
                elif grid[z][y] != 0:
                    break

def up(): #simulates swipe-up
    for x in range(0,4):
        for y in range(0,3):
            if grid[x][y] == 0:
                for z in range(y+1,4):
                    if grid[x][z] != 0:
                        grid[x][y] = grid[x][z]
                        grid[x][z] = 0
                        break
            for z in range(y+1,4):
                if grid[x][y] == grid[x][z]:
                    grid[x][y] = 2 * grid[x][y]
                    grid[x][z] = 0
                    break
                elif grid[x][z] != 0:
                    break

def down(): #simulates swipe-down
    for x in range(0,4):
        for y in range(3,0,-1):
            if grid[x][y] == 0:
                for z in range(y-1,-1,-1):
                    if grid[x][z] != 0:
                        grid[x][y] = grid[x][z]
                        grid[x][z] = 0
                        break
            for z in range(y-1,-1,-1):
                if grid[x][y] == grid[x][z]:
                    grid[x][y] = 2 * grid[x][y]
                    grid[x][z] = 0
                    break
                elif grid[x][z] != 0:
                    break

def populateEmpty():
    emptyTuples = []
    for y in range(4):
        for x in range(4):
            if grid[x][y] == 0:
                emptyTuples.append((x,y))
    if len(emptyTuples) > 0:
        (p,q) = choice(emptyTuples)
        if random() < 0.8:
            grid[p][q] = -2
        else:
            grid[p][q] = -4

grid_window = GraphWin("2048", 400, 400)
initGrid()
updateGrid()
drawGrid()

while(True):
    oldGrid = []
    for row in grid:
        oldGrid.append(row.copy())
    command = grid_window.getKey()
    if command == "a" or command == "Left":
        left()
    elif command == "d" or command == "Right":
        right()
    elif command == "w" or command == "Up":
        up()
    elif command == "s" or command == "Down":
        down()
    #elif command == "z":
        #grid = oldGrid
    elif command == "q":
        break
    if grid != oldGrid:
        populateEmpty()
    updateGrid()
    drawGrid()
            
    
    
    
