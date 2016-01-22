import tkinter
import random
from itertools import permutations

ROWS = 6
COLUMNS = 7
class ConnectFourBoard:
    """
    Board class to be used in the Game obj

    Attributes:
    sq_size: integer to set size of each squares
    color: hex code to color the board size
    """

    def __init__(self, parent, sq_size, color):
        self.parent = parent   # parent is root
        self.sq_size = sq_size
        self.color = color
        self.game_pieces = []

        for i in range(ROWS):
            tmp = []
            for j in range(COLUMNS):
                tmp.append(None)
            self.game_pieces.append(tmp)

        # create a main container for board
        self.container = tkinter.Frame(self.parent)
        self.container.pack()

        # create canvas for container
        self.canvas = tkinter.Canvas(self.container,
                                     width= self.sq_size * COLUMNS,
                                     height= self.sq_size * ROWS)
        # register main canvas
        self.canvas.grid()

    def draw_board(self):
        for row in range(ROWS):
            for column in range(COLUMNS):
                self.canvas.create_rectangle(self.sq_size  * column,
                                        self.sq_size  * row,
                                        self.sq_size  * (column + 1),
                                        self.sq_size  * (row + 1),
                                        fill = self.color)


    def get_row_col(self, evt):
        return evt.x, evt.y


    def floor_of_row_col(self, col, rw):
        """
        normalize col and row number for all board size by taking
        the floor of event's x and y coords as col and row, respectively
        """
        col_flr = col // self.sq_size
        rw_flr = rw // self.sq_size
        return col_flr, rw_flr

    def insert_piece(self,player,evt):
        column,row = self.get_row_col(evt)
        column_floor,row_floor = self.floor_of_row_col(column,row)   

        for i in range(ROWS-1,-1,-1):
            if(self.game_pieces[i][column_floor]==None):
                self.game_pieces[i][column_floor]=player.color
                corner_column = column_floor*self.sq_size+self.sq_size
                corner_row = i*self.sq_size+self.sq_size
                self.color_desired_square(column_floor*self.sq_size,i*self.sq_size,corner_column,corner_row,player.color)
                break
    
    def check_for_winner(self,player):
        for i in range(ROWS):
            for j in range(COLUMNS):
                try:
                    if self.game_pieces[i][j]==player.color and self.game_pieces[i+1][j]==player.color and self.game_pieces[i+2][j]==player.color and self.game_pieces[i+3][j]==player.color:
                        return True
                except IndexError:
                    pass
                try:
                    if self.game_pieces[i][j]==player.color and self.game_pieces[i][j+1]==player.color and self.game_pieces[i][j+2]==player.color and self.game_pieces[i][j+3]==player.color:
                        return True
                except IndexError:
                    pass
                try:
                    if self.game_pieces[i][j]==player.color and self.game_pieces[i+1][j+1]==player.color and self.game_pieces[i+2][j+2]==player.color and self.game_pieces[i+3][j+3]==player.color:
                        return True
                except IndexError:
                    pass
                try:
                    if self.game_pieces[i][j]==player.color and self.game_pieces[i+1][j-1]==player.color and self.game_pieces[i+2][j-2]==player.color and self.game_pieces[i+3][j-3]==player.color:
                        return True
                except IndexError:
                    pass
        return False

    def check_for_draw(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                if(self.game_pieces[i][j]==None):
                    return False
        return True

    def is_full(self,evt):
        column,row = self.get_row_col(evt)
        column_floor,row_floor = self.floor_of_row_col(column,row)   
        for i in range(ROWS-1,-1,-1):
            if(self.game_pieces[i][column_floor]==None):
                return False
        return True
    
    def find_coords_of_selected_sq(self, evt):
        """
        finding coords in a 9-sq grid

        params: event triggered by user's click
        return: tuple of two values for second corner's col, row
        """
        # saves row and col tuple into two variables
        column, row = self.get_row_col(evt)
        # normalize for all square size by keeping the floor
        column_floor, row_floor = self.floor_of_row_col(column, row)

        corner_column = (column_floor * self.sq_size) + self.sq_size
        corner_row =  (row_floor  * self.sq_size) + self.sq_size
        return corner_column, corner_row

    def color_selected_sq(self, evt, second_corner_col,
                          second_corner_row, player_color):

        print(" ---- inside color_selected_sq method ----")
        self.canvas.create_rectangle(
            (evt.x // self.sq_size) * self.sq_size,
            (evt.y // self.sq_size) * self.sq_size,
            second_corner_col,
            second_corner_row,
            fill = player_color)

    def color_desired_square(self,x1,y1,x2,y2,player_color):
        self.canvas.create_rectangle(x1,y1,x2,y2,fill = player_color)
    
    @property
    def winning_combos(self):
        return self._winning_combos
