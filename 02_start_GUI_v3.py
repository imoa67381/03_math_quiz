from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get questions and buttons
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Math Quiz Heading (row 0)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz Game",
                                     font="Arial 17 bold",
                                     padx=10, pady=10)
        self.math_quiz_label.grid(row=0)

        # Initial Instructions for numbers used in questions(row 1)

        math_quiz_instructions = "Enter numbers between -20 and 50 below "

        self.math_quiz_label = Label(self.start_frame, font="Arial 11 italic",
                                     text=math_quiz_instructions,
                                     wrap=275, justify=LEFT, padx=10, pady=10)
        self.math_quiz_label.grid(row=1)

        # Entry box... (row 2)
        self.entry_error_frame = Frame(self.start_frame)
        self.entry_error_frame.grid(row=2)

        self.low_num_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=3)
        self.low_num_entry.grid(row=0, column=0)

        self.to_label = Label(self.entry_error_frame, text="to", font="Arial 15 bold", width=3, padx=3)
        self.to_label.grid(row=0, column=1)

        self.high_num_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=3)
        self.high_num_entry.grid(row=0, column=2)

        self.entry_error_label = Label(self.start_frame, fg="maroon",
                                       text="", font="Arial 10 bold", wrap=275,
                                       justify=LEFT)
        self.entry_error_label.grid(row=3, columnspan=2, pady=5)

        # Initial Instructions for amount of questions (row 4)

        math_quiz_instructions = "Enter amount of questions below "

        self.math_quiz_label = Label(self.start_frame, font="Arial 11 italic",
                                     text=math_quiz_instructions,
                                     wrap=275, justify=LEFT, padx=10, pady=10)
        self.math_quiz_label.grid(row=4)

        # Number of questions entry box... (row 5)
        self.amount_questions_entry = Entry(self.start_frame, font="Arial 19 bold", width=2)
        self.amount_questions_entry.grid(row=5)

        self.amount_error_label = Label(self.start_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=6, columnspan=2, pady=5)

        # button frame (row 7)
        self.buttons_frame = Frame(self.start_frame)
        self.buttons_frame.grid(row=7)

        # Buttons go here...
        button_font = "Arial 15 bold"
        # Addition button ...
        self.addition_button = Button(self.buttons_frame, text="Addition",
                                      command=lambda: self.to_game(1),
                                      font=button_font, bg="Lavender", width=10)
        self.addition_button.grid(row=8, column=1, padx=5, pady=10)

        # Subtraction button...
        self.subtraction_button = Button(self.buttons_frame, text="Subtraction",
                                         command=lambda: self.to_game(2),
                                         font=button_font, bg="PeachPuff", width=10)
        self.subtraction_button.grid(row=9, column=1, padx=5, pady=10)

        # Multiplication Button ...
        self.multiplication_button = Button(self.buttons_frame, text="Multiplication",
                                      command=lambda: self.to_game(3),
                                      font=button_font, bg="MistyRose2", width=10)
        self.multiplication_button.grid(row=10, column=1, padx=5, pady=10)

        # Division Button ...
        self.division_button = Button(self.buttons_frame, text="Division",
                                      command=lambda: self.to_game(4),
                                      font=button_font, bg="light cyan", width=10)
        self.division_button.grid(row=11, column=1, padx=5, pady=10)

        # Disable all stakes buttons at start
        self.addition_button = Button(state=DISABLED)
        self.subtraction_button = Button(state=DISABLED)

        # Help Button (row 11)
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=12, pady=10)

    def check_num(self):
        starting_questions = self.amount_questions_entry.get()
        starting_low_num = self.low_num_entry.get()
        starting_high_num = self.high_num_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white (for testing purposes) ...
        self.low_num_entry.config(bg="white")
        self.entry_error_label.config(text="")
        self.high_num_entry.config(bg="white")
        self.entry_error_label.config(text="")
        self.amount_questions_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # Disable all operations button in case user changes mind and
        self.addition_button.config(state=DISABLED)
        self.subtraction_button.config(state=DISABLED)

        try:
            starting_low_num = int(starting_low_num)
            starting_high_num = int(starting_high_num)
            starting_questions = int(starting_questions)

            if starting_low_num < -20:
                has_errors = "yes"
                error_feedback = "Sorry the least you " \
                                 "can start with is -20"
                self.entry_error_label.config(text=error_feedback)
            elif starting_high_num > 50:
                has_errors = "yes"
                error_feedback = "Too high! The highest you can use " \
                                 "is 50."
                self.entry_error_label.config(text=error_feedback)
            elif starting_questions < 0:
                has_errors = "yes"
                amount_feedback = "Sorry the least you " \
                                  "can start with is 1"
            elif starting_questions > 50:
                has_errors = "yes"
                amount_feedback = "Too high! 50 questions or less " \

        except ValueError:
            has_errors = "yes"
            amount_feedback = "Please enter a number (no text / decimals)"

        if has_errors == "yes":
            self.low_num_entry.config(bg=error_back)
            self.high_num_entry.config(bg=error_back)
            self.amount_questions_entry.config(bg=error_back)
            self.amount_error_label.config(text=amount_feedback)
            return "not ok"

        else:
            return "ok"

    def to_game(self, buttons):

        # get data from entry boxes

        ok = self.check_num()

        if ok == "ok":
            # number of questions
            starting_questions = self.amount_questions_entry.get()
            starting_questions = int(starting_questions)
            print("starting questions to check", starting_questions)

            # low number
            starting_low_num = self.low_num_entry.get()
            starting_low_num = int(starting_low_num)
            print("low num questions to check", starting_low_num)

            # high number
            starting_high_num = self.high_num_entry.get()
            starting_high_num = int(starting_high_num)
            print("high num questions to check", starting_high_num)

            # Game(self, buttons, starting_questions)

            # hide start up window
            root.withdraw

            # Set error background colours (and assume that there are no
            # errors at the start...
            error_back = "#ffafaf"
            has_errors = "no"

            # change background to white (for testing purposes) ...
            self.low_num_entry.config(bg="white")
            self.entry_error_label.config(text="")
            self.high_num_entry.config(bg="white")
            self.entry_error_label.config(text="")
            self.amount_questions_entry.config(bg="white")
            self.amount_error_label.config(text="")

            try:
                starting_low_num = int(starting_low_num)
                starting_high_num = int(starting_high_num)
                starting_questions = int(starting_questions)

                if starting_low_num < -20:
                    has_errors = "yes"
                    error_feedback = "Sorry the least you " \
                                     "can start with is -20"
                    self.entry_error_label.config(text=error_feedback)
                elif starting_high_num > 50:
                    has_errors = "yes"
                    error_feedback = "Too high! The highest you can use " \
                                     "is 50."
                    self.entry_error_label.config(text=error_feedback)
                elif starting_questions < 0:
                    has_errors = "yes"
                    amount_feedback = "Sorry the least you " \
                                      "can start with is 1"
                elif starting_questions > 50:
                    has_errors = "yes"
                    amount_feedback = "Too high! The highest you can use " \
                                      "is 50."

            except ValueError:
                has_errors = "yes"
                amount_feedback = "Please enter a number (no text/ decimals)"

            if has_errors == "yes":
                self.low_num_entry.config(bg=error_back)
                self.high_num_entry.config(bg=error_back)
                self.amount_questions_entry.config(bg=error_back)
                self.amount_error_label.config(text=amount_feedback)

            else:
                Game(self, buttons, starting_questions)


class Game:
    def __init__(self, partner, buttons, starting_questions):
        print("operation", buttons)
        print("num questions", starting_questions)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    Start(root)
    root.mainloop()