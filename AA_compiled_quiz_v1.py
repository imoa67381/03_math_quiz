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

        # Multiplication button ...
        self.multiplication_button = Button(self.buttons_frame, text="Multiplication",
                                            command=lambda: self.to_game(3),
                                            font=button_font, bg="MistyRose2", width=10)
        self.multiplication_button.grid(row=10, column=1, padx=5, pady=10)

        # Division button ...
        self.division_button = Button(self.buttons_frame, text="Division",
                                      command=lambda: self.to_game(4),
                                      font=button_font, bg="light cyan", width=10)
        self.division_button.grid(row=11, column=1, padx=5, pady=10)

        # Help Button (row 12)
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=12, pady=10)

    def to_game(self, buttons):

        # get data from entry boxes
        question_amount = self.amount_questions_entry

        # ok = self.check_num()
        ok = "ok"

        if ok == "ok":
            # number of questions
            starting_questions = self.amount_questions_entry.get()
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
                elif starting_questions <= 0:
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
                Quiz(self, buttons, starting_questions)


class Quiz:
    def __init__(self, partner, type_question, number_questions, var_low_num, var_high_num):
        print(type_question)
        print(number_questions)

        # initialise variables
        self.low_num = IntVar()
        self.low_num.set(var_low_num)

        self.high_num = IntVar()
        self.high_num.set(var_high_num)

        self.number_questions = IntVar()
        self.number_questions.set(0)

        self.correct_answer = IntVar()
        self.correct_answer.set(0)

        # self.user_entry = IntVar()
        # self.user_entry.set(0)

        self.operations = StringVar()
        self.operations.set(type_question)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # So user can quit with x in top corner
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

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
                                     font="Arial 10 bold", padx=10, pady=10)
        self.questions_label.grid(row=0, column=0)

        self.answer_entry = Entry(self.generate_questions_frame,
                                  font="Arial 15 bold", width=3)
        self.answer_entry.grid(row=0, column=1, padx=2, pady=10)

        self.submit_button = Button(self.generate_questions_frame, text="Submit",
                                    font="Arial 15 bold",
                                    bg="gainsboro", fg="black")
        self.submit_button.grid(row=0, column=2, padx=2)

        # Number of question

        self.number_questions_label = Label(self.game_frame,
                                            text="Question 1",
                                            font="Arial 12 bold",
                                            padx=10, pady=10)
        self.number_questions_label.grid(row=2)

        # Next Button goes here(row 2)
        self.next_button = Button(self.game_frame, text="Next",
                                  font="Arial 15 bold",
                                  bg="green", fg="white", width=25, command=self.generate_questions)
        self.next_button.grid(row=3)

        # space where the errors are displayed
        self.amount_error_label = Label(self.game_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=4, columnspan=2, pady=5)

        # Score Label (row 3)

        start_text = "Math Quiz Score:  \n "

        self.score_label = Label(self.game_frame, font="Arial 12 bold", fg="green",
                                 text=start_text, wrap=300,
                                 justify=LEFT)
        self.score_label.grid(row=5, pady=10)

        # Help and Game Stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=6, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  command=self.to_help,
                                  bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Math Quiz Stats...",
                                   font="Arial 15 bold",
                                   command=self.to_stats,
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Disable buttons at start
        self.submit_button.config(state=DISABLED)
        self.stats_button.config(state=DISABLED)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Dismiss", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=7, pady=10)

        # disabling the submit button
        self.submit_button.config(state=DISABLED)

    def generate_questions(self):
        # retrieve the users input
        low_num = self.low_num.get()
        high_num = self.high_num.get()

        print("low", low_num)
        print("high", high_num)

        # Generate questions
        operator = self.operations.get()

        num_1 = random.randint(low_num, high_num)
        num_2 = random.randint(low_num, high_num)

        if operator == "*":
            display_operator = "×"

        elif operator == "/":
            display_operator = "÷"

            if num_1 == 0 and num_2 == 0:
                num_1 = 1
                num_2 = 1

            mult_ans = num_1 * num_2
            num_1 = mult_ans

        else:
            display_operator = operator

        question = ("{} {} {}".format(num_1, operator, num_2))

        # Edit label so user can see their balance
        display_question = "{} {} {} = ".format(num_1, display_operator, num_2)
        self.questions_label.configure(text=display_question)
        self.next_button.config(state=DISABLED)

        # enable stats and submit button
        self.submit_button.config(state=NORMAL)

        answer = eval(question)
        self.correct_answer.set(answer)

        print("{} {}".format(display_question, answer))

    def check_answer(self):
        # disabling the next question button
        self.next_button.config(state=DISABLED)

        wrong_answer = "#ffafaf"
        right_answer = "#00FF44"

        self.amount_error_label.config(text="")
        self.answer_entry.config(bg="white")

        # retrieve users answer
        correct_answer = self.correct_answer.get()
        user_answer = self.answer_entry.get()

        try:
            user_answer = int(user_answer)

            if user_answer != correct_answer:
                answer_correct = "no"
                check_answer = "Sorry this is incorrect " \
                               "click next to continue"
                self.next_button.config(state=NORMAL)
                self.submit_button.config(state=DISABLED)

            elif user_answer == "":
                answer_correct = "no"
                check_answer = "You're answer is can't " \
                               "be blank, try again and click submit "
            else:
                answer_correct = "yes"
                check_answer = "Well done you're answer " \
                               "is correct! Click next to " \
                               "continue"
                self.next_button.config(state=NORMAL)
                self.submit_button.config(state=DISABLED)

                self.answer_entry.config(bg=right_answer)

        except ValueError:
            answer_check = "Please enter a whole number (no text / decimals)"

            self.answer_entry.config(bg=wrong_answer)
        self.amount_error_label.config(text=check_answer)

    def to_help(self):
        print("hello")

    def to_stats(self):
        print("whee")

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