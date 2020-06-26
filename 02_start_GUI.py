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

        self.low_num = Entry(self.entry_error_frame, font="Arial 19 bold", width=3)
        self.low_num.grid(row=0, column=0)

        self.to_label = Label(self.entry_error_frame, text="to", font="Arial 15 bold", width=3, padx=3)
        self.to_label.grid(row=0, column=1)

        self.high_num = Entry(self.entry_error_frame, font="Arial 19 bold", width=3)
        self.high_num.grid(row=0, column=2)

        # Initial Instructions for amount of questions (row 3)

        math_quiz_instructions = "Enter amount of questions below "

        self.math_quiz_label = Label(self.start_frame, font="Arial 11 italic",
                                     text=math_quiz_instructions,
                                     wrap=275, justify=LEFT, padx=10, pady=10)
        self.math_quiz_label.grid(row=3)

        # Number of questions entry box... (row 4)
        self.amount_questions_entry = Entry(self.start_frame, font="Arial 19 bold", width=2)
        self.amount_questions_entry.grid(row=4)

        # button frame (row 5)
        self.buttons_frame = Frame(self.start_frame)
        self.buttons_frame.grid(row=5)

        # Buttons go here...
        button_font = "Arial 12 bold"
        # Addition button ...
        self.addition_button = Button(self.buttons_frame, text="Addition",
                                      command=lambda: self.to_game(1),
                                      font=button_font, bg="MistyRose2")
        self.addition_button.grid(row=0, column=1, padx=5, pady=10)

        # Subtraction button...
        self.subtraction_button = Button(self.buttons_frame, text="Subtraction",
                                         command=lambda: self.to_game(2),
                                         font=button_font, bg="MistyRose3")
        self.subtraction_button.grid(row=0, column=1, padx=5, pady=10)

        # Help Button (row 6)
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=6, pady=10)

    def to_game(self, buttons):
        starting_questions = self.questions_entry.get()


class Game:
    def __init__(self, partner, buttons, starting_questions):
        print(buttons)
        print(starting_questions)

        partner.subtraction_button.config(state=DISABLED)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    Start(root)
    root.mainloop()
