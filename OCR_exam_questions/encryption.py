s = ""

# read string from file
def read_message():
    global s
    file = open("string.txt", "r")
    s = file.read()
    file.close()
    return s

# reverse the string
def reverse_string(str):
    reversed_str = str[::-1]
    return reversed_str


# push each character of the string onto a stack
class Stack(list):
    push = list.append


def push_onto_stack(str):
    stack = Stack()
    #result = []
    for character in str:
        stack.push(character)
    return stack


# read and encrypt each character
def encrypt_into_ascii(str_stack):
    ascii_list = [ord(c) for c in str]
    print(ascii_list)
    # subtract 10 from ascii number at each element
    ascii_list[:] = [x - 10 for x in ascii_list]
    return ascii_list


# save the string into the same file
def save_into_file(ascii_encryption):
    file = open("string.txt", "a")
    file.write("\n")
    for item in ascii_encryption:
        file.write("%s " % item)
    file.close()



str = read_message()
print(str)
reversed_str = reverse_string(str)
print(reversed_str)
string_stack = push_onto_stack(reversed_str)
print(string_stack)
ascii_encryption = encrypt_into_ascii(string_stack)
print(ascii_encryption)
save_into_file(ascii_encryption)
#print(type(ascii_encryption))
