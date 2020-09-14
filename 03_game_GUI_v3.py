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
        operations = 4
        low_num = 1
        high_num = 12

        Game(self, operations, starting_questions, low_num, high_num)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, operations, starting_questions, low_num, high_num, check_answers):
        print(operations)
        print(starting_questions)

        # initialise variables
        self.number_questions = IntVar()
        self.number_questions.set(starting_questions)

        self.user_entry = IntVar()
        self.user_entry.set(check_answers)

        self.correct_answer = IntVar
        self.correct_answer.set(check_answers)

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

        # Next Button goes here(row 2)
        self.next_button = Button(self.game_frame, text="Next",
                                  font="Arial 15 bold",
                                  bg="green", fg="white", width=25, command=self.generate_questions)
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

    def generate_questions(self):
        # retrieve the users input
        low_num = self.number_questions.get()
        high_num = self.number_questions.get()

        # Generate questions
        ops = ['+', '-', '*', '/']
        operator = random.choice(ops)
        num_1 = random.randint(low_num, high_num)
        num_2 = random.randint(low_num, high_num)

        question = ("{} {} {}".format(num_1, operator, num_2))
        answer = eval(question)

        display_question = "{} {} {} = ".format(num_1, operator, num_2)

        # Edit label so user can see their balance
        self.questions_label.configure(text=display_question)
        self.next_button.config(state=DISABLED)

        # enable stats and submit button
        self.submit_button.config(state=NORMAL)

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
        self.amount_error_label.config(text="")

        # retrieve users answer
        correct_answers = self.correct_answer.get()
        user_answer = self.user_entry.get()

        try:
             user_answer = int(user_answer)

             if user_answer != correct_answers:
                 correct_answer = "no"
                 correct_answer = "Sorry this is incorrect " \
                                    "click next to continue"
                 self.next_button.config(state=NORMAL)
                 self.submit_button.config(state=NORMAL)


    def to_quit(self):
     print("hello world")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    Start(root)
    root.mainloop()