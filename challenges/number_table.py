operator = input("Please input an operator, +,-,*,/ ")
number = int(input("Please input a number "))

list_of_numbers = [i for i in range(number+1)]

print(operator + " | " + str(list_of_numbers[:]))
print("- - - - - - - - - -")

for i in range(number+1):
    print(str(i) + " | " + str(list_of_numbers[i:]))
    pass