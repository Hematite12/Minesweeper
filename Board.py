import random

from Cell import *
from Constants import *

class Board:
    def __init__(self):
        self.matrix = [[Cell(x, y) for x in range(SIZE)] for y in range(SIZE)]
        self.setMines()
        self.setNumbers()
        self.mineCount = NUMMINES
    
    def setMines(self):
        mineList = random.sample(range(SIZE*SIZE), NUMMINES)
        for i in mineList:
            self.matrix[i//SIZE][i%SIZE].mine = True
    
    def setNumbers(self):
        for x in range(SIZE):
            for y in range(SIZE):
                cell = self.matrix[y][x]
                if not cell.mine:
                    cell.number = self.numNeighborMines(x, y)
    
    def numNeighborMines(self, x, y):
        mines = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < SIZE and j >= 0 and j < SIZE:
                    if self.matrix[j][i].mine: mines += 1
        return mines
    
    def show(self):
        for x in range(SIZE):
            for y in range(SIZE):
                self.matrix[y][x].show()
    
    def inPosBounds(self, x, y):
        return x>MARGIN and x<XMAX and y>MARGIN and y<YMAX
    
    def getCellLoc(self, x, y):
        return ((x - MARGIN) // CELLDIM, (y - MARGIN) // CELLDIM)
    
    def checkHover(self, x, y):
        if self.inPosBounds(x, y):
            xCellLoc, yCellLoc = self.getCellLoc(x, y)
            self.matrix[yCellLoc][xCellLoc].showHover()
    
    def checkLeftClick(self, x, y):
        if self.inPosBounds(x, y):
            xCellLoc, yCellLoc = self.getCellLoc(x, y)
            cell = self.matrix[yCellLoc][xCellLoc]
            cell.pressed = True
            if cell.mine:
                self.gameOver()
            elif cell.number == 0:
                self.pressZeroes(cell)
    
    def pressZeroes(self, originCell):
        zeroCells = [originCell]
        while len(zeroCells) > 0:
            cell = zeroCells[0]
            zeroCells = zeroCells[1:]
            for i in range(cell.x-1, cell.x+2):
                for j in range(cell.y-1, cell.y+2):
                    if i >= 0 and i < SIZE and j >= 0 and j < SIZE:
                        newCell = self.matrix[j][i]
                        if not newCell.pressed:
                            newCell.pressed = True
                            if newCell.number == 0: zeroCells.append(newCell)
    
    def checkRightClick(self, x, y):
        if self.inPosBounds(x, y):
            xCellLoc, yCellLoc = self.getCellLoc(x, y)
            cell = self.matrix[yCellLoc][xCellLoc]
            if not cell.flag:
                cell.flag = True
                self.mineCount -= 1
            else:
                cell.flag = False
                self.mineCount += 1
    
    def gameOver(self):
        for i in range(SIZE):
            for j in range(SIZE):
                self.matrix[j][i].pressed = True
    
    
    
    
    
    