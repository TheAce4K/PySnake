from Board import Board
from Snake import Snake
import numpy as np

class Game:

    def __init__(self, snake, board):
        self.snake = snake
        self.board = board
        self.gameover = False
        self.direction = 'N'

    def getsnake(self):
        return self.snake

    def setsnake(self, snake):
        self.snake = snake

    def getboard(self):
        return self.board

    def setboard(self, board):
        self.board = board

    def isgameover(self):
        return self.gameover

    def setgameover(self, gameover):
        self.gameover = gameover

    def getdirection(self):
        return self.direction

    def setdirection(self, direction):
        self.direction = direction

    def getnextcell(self, currentposition):
        x = currentposition.getxpos()
        y = currentposition.getypos()

        if self.direction == 'R':
            x = x+1
        elif self.direction == 'L':
            x = x-1
        elif self.direction == 'U':
            y = y-1
        elif self.direction == 'D':
            y = y+1
        nextcell = self.board.getCells()[x,y]
        return nextcell

    def update(self):
        if not self.gameover:
            if self.direction != 'N':
                nextcell = self.getnextcell(self.snake.gethead())
                if self.snake.checkcrash(nextcell):
                    self.setdirection('N')
                    self.setgameover(True)
                else:
                    if nextcell.getcelltype() == 'FOOD':
                        self.snake.grow()
                        self.board.generatefood()
                    self.snake.move(nextcell)

