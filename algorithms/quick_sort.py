# def quick_sort(a_list):
#    quick_sort_helper(a_list, 0, len(a_list) - 1)
#
#
# def quick_sort_helper(a_list, first, last):
#    if first < last:
#
#        split_point = partition(a_list, first, last)
#
#        quick_sort_helper(a_list, first, split_point - 1)
#        quick_sort_helper(a_list, split_point + 1, last)
#
#
# def partition(a_list, first, last):
#
#    pivot_value = a_list[first]
#
#    left_mark = first+1
#    right_mark = last
#
#    done = False
#    while not done:
#
#        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
#            left_mark = left_mark + 1
#
#        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
#            right_mark = right_mark -1
#
#        if right_mark < left_mark:
#            done = True
#        else:
#            temp = a_list[left_mark]
#            a_list[left_mark] = a_list[right_mark]
#            a_list[right_mark] = temp
#
#    temp = a_list[first]
#    a_list[first] = a_list[right_mark]
#    a_list[right_mark] = temp
#
#    return right_mark


def quick_sort(a_list):
    less = []
    equal = []
    greater = []

    if len(a_list) > 1:
        # define the pivot, usually the firs element in the list
        pivot = a_list[0]
        for x in a_list:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        print("Splitting: Less", less, "Pivot", equal, "Greater", greater)
        # recursive calls
        return quick_sort(less) + equal + quick_sort(greater)  # Just use the + operator to join lists
    else:  # when there is only one element in the array
        return a_list



a_list = [54,26,93,17,77,31,44,55,20]
print("Original list", a_list)
print("Sorted list", quick_sort(a_list))
