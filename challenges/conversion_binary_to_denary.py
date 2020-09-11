binary_range = [128, 64, 32, 16, 8, 4, 2, 1]
binary_number = input("Please enter 8 bit binary number")
denary_result = 0

for i in range(0, 8):
    if binary_number[i] == "1":
        denary_result += binary_range[i]

print(denary_result)
