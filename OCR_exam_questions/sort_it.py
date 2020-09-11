# 2017 Paper 2 June Q1
def sort_it(data_array):

    print(data_array)

    # for loop over the array from second element to the end
    for x in range(1, len(data_array)):
        current_data = data_array[x]
        position = x
        while (position > 0 and data_array[position-1] > current_data):
            data_array[position] = data_array[position-1]
            position = position - 1

        data_array[position] = current_data
        print(data_array)


nlist = [6,1,15,12,5,6,9]
sort_it(nlist)
print(nlist)