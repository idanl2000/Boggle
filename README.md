# Boggle

#Overview:
This project is an implementation of the classic Boggle word game.
Players attempt to form words by connecting adjacent letters on a randomly generated Boggle board.
The game includes functionalities for board generation,
word validation, and scoring.

#Files Description
- boggle.py: Contains the main logic for running the Boggle game, including board setup, user interaction, and game flow.
- boggle_board_randomizer.py: Handles the random generation of the Boggle board.
- boggle_dict.txt: A text file containing a dictionary of valid words for the game.
- boggle_game.py: Implements the game mechanics, including word validation, scoring, and gameplay rules.
- game_display.py: Manages the graphical user interface (GUI) for displaying the game board and user interactions.
- utils.py: Provides utility functions used across the game, such as board processing and helper methods.

#How to Run:
1.Ensure you have Python installed (version 3.x recommended).
2.Clone or download the repository.
3.Run the game using the following command:
4.python boggle.py
5.use mouse to play the game

#Game Rules:
- Words must be formed by connecting adjacent letters (horizontally, vertically, or diagonally).
- Each letter can only be used once per word.
- Words must be at least 3 letters long.
- Words must exist in the provided dictionary (boggle_dict.txt).

