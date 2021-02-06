def fib():
    a, b = 0, 1
    count = 0

    #while len(str(a)) < 11:
    while count < 10:

        a, b = b, a + b
        count = count + 1
        print(count, a)

    return count, a


print(fib())


# Python program to display the Fibonacci sequence
#
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
#
# nterms = 10
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))