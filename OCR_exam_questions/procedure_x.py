# 2017 Paper 2 June Q2
import numpy as np

def x(theOrders):
    finished = False
    print(finished)
    count = 0
    print(count)
    while not finished:
        if theOrders[1,count] is None:
            finished = True
        else:
            output = theOrders[0,count]
            print(output)
            #print(finished)
            count = theOrders[1,count]
            #print(count)

    output = theOrders[0,count]
    #print(output)


theOrders = np.array([
[184,186,155,187],
    [1,2,3,None]
])

# theOrders[row, col]
# print(theOrders[0,0])

# x(theOrders)


