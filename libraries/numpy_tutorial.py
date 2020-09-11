# numpy = Numerical Python
# Mathematical and logical operations on arrays.
# Fourier transforms and routines for shape manipulation.
# Operations related to linear algebra.
# NumPy has in-built functions for linear algebra and random number generation.
# Replacing Matlab

import numpy as np

# a = np.array([1,2,3])
# b = np.array([[1, 2], [3, 4]])
# c = np.array([1, 2, 3, 4, 5], ndmin = 2)
# d = np.array([1, 2, 3], dtype = complex)
# print(a)
# print(b)
# print(c)
# print(d)


# a = np.array([[1,2,3],[4,5,6]]) # 2 rows, 3 cols
# print(a.shape)
# a.shape = (3,2)
# print(a)
# b = a.reshape(3,2)
# print(b)


# c = np.arange(24)
# print(c)
# b = c.reshape(2,4,3)
# print(b)


# x = np.array([1,2,3,4,5])
# print(x.flags)

x = np.empty([3,2], dtype = int)
print(x)


#https://www.tutorialspoint.com/numpy/numpy_array_from_existing_data.htm