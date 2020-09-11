import numpy as np
import statistics

# array data[16,11]

data = [[1, 5, 7, 12, 0, 0, 0, 0, 0, 0, 36],
        [3, 4, 15, 16, 0, 0, 0, 0, 0, 0, 48],
        [0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 10],
        [12, 16, 18, 23, 0, 0, 0, 0, 0, 0, 100],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 10, 15, 25, 0, 0, 0, 0, 0, 0, 96]]


print(data[15][10])


# example median
#the_array = [1, 5, 7, 12, 15]
#print(the_array[2])
#print(statistics.median(the_array))


# find the median of each row
#for i in range(0, 15):
#    print(data[i][5])


# find the mean of each row
result = 0
for i in range(0, 15):
    for j in range(0, 10):
        result = result + j
        #print(result)
    mean = result / 11
    print(mean)