# The Factorial of a positive integer, n, is defined as
# the product of the sequence n, n-1, n-2, ...1
# and the factorial of zero, 0, is defined as being 1.
# Solve this using both loops and recursion.

# for loop solution
# def factorial(n):
#    factorial = 1
#    for i in range(1, n+1):
#        factorial = factorial * i
#    return factorial

# while solution
def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result


# recursive solution
# def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)

n = int(input("Input a number to compute the factorial : "))
print(factorial(n))