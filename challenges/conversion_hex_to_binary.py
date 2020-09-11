hex_number = input("Please enter 2 digit hex number")
denary_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
denary_result = 0
bin_result = ""


def convert(hex_digit):
    if hex_digit in denary_numbers:
        return int(hex_digit)
    elif hex_digit == "A":
        return 10
    elif hex_digit == "B":
        return 11
    elif hex_digit == "C":
        return 12
    elif hex_digit == "D":
        return 13
    elif hex_digit == "E":
        return 14
    elif hex_digit == "F":
        return 15


def hex_to_bin(denary_result):
    binary_result = ""

    if denary_result > 15:
        print("out of range")

    if denary_result >= 8 and denary_result < 16:
        binary_result += "1"
        denary_result = denary_result - 8
    else:
        binary_result += "0"

    if denary_result >= 4 and denary_result < 8:
        binary_result += "1"
        denary_result = denary_result - 4
    else:
        binary_result += "0"

    if denary_result >= 2 and denary_result < 4:
        binary_result += "1"
        denary_result = denary_result - 2
    else:
        binary_result += "0"

    if denary_result >= 1 and denary_result < 2:
        binary_result += "1"
        denary_result = denary_result - 1
    else:
        binary_result += "0"

    return binary_result


for i in hex_number:
    denary_result = convert(i)
    bin_result += hex_to_bin(denary_result)

print(bin_result)


