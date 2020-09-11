import random
import time


def bubblesort(list_of_elements):
    moreSwaps = True
    while moreSwaps:
        moreSwaps = False
        for element in range(len(list_of_elements) - 1):
            if (list_of_elements[element] > list_of_elements[element + 1]):
                moreSwaps = True
                temp = list_of_elements[element]
                list_of_elements[element] = list_of_elements[element + 1]
                list_of_elements[element + 1] = temp
    return list_of_elements


#my_list = [5, 2, 5, 1, 4, 3, 7, 4]
#print(bubblesort(myList))


size_of_list = int(input("Please enter the size of the random list. "))

my_list = random.sample(range(0,100000),size_of_list)
print(my_list)

print('Let\'s sort the list! And see how long it takes!')

# take a start time
start_time = time.time()
# run the algorithm
print(bubblesort(my_list))
# take a finish time
finish_time = time.time() - start_time
rounded_time = (round(finish_time,5))

#print("It took: --- %s seconds ---" % (round(finish_time,5)))

print("It took in seconds: {:0.5f} ".format(rounded_time))
