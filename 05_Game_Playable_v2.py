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

        # retrieve starting questions
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
                                        text="Answer the questions",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Game Questions go here (row 2)
        game_text = "Arial 16 bold"
        game_back = "#b9ea96"  # light green
        game_width = 5
        self.game_frame = Frame(self.game_frame)
        self.game_frame.grid(row=2, pady=10)

        # Entry box... (row 2)
        self.entry_error_frame = Frame(self.game_frame)
        self.entry_error_frame.grid(row=2)

        self.low_num = Entry(self.entry_error_frame, font="Arial 19 bold", width=3)
        self.low_num.grid(row=0, column=0)

        self.to_label = Label(self.entry_error_frame, font="Arial 15 bold", width=3, padx=3)
        self.to_label.grid(row=0, column=1)

        self.high_num = Entry(self.entry_error_frame, font="Arial 19 bold", width=3)
        self.high_num.grid(row=0, column=2)

        # Play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.questions)
        self.play_button.grid(row=3)

        # Balance Label (row 4)

        start_text = "Game Cost: ${} \n "" \nHow much " \
                     "will you win?".format(operations * 5)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="green",
                                   text=start_text, wrap=300,
                                   justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game Stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Math Quiz Results...",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#66O000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):
        # retrieve the balance from the initial function...
        current_results = self.results.get()

        right_answers = 0
        wrong_answers = 0
        backgrounds = []

        # Set math quiz results to new results
        self.results.set(current_results)

        results_statement = "Results: ${}\nPayback: ${} \n" \
                            "Current Results: ${}".format(right_answers,
                                                          wrong_answers,
                                                          current_results)

        # Edit label so user can see their balance
        self.balance_label.configure(text=results_statement)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    something = Start(root)
    root.mainloop()
