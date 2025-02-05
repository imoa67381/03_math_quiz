from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get questions for quiz
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.submit_button = Button(text="Submit", command=self.to_quiz)
        self.submit_button.grid(row=0, pady=10)

    def to_quiz(self):
        # retrieve starting questions
        amount_questions = 3
        operations = 4

        if operations == 4:
            operator = "/"

        low_num = 1
        high_num = 12

        Quiz(self, operator, amount_questions, low_num, high_num)

        # hide start up window
        root.withdraw()


class Quiz:
    def __init__(self, partner, type_question, amount_questions, var_low_num, var_high_num):
        print(type_question)
        print(amount_questions)

        # low number the user enters at the start
        self.low_num = IntVar()
        self.low_num.set(var_low_num)

        # high number the user enters at the start
        self.high_num = IntVar()
        self.high_num.set(var_high_num)

        # number of questions that user asks for
        self.number_questions = IntVar()
        self.number_questions.set(amount_questions)

        # number of questions answered
        self.num_answered = IntVar()
        self.num_answered.set(0)

        # number of correct answers by user
        self.correct_answer = IntVar()
        self.correct_answer.set(0)

        # Importing the correct answer
        self.question_number = IntVar()
        self.question_number.set(1)

        # setting the score as an integer
        self.score = IntVar()

        # operator the user chooses at the start of the game
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

        # Number of question
        self.question_number_label = Label(self.game_frame,
                                            text="Question 1",
                                            font="Arial 12 bold",
                                            padx=10, pady=10)
        self.question_number_label.grid(row=1)

        # Questions Label, Entry box and Submit Button  (row 2)
        self.generate_questions_frame = Frame(self.game_frame)
        self.generate_questions_frame.grid(row=2, pady=10)

        self.questions_label = Label(self.generate_questions_frame, wrap=300, justify=LEFT,
                                     text="Please click next",
                                     font="Arial 10 bold", padx=10, pady=10)
        self.questions_label.grid(row=0, column=0)

        self.answer_entry = Entry(self.generate_questions_frame,
                                  font="Arial 15 bold", width=3)
        self.answer_entry.grid(row=0, column=1, padx=2, pady=10)

        self.submit_button = Button(self.generate_questions_frame, text="Submit",
                                    font="Arial 15 bold",
                                    command=self.check_answer,
                                    bg="gainsboro", fg="black")
        self.submit_button.grid(row=0, column=2, padx=2)

        # Next Button goes here(row 3)
        self.next_button = Button(self.game_frame, text="Next",
                                  font="Arial 15 bold",
                                  bg="green", fg="white", width=25, command=self.generate_questions)
        self.next_button.grid(row=3)

        # space where the errors are displayed
        self.amount_error_label = Label(self.game_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=4, columnspan=2, pady=5)

        # Score Label (row 5)
        start_text = "Math Quiz Score:  \n "

        self.score_label = Label(self.game_frame, font="Arial 12 bold", fg="green",
                                 text=start_text, wrap=300,
                                 justify=LEFT)
        self.score_label.grid(row=5, pady=10)

        # Help and Game Stats button (row 6)
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
        # color for when box is cleared (white)
        box_clear = "#ffffff"

        self.answer_entry.config(bg=box_clear)
        self.answer_entry.delete(0, 'end')

        new_question_number = self.question_number.get()

        question_number_text = "Question {}".format(new_question_number)
        self.question_number_label.config(text=question_number_text)

        # retrieve the users input
        low_num = self.low_num.get()
        high_num = self.high_num.get()
        number_questions = self.number_questions.get()
        #num_answered = num_answered.get()

        print("low", low_num)
        print("high", high_num)
        print("number_questions", number_questions)
        #print("num_answered", num_answered)

        new_question_number += 1
        self.question_number.set(new_question_number)

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
        answer = int(answer)
        self.correct_answer.set(answer)

        print("{} {}".format(display_question, answer))

    def check_answer(self):
        # disabling the next question button
        self.next_button.config(state=DISABLED)
        # enabling the stats button when the user has entered an answer
        self.stats_button.config(state=NORMAL)

        # collecting the different variables required for checking the answers
        score = self.score.get()
        questions = self.number_questions.get()
        new_question_number = self.question_number.get()
        question_num = self.question_number.get()

        wrong_answer = "#ffafaf"
        right_answer = "#00FF44"

        self.amount_error_label.config(text="")
        self.answer_entry.config(bg="white")

        # retrieve users answer
        answer_correct = self.correct_answer.get()
        user_answer = self.answer_entry.get()

        try:
            user_answer = int(user_answer)

            if user_answer != answer_correct:
                answer_correct = "no"
                check_answer = "Sorry this is incorrect " \
                               "click next to continue"
                self.next_button.config(state=NORMAL)
                self.submit_button.config(state=DISABLED)

                self.answer_entry.config(bg=wrong_answer)

            elif user_answer == "":
                answer_correct = "no"
                check_answer = "You're answer can't " \
                               "be blank, try again and click submit "
                self.amount_error_label.config(text=check_answer)
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

    def to_help(self):
        print("help")

    def to_stats(self):
        print("stats")

    def to_quit(self):
        root.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    Start(root)
    root.mainloop()