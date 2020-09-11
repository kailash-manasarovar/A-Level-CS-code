gate = input("Enter logic gate: AND, OR, XOR, NAND, or NOR ")
first = int(input("Enter first input: "))
second = int(input("Enter second input: "))

def AND(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def OR(a,b):
    if a == 0 and b == 0:
        return 0
    else:
        return 1


if gate == 'AND':
    print(AND(first, second))

if gate == 'OR':
    print(OR(first, second))
