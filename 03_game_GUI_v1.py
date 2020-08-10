from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get questions for quiz
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.submit_button = Button(text="Submit", command=self.to_game)
        self.submit_button.grid(row=0, pady=10)

    def to_game(self):
        # retrieve starting questions
        starting_questions = 50
        operations = 2
        low = 1
        high = 12

        Game(self, operations, starting_questions)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, operations, starting_questions):
        print(operations)
        print(starting_questions)

        # initialise variables
        self.balance = IntVar()
        # Set starting balance to amount entered by user at the start of the game
        self.balance.set(starting_questions)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Answer the questions below",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Entry box... (row 2)
        self.entry_error_frame = Frame(self.game_frame)
        self.entry_error_frame.grid(row=3)

        self.answer_entry = Entry(self.entry_error_frame,
                                  font="Arial 19 bold", width=3)
        self.answer_entry.grid(row=0, column=0)

        # Score Label (row 4)

        start_text = "Game Score:  \n "

        self.score_label = Label(self.game_frame, font="Arial 12 bold", fg="green",
                                 text=start_text, wrap=300,
                                 justify=LEFT)
        self.score_label.grid(row=4, pady=10)

        # Help and Game Stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Math Quiz Stats...",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def to_quit(self):
        print("hello world")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    Start(root)
    root.mainloop()
