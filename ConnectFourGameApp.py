import tkinter
import random
from itertools import permutations
from ConnectFourBoard import *
from Player import *

class ConnectFourGameApp(object):
    """
    GameApp class as controller for board and player objects

    Attributes:
    parent: (tkinter.Tk) the root window, parent of the frame
    board: instance of the board class
    unused_squares_dict: keep track of squares left on the board
    player1: instance of player class
    player2: ibid
    computer: ibid
    """

    def __init__(self, parent):
        self.parent = parent

        # create a board
        self.board = ConnectFourBoard(self.parent, 50, "#ECECEC")  # hex color gray
        self.board.draw_board()

        # create all players instances
        self.player1 = Player("Player 1", "#446CB3") # hex blue
        self.player2 = Player("Player 2", "#F4D03F") # hex yellow
        self.initialize_buttons()
        self.show_menu()

    def initialize_buttons(self):
        
        #  --- create buttons for menu ---
        self.two_players_button = tkinter.Button(self.board.container,
                                text = "PLAY WITH A FRIEND",
                                width = 25,
                                command = self.init_two_players_game)

        self.reset_button = tkinter.Button(self.board.container,
                                           text = "RESET",
                                           width = 25,
                                           command = self.restart)

    def show_menu(self):
         # register buttons to board's container
        self.two_players_button.grid()

    def init_two_players_game(self):
        # reset players' squares to empty set
        self.player1.selected_sq = set()
        self.player2.selected_sq = set()

        # keep track of turns
        self.player1_turn = True

        # show reset button
        self.reset_button.grid()

        #bind play() to the leftmost button click, for macs
        #windows or other pcs might be "<Button-2>"
        self.buttonid = self.board.canvas.bind("<Button-1>", self.play)

    def restart(self):
        """ Reinitialize the game and board after restart button is pressed """
        self.board.container.destroy()
        # create a new board object and draw board + buttons again
        self.board = ConnectFourBoard(self.parent, 50, "#ECECEC")
        self.board.draw_board()
        self.initialize_buttons()
        self.show_menu()

    def add_to_player_sq(self, key, player_sq):
        """
        use key of col and row to locate position of square
        and add square to player's selected_sq set
        :param key: str concat of col and row key str
        """
        current_selected_sq = self.board.unused_squares_dict[key]
        print("current selected sq  ---->", current_selected_sq)
        print("BEFORE player selected_sq: ", player_sq)
        player_sq.add(current_selected_sq)   # player 1 = {1}
        print("AFTER player selected_sq: ", player_sq)

    def delete_used_sq(self, key):
        # delete selected sq in self.board.unused_squares_dict
        print(" ---- square to delete ---: ", self.board.unused_squares_dict[key])
        print("unused squares dictionary before: ", self.board.unused_squares_dict)
        del self.board.unused_squares_dict[key]
        print("unused squares dictionary after: ", self.board.unused_squares_dict)

    def play(self, event):
        """  method is invoked when the user clicks on a square
        handles click event on UI for player
        Params: event (as mouse click, with x/y coords)
        """

        # locate second column and row when player click on a square
        colrow_tuple = self.board.find_coords_of_selected_sq(event)
        # save the col and row as variable
        corner_two_col, corner_two_row = colrow_tuple[0], colrow_tuple[1]

        if(self.board.is_full(event)):
            print "COLUMN IS FULL"
            return

        if self.player1_turn==True:
            self.board.insert_piece(self.player1,event)
            if(self.board.check_for_winner(self.player1)):
                self.show_game_result(self.player1.name+" WINS!")
            self.player1_turn=False
        else:
            self.board.insert_piece(self.player2,event)
            if(self.board.check_for_winner(self.player2)):
                self.show_game_result(self.player2.name+" WINS!")
            self.player1_turn=True

        if(self.board.check_for_draw()):
            self.show_game_result("Its a TIE!!")



    def show_game_result(self, txt):
        """
        make a label to display three possible winning conditions
        params: txt to display the winner
                player_color to display matching color as player's sq
        """
        result_label = tkinter.Label(self.board.container,
                                            text= txt,
                                            width = 12,
                                            height = 5,
                                            foreground = "red",
                                            background = "gray",
                                            borderwidth = 3)

        result_label.grid(row = 0, column = 0)
        # unbind button so player cannot click on square
        self.board.canvas.unbind("<Button-1>")
