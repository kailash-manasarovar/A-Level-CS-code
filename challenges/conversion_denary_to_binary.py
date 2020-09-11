# def dec_to_bin(decimal):
#     binary = bin(decimal)
#     print(str(binary))
# number = input("Input a number for conversion: ")
# dec_to_bin(int(number))

# def dec_to_bin(num):
#     if num > 1:
#         dec_to_bin(num // 2)
#     print(num % 2, end='')
# number = input("Input a number for conversion: ")
# dec_to_bin(int(number))


# den to bin
denary_number = int(input("Input a denary number for conversion: "))
binary_result = ""

if denary_number > 255:
    print("Number out of range.")

if denary_number >= 128:
    binary_result = binary_result + "1"
    denary_number = denary_number - 128
else:
    binary_result = binary_result + "0"

if denary_number >= 64 and denary_number < 128:
    binary_result = binary_result = binary_result + "1"
    denary_number = denary_number - 64
else:
    binary_result = binary_result + "0"

if denary_number >= 32 and denary_number < 64:
    binary_result = binary_result = binary_result + "1"
    denary_number = denary_number - 32
else:
    binary_result = binary_result + "0"

if denary_number >= 16 and denary_number < 32:
    binary_result = binary_result = binary_result + "1"
    denary_number = denary_number - 16
else:
    binary_result = binary_result + "0"

if denary_number >= 8 and denary_number < 16:
    binary_result = binary_result = binary_result + "1"
    denary_number = denary_number - 8
else:
    binary_result = binary_result + "0"

if denary_number >= 4 and denary_number < 8:
    binary_result = binary_result = binary_result + "1"
    denary_number = denary_number - 4
else:
    binary_result = binary_result + "0"

if denary_number >= 2 and denary_number < 4:
    binary_result = binary_result = binary_result + "1"
    denary_number = denary_number - 2
else:
    binary_result = binary_result + "0"

if denary_number >= 1 and denary_number < 2:
    binary_result = binary_result = binary_result + "1"
    denary_number = denary_number - 1
else:
    binary_result = binary_result + "0"

print(binary_result)



