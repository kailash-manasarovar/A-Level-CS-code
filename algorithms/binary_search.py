# BINARY SEARCH
# input - list, value to search for
# algorithm
# output - boolean
# PREREQUISITE: list has to be in order!!

# Big O (worst case scenario runtime) of Binary Search = log n

# list has n items
# _ _ _ _ _ _
# _ _ _
# _
# _ _ _ _ _ _
#       _ _ _
#       _

#import time

def binary_search(list_of_elements, item):

    # debug, print out trace table
    #print("TRACE TABLE")
    #print(list_of_elements[:])

    first = 0
    last = len(list_of_elements) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        #print(mid)
        if list_of_elements[mid] == item:
            found = True
        else:
            if item < list_of_elements[mid]:
                last = mid - 1
            else:
                first = mid + 1

        # debug, print out trace table
        # print(list_of_elements[first:last])

    return found


## A Level mock question test
my_list = ["Adam", "Alex", "Anna", "Hon", "Mohammed", "Moonis", "Niraj", "Philip", "Punit", "Ravi", "Richard", "Timothy", "Tushara", "Uzair", "Zara"]
#print(binary_search(my_list, "Richard"))



# def recursive_binary_search(list_of_elements, item):
#
#     if len(list_of_elements) == 0:
#         return False
#     else:
#         mid = len(list_of_elements) // 2
#
#     if list_of_elements[mid] == item:
#         return True
#     else:
#         if item < list_of_elements[mid]:
#             return recursive_binary_search(list_of_elements[:mid], item)
#         else:
#             return recursive_binary_search(list_of_elements[mid + 1:], item)


# import random as r
# randomlist = []
# for i in range(0,100000000):
#     n = r.randint(1,10000000)
#     randomlist.append(n)
# #print(randomlist)
#
# start = time.time()
# is_found = binary_search(randomlist, 300)
# end = time.time()
# time_took = end - start
# rounded_time = round(time_took,5)
#
#
# if is_found:
#     print("Your item is in the list.")
# else:
#     print("Your item is not in the list.")
#
# print("It took in seconds: {:0.5f} ".format(rounded_time))


# print(binary_search([1,2,3,5,8], 5))
# print(binary_search(['a','c','d','e','f'],'c'))