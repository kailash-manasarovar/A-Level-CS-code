def is_evil(num):
    temp = True
    while (num > 0):
        if (num % 2 == 1):
            temp = not temp
            num = num - 1
        num = num//2
    return temp

# dodgy recursion error
def is_odious(num):
    if num == 0:
        return False
    elif num % 2 == 0:
        return is_odious(num / 2)
    else:
        return not(is_odious(num / 2))


print(is_evil(0))
print(is_evil(2))
print(is_odious(0))
print(is_odious(2))
