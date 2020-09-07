import random

low = 1
high = 12

operator = "+"

num_1 = random.randint(low, high)
num_2 = random.randint(low, high)

question = "{} {} {}".format(num_1, operator, num_2)
answer = eval(question)

if operator == "*":
    operator = "×"

display_question = "{} {} {} = ".format(num_1, operator, num_2)

print(display_question)
print("Answer: ", answer)