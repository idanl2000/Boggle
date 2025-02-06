##############################################################################
# FILE: boggle_game.py
# EXERCISE: Intro2cs ex11 2022-2023
# WRITER: Idan Lieberman
# DESCRIPTION:A class file that handel the game
##############################################################################
#Impots
from boggle_board_randomizer import randomize_board
from typing import Any, Optional, List, Tuple, Dict
##############################################################################

class BoogleGame:
    """a class to hundel the logic in the game"""
    def __init__(self, words_leagle):
        self._word = ''
        self._word_list = []
        self._words_leagle = words_leagle
        self._board = randomize_board()
        self._key_clicked = None
        self._mouse_loc = None
        self._path = []
        self._score = 0

    def get_score(self):
        """:return score"""
        return self._score

    def get_word(self):
        """:return word"""
        return self._word

    def get_word_list(self):
        """:return word_list"""
        return self._word_list

    def get_board(self):
        """:return the board in display form"""
        return [[item + ' ' if len(item) == 1 else item for item in row] for row in self._board]

    def del_word(self):
        """del the current path and word and start new"""
        self._word = ''
        self._path = []
        self._mouse_loc = None

    def find_word(self):
        """serch if current word is in word list"""
        if self._word not in self._word_list:
            if self._word in self._words_leagle:
                self._word_list.append(self._word)
                self._score += len(self._path) ** 2
                self._word = ''
                self._path = []
                self._mouse_loc = None
                return True
        return False

    def read_key(self, key_clicked: Optional[Tuple])-> None:
        """get the input of the game from GameDisplay"""
        self._key_clicked = key_clicked

    def update_word(self):
        """
        update the game if there new inpute
        :return True if on succses else False
        """
        if self._key_clicked:
            row, col = self._key_clicked
            if self._mouse_loc == None or self.leagel_move(row, col):
                self._mouse_loc = self._key_clicked
                self._word += self._board[row][col]
                self._path.append(self._key_clicked)
                self._key_clicked = None
                return True
        return False

    def leagel_move(self, row, col):
        """
        check if the input is leagle
        :return True if legeal else False
        """
        mouse_row, mouse_col = self._mouse_loc
        if -1 <= mouse_row - row <= 1 and -1 <= mouse_col - col <= 1 and (row, col) not in self._path:
            return True
        else:
            return False

    def new_game(self):
        """start a new game"""
        self._word = ''
        self._word_list = []
        self._board = randomize_board()
        self._mouse_loc = None
        self._path = []
        self._score = 0
