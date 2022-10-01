import random as rnd
from Cell import Cell
import numpy as np

class Board:

    def __init__(self,xcount,ycount):
        self.xcount = xcount
        self.ycount = ycount
        self.cells = np.empty((xcount+1, ycount+1), dtype=object)
        for x in range(xcount+1):
            for y in range(ycount+1):
                if x==0 or x==xcount or y==0 or y==ycount:
                    self.cells[x,y] = Cell(x, y, 'WALL')
                else:
                    self.cells[x,y] = Cell(x, y, 'EMP')
        self.generatefood()


    def getCells(self):
        return self.cells

    def setCells(self, cells):
        self.cells = cells

    def generatefood(self):
        while True:
            x = rnd.randrange(0, self.xcount - 2, 1)
            y = rnd.randrange(0, self.ycount - 2, 1)
            celltype = self.cells[x+1,y+1].getcelltype()
            if celltype == 'EMP':
                self.cells[x,y].setcelltype('FOOD')
                break
