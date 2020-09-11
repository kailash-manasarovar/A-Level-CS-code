from numpy import array

# list
# l = [1.0, 2.0, 3.0]
# print(type(l))
# #
# print(l)
# a = array(l)
# print(a)
# print(a.shape)
# print(a.dtype)

#
from numpy import empty
a = empty([3,3])
print(a)
print(a.shape)
print(a.dtype)
#
#
# create zero array
from numpy import zeros
a = zeros([3,5])
print(a)
# #
# #
filled_array = [[0, 1, 2, 3],
               [4, 5, 6, 7],
                [8, 9, 10, 11]]
# #
fa = array(filled_array)
print(fa)
print(fa[1][1])