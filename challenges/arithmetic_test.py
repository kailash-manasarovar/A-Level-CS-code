import random
import operator as op

def test():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, num1)

    ops = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
    }

    keys = list(ops.keys()) ##=> ['+', '*', '-']
    rand_key = random.choice(keys)  #e.g. '+'
    operation = ops[rand_key]  #e.g. op.add

    correct_result = operation(num1, num2)

    print ("What is {} {} {}?".format(num1, rand_key, num2))
    user_answer= int(input("Your answer: "))

    if user_answer != correct_result:
        print ("Incorrect. The right answer is {}".format(correct_result))
        return False
    else:
        print("Correct!")
        return True

username = input("What is your name? ")
print("Hi {}! Welcome to the Arithmetic quiz...".format(username))

correct_answers = 0
num_questions = 3

for i in range(num_questions):
    if test():
        correct_answers +=1


print("{}: You got {}/{} questions correct.".format(
    username,
    correct_answers,
    num_questions,
    #'question' if (correct_answers==1) else 'questions'
))
