from Board import Board

class Snake:
    def __init__(self, initpos):
        self.head = initpos
        self.head.setcelltype('SNAKE')
        self.snakepartslist = [self.head]

    def grow(self):
        self.snakepartslist.append(self.snakepartslist[-1])

    def move(self, nextcell):
        self.snakepartslist[-1].setcelltype('EMP')
        self.snakepartslist.pop(-1)
        self.head = nextcell
        self.head.setcelltype('SNAKE')
        self.snakepartslist.insert(0,self.head)

    def checkcrash(self, nextcell):
        for cell in self.snakepartslist:
            if cell == nextcell:
                return True
        if nextcell.getcelltype() == 'WALL':
            return True
        return False

    def getsnakepartslist(self):
        return self.snakepartslist

    def setsnakepartslist(self, snakepartslist):
        self.snakepartslist = snakepartslist

    def gethead(self):
        return self.head

    def sethead(self, head):
        self.head = head