# test_array = ["A", "B", "C", "D", "E"]
# new_array = ["", "", "", "", "", ""]
# shift_amount = 4
#
# new_array = test_array[shift_amount:] + test_array[:shift_amount]
#
# print(new_array)


## THE ANSWER
# i = row number from the 2D array
# x = amount to shift - KEY
def shiftRow(i, x):
    shifted_row = i[x:] + i[:x]
    print(shifted_row)

# left shift
shiftRow(["A", "B", "C", "D", "E"],2)
# right shift
shiftRow(["A", "B", "C", "D", "E"],-2)




