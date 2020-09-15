class Quiz:
    def __init__(self, partner, question_type, question_amount, numbers_used_low,
                 numbers_used_high):
        print(question_type)
        print(question_amount)
        print(numbers_used_low)
        print(numbers_used_high)

        # importing numbers inputed by the user for generating questions
        self.var_low = IntVar()
        self.var_low.set(numbers_used_low)

        self.var_high = IntVar()
        self.var_high.set(numbers_used_high)

        # Importing the correct answer
        self.var_correct_ans = IntVar()
        self.var_correct_ans.set(0)

        # Importing the correct answer
        self.var_ques_number = IntVar()
        self.var_ques_number.set(0)

        self.var_operation = StringVar()
        self.var_operation.set(question_type)

        # GUI Setup
        self.quiz_box = Toplevel()

        # So user can quit with x in top corner
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        # Frame for main quiz functions
        self.quiz_frame = Frame(self.quiz_box, pady=10, padx=10)
        self.quiz_frame.grid()

        # Frame for help button
        self.help_frame = Frame(self.quiz_box, pady=10, padx=10)
        self.help_frame.grid()

        # Frame for the quit button
        self.quit_frame = Frame(self.quiz_box, pady=10, padx=10)
        self.quit_frame.grid()

        # Top heading
        self.math_quiz_label = Label(self.quiz_frame,
                                          text="Play",
                                          font=("Arial", "19", "bold"),
                                          padx=10, pady=10)
        self.math_quiz_label.grid(row=0)

        # Instructions for user
        self.math_instructions = Label(self.quiz_frame, font="Arial 10 italic",
                                       text="Click on the Next button "
                                            "to continue. Then click on "
                                            "the submit button to check you're "
                                            "answer.  ",
                                            wrap=275, justify=LEFT,
                                            padx=10, pady=10,)
        self.math_instructions.grid(row=1)

        # question number

        self.question_number_label = Label(self.quiz_frame,
                                          text="Question 1",
                                          font=("Arial", "12", "bold"),
                                          padx=10, pady=10)
        self.question_number_label.grid(row=2)

        # used to display the questions
        self.questions_label = Label(self.quiz_frame,
                                       font="Arial 15 bold",
                                       text="question")
        self.questions_label.grid(row=4, column=0)

        # entry box for answers
        self.question_answer_entry = Entry(self.quiz_frame,
                                        font="Arial 19 bold", width=5)
        self.question_answer_entry.grid(row=4, column=1, padx=15)

        # space where the errors are displayed
        self.amount_error_label = Label(self.quiz_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=3, columnspan=2, pady=5)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Submit answer button
        self.submit_button = Button(self.quiz_frame, text="Submit",
                                            command=lambda: self.check_answer(),
                                            font=button_font, bg="#4ee6ab")
        self.submit_button.grid(row=5, column=1, pady=10)

        # next question button
        self.next_button = Button(self.quiz_frame, text="Next",
                                            command=lambda: self.next_question(question_amount),
                                            font=button_font, bg="#4ee6ab")
        self.next_button.grid(row=5, column=0, pady=10)

        # help button
        self.help_button = Button(self.help_frame, text="How to Play",
                                       bg="#808080", fg="white",
                                       font="Arial 15 bold",
                                       command=self.to_help)
        self.help_button.grid(row=1, column=0, pady=5)

        # help button
        self.stats_btn = Button(self.help_frame, text="Stats",
                                       bg="#0033FF", fg="white",
                                       font="Arial 15 bold",
                                       command=self.to_stats)
        self.stats_btn.grid(row=1, column=1, pady=5)

        # Quit button
        self.quit_button = Button(self.quit_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold",
                                  command=self.to_quit, padx=10, pady=5)
        self.quit_button.grid(row=7, pady=10, column=1)

        # ensuring the user cannot click submit with no question
        self.submit_button.config(state=DISABLED)


def check_answer(self):
    # disabling the next question button until user has correct answer.
    self.next_button.config(state=DISABLED)

    answer_wrong = "#ffafaf"
    answer_right = "#00FF44"

    self.amount_error_label.config(text="")
    self.question_answer_entry.config(bg="white")

    actual_answer = self.var_correct_ans.get()
    user_answer = self.question_answer_entry.get()

    try:

        user_answer = int(user_answer)

        if user_answer != actual_answer:
            answer_correct = "no"
            answer_check = "Sorry that is the incorrect " \
                           "answer! Click next to continue"
            self.next_button.config(state=NORMAL)
            self.submit_button.config(state=DISABLED)

        elif user_answer == "":
            answer_correct = "no"
            answer_check = "You're answer cannot be " \
                           "blank! try again and click submit"
        else:
            answer_correct = "yes"
            answer_check = "Well Done that is the " \
                           "correct answer! Click next to " \
                           "continue"
            self.next_button.config(state=NORMAL)
            self.submit_button.config(state=DISABLED)

            self.question_answer_entry.config(bg=answer_right)

    except ValueError:
        answer_check = "Please enter a whole number (no text / decimals)"

        self.question_answer_entry.config(bg=answer_wrong)
    self.amount_error_label.config(text=answer_check)


# setting up for the help button
def to_help(self):
    get_help = Help(self)


# so the quit button functions correctly
def to_quit(self):
    root.destroy()


# Going to the stats function
def to_stats(self):
    QuizStats()