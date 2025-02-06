##############################################################################
# FILE: game_display.py
# EXERCISE: Intro2cs ex11 2022-2023
# WRITER: Idan Lieberman
# DESCRIPTION:A class file to handel the display part of the game
##############################################################################
#Impots
import string
import tkinter

from boggle_board_randomizer import randomize_board
import tkinter as tki
from typing import Any, Optional, List, Tuple, Dict
from boggle_game import BoogleGame
##############################################################################

class GameDisplay:

    def __init__(self, game):
        """class that hundel the display part of the game"""
        self._game:BoogleGame = game
        #creating the main window
        self._root = tki.Tk()
        self._root.title("Boggle")
        #creating the right click event
        self._root.bind("<Button-3>",self._right_click)
        #creating the score frame
        self._score_var = tki.StringVar()
        self._init_score_frame()
        #creating the current word label
        self._word_lable = tki.Label(self._root,text="" ,width= 20, height = 2, font=("Courier", 22))
        self._word_lable.grid(row=1, columnspan=4)
        # Define Buttons
        self._button_list: List[tki.Button] = self._init_button_grid(self._game.get_board())
        #creating the timer
        self._time = 180
        self._do_tik = False
        self._count_down = tki.Label(text='3:00',width=20 , height= 2,
                                     background="yellow", font=("Courier", 18))
        self._count_down.grid(row=0, column=5)
        #creating the word list label
        self._word_list_var = tki.StringVar()
        self._word_list_label = tki.Label(self._root, textvariable=self._word_list_var,
                                          width=25, height=10, font=("Courier", 14))
        self._word_list_label.grid(row=1, column=5)
        self._word_list_counter = 2
        #creating the new game and exit buttons
        new_game_button = tki.Button(self._root, text= 'New Game', pady= 20, padx=32, font=("Courier", 10),
                                     background= "green", command= lambda : self.new_game())
        exit_button = tki.Button(self._root, text= 'Exit', pady= 20,  padx=53, font=("Courier", 10),
                                 background= "red", command=lambda  : self._root.destroy())

        new_game_button.grid(row=5, column=4 ,columnspan=2 ,sticky='w')
        exit_button.grid(row=5, column=5 , columnspan=2 ,sticky='e')
        #hundling not wanted function
        self._root.resizable(0,0)

    def _clean_board(self):
        """
        Internal: this method clean the button grid frome previes path
        :return: Noun
        """
        for button in self._button_list:
            button.configure(background="white")

    def _right_click(self, event):
        """
        Internal: This method hundel the right click event
        :return:Noun
        """
        self._game.del_word()
        self._word_lable.configure(text="")
        self._clean_board()

    def new_game(self):
        """
        Internal: This method start a new game
        :return:Noun
        """
        self._do_tik = False
        self._word_list_counter = 2
        self._time = 180
        #start a new game in the class Boggle_game
        self._game.new_game()
        #start a new game in the display
        self._new_game_display(self._game.get_board())

    def _new_game_display(self, board):
        """
        Internal: This method painte the new game on the board
        :return:Noun
        """
        self._word_lable.configure(text='')
        self._word_list_var.set('')
        self.show_score('Not Set')
        self._count_down.configure(text='3:00')
        for index, button in enumerate(self._button_list):
            button.configure(text= board[index//4][index%4], background= "white")

    def _init_button_grid(self, letter_mat):
        """
        Internal: This method initializes the score frame
        :return: List[Button]
        """
        class LetButton (tki.Button):
            "the button class frome tkinker"
            def __init__(self, master, i, app, *args, **kwargs):
                tki.Button.__init__(self, master, *args, **kwargs)
                self.configure(text= letter_mat[i//4][i%4], padx=30, pady=13, font=("Courier", 16),
                               command= lambda : app._button_press(i//4, i%4))
        #creating all the buttons
        button_list = [LetButton(self._root, i, self) for i in range(16)]
        #placeing all the buttons
        for i  in range(16):
            button_list[i].grid(row=2 + i//4, column=i%4, ipadx = 2, ipady = 2,sticky= "w")

        return button_list

    def _init_score_frame(self) -> None:
        """
        Internal: This method initializes the score frame
        :return: None
        """
        self._score_frame = tki.Frame(self._root)
        self._score_frame.grid(row=0 ,columnspan=4)

        self.show_score("Not Set")
        self._score_label = tki.Label(self._score_frame,
                                      borderwidth=2,
                                      relief="ridge",
                                      textvariable=self._score_var,
                                      font=("Courier", 22))

        self._score_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self._score_frame.grid_rowconfigure(0, weight=1)

    def show_score(self, val: Any) -> None:
        """
        This method updates the currently shown score on the board.
        :param val: the score we wish to display
        :return: None
        """

        print(f'Score:{val}')
        self._score_var.set("Score: " + str(val))

    def _update_count_down(self):
        "the founciton that handel the timer of the game"
        # check if the game ended
        if self._time == 0:
            # New-Game or Exit
            Popup(self._root, self)
        #check if the game started
        elif self._do_tik:
            self._time -= 1
            self._count_down.configure(text=f'{self._time // 60:<01d}:{self._time % 60:>02d}')
            self._root.after(1000, self._update_count_down)

    def start(self) -> None:
        """
        Internal: Starts the program: calls the main method and runs the GUI.
        :return: None
        """
        self._root.mainloop()

    def _button_press(self, row, col) -> None:
        """
        Internal: handel white the button press event
        :return:None
        """
        #start clock
        if self._time == 180:
            #test pop up
            #self._time = 5
            self._do_tik = True
            self._update_count_down()

        self._game.read_key((row, col))
        #chcek if leagle move and updet the game
        if self._game.update_word():
            self._button_list[row * 4 + col].configure(background="blue")
        if self._game.find_word():
            s = self._word_list_var.get() + self._game.get_word_list()[-1]
            if self._word_list_counter == 0:
                s += '\n'
                self._word_list_counter = 2
            else:
                s += ', '
                self._word_list_counter -= 1
            self._word_list_var.set(s)
            self.show_score(self._game.get_score())
            self._clean_board()
        self._word_lable.config(text=self._game.get_word())

    def get_score(self):
        "get the score for the popup"
        return self._score_var


class Popup(tki.Toplevel):
    """class that handel the pop app"""
    def __init__(self, master, app, *args):
        tki.Toplevel.__init__(self, master, *args)
        self._app = app

        self.title("Game Over")

        #creating score label
        pop_score_label = tki.Label(self,
                                  borderwidth=2,
                                  relief="ridge",
                                  textvariable=self._app.get_score(),
                                  font=("Courier", 22))
        pop_score_label.grid(row=0,column=0, columnspan=2)

        #creating buttons
        pop_exit_button = tki.Button(self, text="Exit", pady=25, padx=50,
                                     background="red", command=lambda :self._pop_button(False))
        pop_new_game_button = tki.Button(self, text="New Game", pady=25, padx=27,
                                         background="green", command= lambda :self._pop_button(True))
        pop_exit_button.grid(row=1, column=1)
        pop_new_game_button.grid(row=1, column=0)

        #handel with not wanted events
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", lambda : ...)
        self.grab_set()

    def _pop_button(self, new_game):
        "funciton that hundel the buttons inn the pop up"
        if new_game:
            self._app.new_game()
            self.destroy()
        else:
            self.master.destroy()




