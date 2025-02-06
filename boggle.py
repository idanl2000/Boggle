##############################################################################
# FILE: boggle.py
# WRITER: Idan Lieberman
# DESCRIPTION:The main file to run the game
##############################################################################
#Imports
from boggle_game import BoogleGame
from game_display import GameDisplay
##############################################################################
if __name__ == "__main__":
    s = set()
    with open('boggle_dict.txt') as html_list:
        for word in html_list:
            s.add(word.strip('\n'))
    game = BoogleGame(s)
    gd = GameDisplay(game)
    gd.start()
