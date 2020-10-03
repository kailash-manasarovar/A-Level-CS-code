# LINEAR SEARCH (SERIAL SEARCH):
# 2 inputs = list of elements, search value
# output = is it there? is the search value in the list of elements? yes or no, boolean (true or false)
# Big O (worst case scenario runtime)
# if the number of elements in the list = n, Big O of Linear Search = n


#import time

def linear_search(myList, myItem):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position + 1
    return found


#
# list_of_elements = [4, 2, 8, 9, 3, 7]
# number_to_search_for = int(input("Enter number to search: "))
#
# starttime = time.time()
# is_found = linear_search(list_of_elements, number_to_search_for)
# endtime = time.time()
#
# time_it_took = endtime - starttime
# rounded_time = round(time_it_took,5)
#
# if is_found:
#     print("Your item is in the list.")
# else:
#     print("Your item is not in the list.")
#
# print("It took in seconds: {:0.5f} ".format(rounded_time))



# found = False
#
# for i in range(len(list_of_elements)):
#  if(list_of_elements[i] == number_to_search_for):
#   found = True
#   print("%d found at %dth position"%(number_to_search_for,i))
#   break
#
# if(found == False):
#  print("%d is not in list"%number_to_search_for)



#OCR GCSE PSUEDOCODE
#pointer = 0
#my_list = [1, 2, 3, 4, 5, 6]
#search_item = int(input("Enter number to search for: "))

#while pointer < len(my_list) and my_list[pointer] != search_item:
#    pointer = pointer + 1

#if pointer >= len(my_list):
#    print("Value not in the list")
#else:
#    print("The value is in the list at location " + str(pointer))



#DO-WHILE
# Python doesn't give you do-while but...
# pointer = 0
# my_list = [1, 2, 3, 4, 5, 6]
# search_item = int(input("Enter number to search for: "))
# while True:
#     if pointer < len(my_list) and my_list[pointer] != search_item:
#         pointer = pointer + 1
#     else:
#         break
#
# if pointer >= len(my_list):
#     print("Value not in the list")
# else:
#     print("The value is in the list at location " + str(pointer))