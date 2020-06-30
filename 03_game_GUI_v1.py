from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, partner):

        # GUI to get starting balance and high and low number
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.submit_button = Button(text="Submit", command=self.to_game)
        self.submit_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        operations = 2

        Game(self, operations, starting_balance)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, operations, starting_balance):
        print(operations)
        print(starting_balance)

        # initialise variables
        self.balance = IntVar()
        # Set starting balance to amount entered by user at the start of the game
        self.balance.set(starting_balance)

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.game_frame, warp=300, justify=LEFT,
                                        text="Press <enter> or click the 'Open"
                                        "")

