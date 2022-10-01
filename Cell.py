class Cell:
    def __init__(self, x, y, celltype):
        self.x=x
        self.y=y
        self.celltype=celltype

    def getcelltype(self):
        return self.celltype

    def setcelltype(self, celltype):
        self.celltype = celltype

    def getxpos(self):
        return self.x

    def getypos(self):
        return self.y

