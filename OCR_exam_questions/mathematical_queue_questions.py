questions = ["2*3", "1+4", "3-1", "10/2", "3+6"]
print(questions)
#
# a queue is FIFO ?
#
questions.append("6+1")
print(questions)
# #
head = questions[0]
print(head)
# #
tail = questions[len(questions)-1]
print(tail)
#
# remove the first element in the queue
# remember, the first element is the head
#
def remove():
     first_element = questions.pop(0)
     print(first_element)
remove()
print(questions)
#
#
# procedure add elements
def add():
    max_elements = 10
    new_question = input("Please input a new question")
    question_size = len(questions)
    print(question_size)
    if question_size > 10:
        print("Sorry, the queue is full, you cannot add any new questions")
    else:
        questions.append(new_question)
        print(questions)

add()