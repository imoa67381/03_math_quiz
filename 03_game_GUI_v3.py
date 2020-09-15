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
        number_questions = 50
        operations = 4
        low_num = 1
        high_num = 12

        Game(self, operations, number_questions, low_num, high_num)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, type_question, number_questions, low_num, high_num, check_answers):
        print(type_question)
        print(number_questions)
        print(low_num)
        print(high_num)
        print(check_answers)

        # initialise variables
        self.low_num = IntVar()
        self.low_num.set(low_num)

        self.high_num = IntVar()
        self.high_num.set(high_num)

        self.number_questions = IntVar()
        self.number_questions.set(0)

        self.correct_answer = IntVar
        self.correct_answer.set(0)

        self.user_entry = IntVar()
        self.user_entry.set(0)

        self.operations =StringVar()
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
                                     font="Arial 10", padx=10, pady=10)
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
        self.quit_button.grid(row=7, pady=10)

        # disabling the submit button
        self.submit_button.config(state=DISABLED)

    def generate_questions(self):
        # retrieve the users input
        low_num = self.number_questions.get()
        high_num = self.number_questions.get()

        # Generate questions
        ops = ['+', '-', '*', '/']
        operator = random.choice(ops)
        num_1 = random.randint(low_num, high_num)
        num_2 = random.randint(low_num, high_num)

        if operator == "*":
            operator = "×"

        question = ("{} {} {}".format(num_1, operator, num_2))
        answer = eval(question)

        display_question = "{} {} {} = ".format(num_1, operator, num_2)

        # Edit label so user can see their balance
        self.questions_label.configure(text=display_question)
        self.next_button.config(state=DISABLED)

        # enable stats and submit button
        self.submit_button.config(state=NORMAL)

        self.correct_answer.set(answer)

        print("{} {}".format(display_question, answer))

        score = 0
        correct_answers = 0
        number_questions = 0

        try:

            user_entry = int(input())
            if ops == "+":
                answer = (low_num + high_num)
            elif ops == "-":
                answer = (low_num - high_num)
            elif ops == "*":
                answer = (low_num * high_num)
            elif ops == "/":
                answer = (low_num / high_num)
            if user_entry == answer:
                print("Well done")
                score = score + 1

            else:
                print("WRONG!")
                print("The answer was", answer)

                number_questions = number_questions + 1

    def check_results(self):
        # disabling the next question button
        self.next_button.config(state=DISABLED)

        wrong_answer = "#ffafaf"
        right_answer = "#00FF44"

        self.amount_error_label.config(text="")
        self.user_entry.config(bg="white")

        # retrieve users answer
        correct_answers = self.correct_answer.get()
        user_answer = self.user_entry.get()

        try:
             user_answer = int(user_answer)

             if user_answer != correct_answers:
                 correct_answer = "no"
                 answer_check = "Sorry this is incorrect " \
                                    "click next to continue"
                 self.next_button.config(state=NORMAL)
                 self.submit_button.config(state=DISABLED)

             elif user_answer =="":
                 correct_answer = "no"
                 answer_check = "You're answer is can't " \
                                "be blank, try again and click submit " \

             else:
                  correct_answer = "yes"
                  answer_check = "Well done you're answer " \
                                "is correct! Click next to " \
                                 "continue"
                  self.next_button.config(state=NORMAL)
                  self.submit_button.config(state=DISABLED)

                  self.user_entry.config(bg=correct_answer)

        except ValueError:
            answer_check = "Please enter a whole number (no text / decimals)"

            self.user_entry.config(bg=wrong_answer)
            self.amount_error_label.config(text=right_answer)

        # setting up for the help button
        def to_help(self):
            get_help = Help(self)

        # so the quit button functions correctly
        def to_quit(self):
            root.destroy()

        # Going to the stats function
        def to_stats(self):
            QuizStats()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    Start(root)
    root.mainloop()