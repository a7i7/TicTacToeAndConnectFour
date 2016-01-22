
import tkinter
import random
from itertools import permutations

class TicTacToeBoard:
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

        # use as a pseudo private attribute, read only
        self._winning_combos = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                      {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
                      {1, 5, 9}, {3, 5, 7}]

        # design to fit tkinter grid(row, col)two params
        self.unused_squares_dict = { '00': 1, '10': 2, '20': 3,
                                     '01': 4, '11': 5, '21': 6,
                                     '02': 7, '12': 8, '22': 9  }

        # create a main container for board
        self.container = tkinter.Frame(self.parent)
        self.container.pack()

        # create canvas for container
        self.canvas = tkinter.Canvas(self.container,
                                     width= self.sq_size * 3,
                                     height= self.sq_size * 3)
        # register main canvas
        self.canvas.grid()

    def get_unused_squares_dict(self):
        return self.unused_squares_dict

    def reset_unused_squares_dict(self):
        self.unused_squares_dict = { '00': 1, '10': 2, '20': 3,
                                     '01': 4, '11': 5, '21': 6,
                                     '02': 7, '12': 8, '22': 9  }

    def draw_board(self):
        for row in range(3):
            for column in range(3):
                self.canvas.create_rectangle(self.sq_size  * column,
                                        self.sq_size  * row,
                                        self.sq_size  * (column + 1),
                                        self.sq_size  * (row + 1),
                                        fill = self.color)

    def get_row_col(self, evt):
        # get the row and col from event's x and y coords
        return evt.x, evt.y

    def floor_of_row_col(self, col, rw):
        """
        normalize col and row number for all board size by taking
        the floor of event's x and y coords as col and row, respectively
        """
        col_flr = col // self.sq_size
        rw_flr = rw // self.sq_size
        return col_flr, rw_flr

    def convert_to_key(self, col_floor, row_floor):
        # turn col and row's quotient into a string for the key
        return str(col_floor) + str(row_floor)

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

        # convert to key, use key to locate position in 3x3 grid
        rowcol_key_str = self.convert_to_key(column_floor, row_floor)

        corner_column = (column_floor * self.sq_size) + self.sq_size
        corner_row =  (row_floor  * self.sq_size) + self.sq_size
        print("rowcol_key_str: " + str(rowcol_key_str))
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

    @property
    def winning_combos(self):
        return self._winning_combos
