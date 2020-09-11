def fib():
    a, b = 0, 1
    count = 0

    while len(str(a)) < 11:

        a, b = b, a + b
        count = count + 1
        print(a, count)

    return a, count


print(fib())