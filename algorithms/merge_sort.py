def merge(a_list):
    print("Splitting ", a_list)
    if len(a_list)>1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge(left_half)
        merge(right_half)
        i=j=k=0
        # while all lists have more than one element
        while i < len(left_half) and j < len(right_half):
            # check the order and add to new list identified by k depending on order
            if left_half[i] < right_half[j]:
                a_list[k]=left_half[i]
                i=i+1
            else:
                a_list[k]=right_half[j]
                j=j+1
            k=k+1

        # check for the situations in which only one half has more than one element / in the case of odd numbers
        while i < len(left_half):
            a_list[k]=left_half[i]
            i=i+1
            k=k+1

        while j < len(right_half):
            a_list[k]=right_half[j]
            j=j+1
            k=k+1
    print("Merging ", a_list)

my_list = [14,46,43,27,57,41,45,21,70]
merge(my_list)
print(my_list)



