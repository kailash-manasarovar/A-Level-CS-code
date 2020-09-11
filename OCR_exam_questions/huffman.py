
def huffman(argument):
    switch = {
        '0': "A",
        '11': "B",
        '100': "C",
        '101': "D"
    }
    return switch.get(argument, "nothing")



message = input("Enter the message")

result = huffman(message)

print(result)


# if else is better

