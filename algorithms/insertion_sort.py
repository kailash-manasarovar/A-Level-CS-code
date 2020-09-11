import time
import random

def insertion_sort(nlist):

    # for loop over the whole list from the second element to the end
   for index in range(1,len(nlist)):

    # set value and index for each iteration dependent on index
     currentvalue = nlist[index]
     position = index

    # check to see if the value left of the current value is greater than the current value and if so, swap it
    # end while when position is 0 and everything is in order for that section
     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

    # insert in the correct place
     nlist[position]=currentvalue

#nlist = [14,46,43,27,57,41,45,21,70]
#insertion_sort(nlist)
#print(nlist)

size_of_list = int(input("Please enter the size of the random list. "))

my_list = random.sample(range(0,100000),size_of_list)
print(my_list)

print('Let\'s sort the list! And see how long it takes!')

# take a start time
start_time = time.time()
# run the algorithm
print(insertion_sort(my_list))
# take a finish time
finish_time = time.time() - start_time
rounded_time = (round(finish_time,5))

#print("It took: --- %s seconds ---" % (round(finish_time,5)))

print("It took in seconds: {:0.5f} ".format(rounded_time))
