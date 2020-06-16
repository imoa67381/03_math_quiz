from tkinter import *
from functools import partial    # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI for math quiz game
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Math Quiz Heading ( row 0)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz Game",
                                     font="Arial 19 bold")
        self.math_quiz_label.grid(row=1)

        # Entry box... (row 1)
        self.start_number_checker_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_number_checker_entry.grid(row=2)

        # Entry box for number of questions... (row 2)
        self.amount_questions_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.amount_questions_entry.grid(row=2)

        # Addition Button (row 3)
        self.addition_button = Button(text="Addition",
                                      command=lambda: self.to_game(1))
        self.addition_button.grid(row=3, pady=10)

        # Subtraction Button (row 4)
        self.subtraction_button = Button(text="Subtraction",
                                         command=lambda: self.to_game(2))
        self.subtraction_button.grid(row=4, pady=10)


class Game:
    def __init__(self, partner, starting_balance):
        print(starting_balance)

        # disable addition button
        partner.addition_button.congig(state=DISABLED)

        # disable subtraction button
        partner.subtraction_button.congig(state=DISABLED)

        # initialise variables
        self.balance = IntVar()

        # Set number between questions to amount entered by user at start of game
        self.balance.set(starting_balance)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Heading",
                                                         font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    root.mainloop()
