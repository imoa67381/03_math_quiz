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
                                      font=button_font, bg="MistyRose2", width=10)
        self.addition_button.grid(row=8, column=1, padx=5, pady=10)

        # Subtraction button...
        self.subtraction_button = Button(self.buttons_frame, text="Subtraction",
                                         command=lambda: self.to_game(2),
                                         font=button_font, bg="PeachPuff", width=10)
        self.subtraction_button.grid(row=9, column=1, padx=5, pady=10)

        # Disable all stakes buttons at start
        self.addition_button = Button(state=DISABLED)
        self.subtraction_button = Button(state=DISABLED)

        # Help Button (row 10)
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=10, pady=10)

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
        self.heading_label = Label(self.game_frame, text="Play Now",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Questions Label, Entry box and Submit Button  (row 1)
        self.generate_questions_frame = Frame(self.game_frame)
        self.generate_questions_frame.grid(row=1, pady=10)

        self.questions_label = Label(self.generate_questions_frame, wrap=300, justify=LEFT,
                                     text="Please click next",
                                     font="Arial 10", padx=10, pady=10)
        self.questions_label.grid(row=0, column=0)

        self.answer_entry = Entry(self.generate_questions_frame,
                                  font="Arial 15 bold", width=3)
        self.answer_entry.grid(row=0, column=1, padx=2, pady=10)

        self.submit_button = Button(self.generate_questions_frame, text="Submit",
                                    font="Arial 15 bold",
                                    bg="gainsboro", fg="black")
        self.submit_button.grid(row=0, column=2, padx=2)

        # Next Button (row 2)
        self.next_button = Button(self.game_frame, text="Next",
                                  font="Arial 15 bold",
                                  bg="green", fg="white", width=25)
        self.next_button.grid(row=2)

        # Score Label (row 3)

        start_text = "Math Quiz Score:  \n "

        self.score_label = Label(self.game_frame, font="Arial 12 bold", fg="green",
                                 text=start_text, wrap=300,
                                 justify=LEFT)
        self.score_label.grid(row=3, pady=10)

        # Help and Game Stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=4, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Math Quiz Stats...",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Disable buttons at start
        self.submit_button.config(state=DISABLED)
        self.stats_button.config(state=DISABLED)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Dismiss", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=5, pady=10)

    def to_help(self):
        get_help = Help(self)

    def to_quit(self):
        root.destroy()


class Help:
    def __init__(self, partner):
        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "Enter the numbers you want the questions to be between. " \
                    "If the numbers you entered are too high, " \
                    "you will need to change it. Then enter the  " \
                    "amount of questions you want." \
                    "Then select either Addition or Subtraction for your " \
                    "math questions. Every correct answer you get right, your score will go up " \

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="arial 15 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    Start(root)
    root.mainloop()