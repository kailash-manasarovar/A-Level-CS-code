# Practice Papers Set 1 Paper 2 Q5
def fun1(x):
    flag = False
    y=""
    if x<0:
        flag = True
        x = x * -1
    while (x > 0):
        y = str(x % 2) + y
        x = x // 2
        #print(x)
    if flag == True:
        y = "1" + y
    else:
        y = "0" + y
    print(y)


fun1(10)
fun1(-13)