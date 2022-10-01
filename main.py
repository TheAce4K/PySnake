import numpy as np

from Board import Board
from Snake import Snake
from Cell import Cell
from Game import Game
from tkinter import *

## options
width = 21
height = 21


initpos = Cell(round(width/2),round(height/2), 'SNAKE')
pixelsize = 60
board_width = (width+1)*pixelsize
board_height = (height+1)*pixelsize
window = Tk()
canvas = Canvas(window, width=board_width, height=board_height)
canvas.pack()


def setinput(event):
    key = event.keysym
    if key == "Up" and game.getdirection() != 'D':
        game.setdirection('U')
    elif key == 'Left' and game.getdirection() != 'R':
        game.setdirection('L')
    elif key == 'Right' and game.getdirection() != 'L':
        game.setdirection('R')
    elif key == 'Down' and game.getdirection() != 'U':
        game.setdirection('D')


window.bind('<Key>', setinput)
red = '#EE4035'
white = '#FFFFFF'
green = '#7BC043'
black = '#000000'


def paintcell(x,y,color):
    canvas.create_rectangle(x*pixelsize,y*pixelsize,(x+1)*pixelsize,(y+1)*pixelsize,fill=color)


if __name__ == '__main__':

    board = Board(width, height)
    snake = Snake(initpos)
    game = Game(snake,board)
    while not game.isgameover():

        for j in range(np.size(board.getCells(),1)):
            for i in range(np.size(board.getCells(),0)):
                if board.getCells()[i,j].getcelltype() == 'WALL':
                    paintcell(i,j,black)
                elif board.getCells()[i,j].getcelltype() == 'EMP':
                    paintcell(i,j,white)
                elif board.getCells()[i,j].getcelltype() == 'FOOD':
                    paintcell(i,j,red)
                elif board.getCells()[i,j].getcelltype() == 'SNAKE':
                    paintcell(i,j,green)
        window.after(100)
        window.update()
        game.update()






