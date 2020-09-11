# 2017 Paper 2 June Q3
# # stack is LIFO ?
#
# the_string = "SILVER"
# length_of_the_string = len(the_string)
# print(length_of_the_string)
#
#
# # my Stack class definition
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[len(self.items) - 1]
#
#     def size(self):
#         return len(self.items)
#
#     def __str__(self):
#         result = ""
#         for i in self.items:
#             result = result + " " + str(i) + "\n"
#         return result
#
#
#
# # first create a stack
# stack = Stack()
# print(stack.isEmpty())
#
# for i in the_string:
#     stack.push(i)
# stack.push(length_of_the_string)
#
#
# # create a string that represents the stack
# string_of_stack = stack.__str__()
# # reverse it so it looks the same as the answer - this is not necessary as the stack is correct already
# print(string_of_stack[::-1])



def passtostack(passString):
    string_len = len(passString)
    # print(string_len)
    # create a list of the correct size and fill it so there's no null pointers
    stack = [None] * (string_len+1)
    # print(stack)

    # set the pointers for the stack and the list
    stackptr = 0
    stringptr = string_len - 1

    # in reverse order of the string
    for i in range(string_len-1, -1, -1):
        print(stack[i])
        print(passString[i])
        stack[stackptr] = passString[stringptr]
        stackptr = stackptr + 1
        stringptr = stringptr - 1

    stack[stackptr] = string_len
    print(stack)



passtostack("hello")

