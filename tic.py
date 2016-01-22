import tkinter
import random
from itertools import permutations
from Player import *
from Board import *
from TicTacToeGameApp import *
from ConnectFourGameApp import *

class ChooseGameMenu(object):

    def __init__(self, parent):
        
        self.parent = parent
        self.sq_size = 100
        self.container = tkinter.Frame(self.parent)
        self.container.pack()
        self.canvas = tkinter.Canvas(self.container,
                                     width= self.sq_size * 3,
                                     height= self.sq_size * 3)
        self.canvas.grid()
        self.initialize_buttons()
        self.play_tic_tac_toe_button.grid()
        self.play_connect_four_button.grid()

    def initialize_buttons(self):

        self.play_tic_tac_toe_button = tkinter.Button(self.container,
                                text = "PLAY TIC TAC TOE",
                                width = 25,
                                command = self.play_tic_tac_toe)

        self.play_connect_four_button = tkinter.Button(self.container,
                                        text = "PLAY CONNECT FOUR",
                                        width = 25,
                                        command = self.play_connect_four)

    def play_tic_tac_toe(self):
        self.container.destroy()
        self.parent.title("TIC TAC TOE")
        TicTacToeGameApp(self.parent)

    def play_connect_four(self):
        self.container.destroy()
        self.parent.title("CONNECT FOUR")
        ConnectFourGameApp(self.parent)

def main():
    root = tkinter.Tk()
    root.title("Choose Yo Game")
    ChooseGameMenu(root)  # root is parent
    root.mainloop()

if __name__ == '__main__':
    main()