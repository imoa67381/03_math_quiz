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
