from functools import reduce, partial

## MAP
l = map(str, [0, 1, 2, 3])
print(list(l))
def my_function(a,b):
    return a+b
l = map(my_function, [1, 2, 3, 4], [1, 2, 3, 4])
print(list(l))


# ## REDUCE
# def do_sum(x1, x2):
#     return x1 + x2
# print(reduce(do_sum, [1, 2, 3, 4]))
#
#
#
#
#
# ## FIlTER
# def filter_function(x):
#    if x > 18:
#        return True
# adults=filter(filter_function, [18, 21, 25, 16])
# for adult in adults:
#     print(adult)
#
#
#
# ## PARTIAL
# def multiply(x,y):
#         return x * y
# # create a new function that multiplies by 2
# double = partial(multiply,2)
# print(double(4))
#
#
#
#
# ## RECURSE
# # procedural code
# starting_number = 96
# # get the square of the number
# square = starting_number ** 2
# # increment the number by 1
# increment = square + 1
# # cube of the number
# cube = increment ** 3
# # decrease the cube by 1
# decrement = cube - 1
# # get the final result
# result = print(decrement) # output 783012621312
#
#
#
# ### FUNCTION COMPOSITION
# def composite_function(f, g):
#     return lambda x,y : f(g(x,y),y)
#
# # Function to add
# def add(x,y):
#     return x + y
#
# # Function to multiply
# def multiply(x,y):
#     return x * y
#
# add_multiply = composite_function(multiply, add)
# print(add_multiply(5,5))