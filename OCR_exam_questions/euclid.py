# 2017 Paper 2 Q5
def calculate(num1, num2):
    if num1 == num2:
        return num1
    elif num1 < num2:
        return calculate(num1, num2-num1)
    else:
        return calculate(num2, num1-num2)


print(calculate(4,10))

# returns the highest multiple of both numbers


def euclid(num1, num2):
    while num1 != num2:
        if num1 < num2:
            num2 = num2 - num1
        else:
            temp = num1 - num2
            num1 = num2
            num2 = temp
    return num1


print(euclid(4,10))