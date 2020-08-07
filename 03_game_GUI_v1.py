from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Start:
    def __init__(self, parent):

        # GUI to get starting questions
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.submit_button = Button(text="Submit", command=self.to_game)
        self.submit_button.grid(row=0, pady=10)

    def to_game(self):

