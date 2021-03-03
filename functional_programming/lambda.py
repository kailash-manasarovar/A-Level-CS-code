## writing lambda functions in Python

# ## simple addition and multiplication
# function = lambda a : a + 15
# print(function(10))
# function = lambda x, y : x * y
# print(function(12, 4))
#
#
# ## sort a list of tuples
# # https://docs.python.org/3/howto/sorting.html - lots of sorting options
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print("Original list of tuples:")
# print(subject_marks)
# subject_marks.sort(key = lambda x: x[1])
# print("\nSorting the List of Tuples:")
# print(subject_marks)


# ## fibonacci
# from functools import reduce
# fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
#                               range(n - 2), [0, 1])
# print("Fibonacci series upto 2:")
# print(fib_series(2))
# print("\nFibonacci series upto 3:")
# print(fib_series(3))
# print("\nFibonacci series upto 4:")
# print(fib_series(4))
# print("\nFibonacci series upto 9:")
# print(fib_series(9))


## palindromes
texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
print("Orginal list of strings:")
print(texts)
result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
print("\nList of palindromes:")
print(result)