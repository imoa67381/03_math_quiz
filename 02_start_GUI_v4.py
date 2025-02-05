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

        self.number_questions = IntVar()
        self.number_questions.set(0)

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
                                      command=lambda: self.to_quiz(1),
                                      font=button_font, bg="Lavender", width=10)
        self.addition_button.grid(row=8, column=1, padx=5, pady=10)

        # Subtraction button...
        self.subtraction_button = Button(self.buttons_frame, text="Subtraction",
                                         command=lambda: self.to_quiz(2),
                                         font=button_font, bg="PeachPuff", width=10)
        self.subtraction_button.grid(row=9, column=1, padx=5, pady=10)

        # Multiplication button ...
        self.multiplication_button = Button(self.buttons_frame, text="Multiplication",
                                            command=lambda: self.to_quiz(3),
                                            font=button_font, bg="MistyRose2", width=10)
        self.multiplication_button.grid(row=10, column=1, padx=5, pady=10)

        # Division button ...
        self.division_button = Button(self.buttons_frame, text="Division",
                                      command=lambda: self.to_quiz(4),
                                      font=button_font, bg="light cyan", width=10)
        self.division_button.grid(row=11, column=1, padx=5, pady=10)

        # Help Button (row 12)
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=12, pady=10)

    def to_quiz(self, buttons):

        # number of questions
        amount_questions = self.amount_questions_entry.get()
        starting_low_num = self.low_num_entry.get()
        starting_high_num = self.high_num_entry.get()

        amount_feedback = ""

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
            amount_questions = int(amount_questions)

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
            elif amount_questions <= 0:
                has_errors = "yes"
                amount_feedback = "Sorry the least you " \
                                  "can start with is 1"
            elif amount_questions > 50:
                has_errors = "yes"
                amount_feedback = "Too high! The highest you can use " \
                                  "is 50."

            elif amount_questions >= 1:
                self.number_questions.set(amount_questions)

        except ValueError:
            has_errors = "yes"
            amount_feedback = "Please enter a number (no text/ decimals)"

        if has_errors == "yes":
            self.low_num_entry.config(bg=error_back)
            self.high_num_entry.config(bg=error_back)
            self.amount_questions_entry.config(bg=error_back)
            self.amount_error_label.config(text=amount_feedback)

        else:
            # code to start game
            self.number_questions.set(amount_questions)

            amount_questions = self.number_questions.get()
            starting_low_num = self.low_num_entry.get()
            starting_high_num = self.high_num_entry.get()

            Quiz(self, buttons, amount_questions, starting_low_num, starting_high_num)

            # hide start up menu
            root.withdraw()

    def to_help(self):
        print("Help")


class Quiz:
    def __init__(self, partner, buttons, amount_questions_entry, starting_low_num, starting_high_num):
        print("operation", buttons)
        print("num questions", amount_questions_entry)
        print("low_num", starting_low_num)
        print("high_num", starting_high_num)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    Start(root)
    root.mainloop()
