# find a number y that is x (given) times smaller than the original number y (not given)
# once the first digit is removed
for i in range(0,9999,57):
    str_i = str(i)
#    print(str_i[1:len(str_i)], ":", i // 7)
    if str_i[1:] == str(i//57):
        print(i)



