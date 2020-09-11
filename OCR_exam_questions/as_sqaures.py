#procedure squares()
#do number = int(input("Enter a number between 1 and 100")) until number >= 1 AND number <= 100
#   for x = 1 to number
#     print(x * x)
#   next x
#endprocedure


def squares(number):
    for x in range(1, number+1):
        #print(x)
        print(x * x)


try:
    number = int(input("Enter a number between 1 and 100"))
    assert 0 <= number <= 100
    squares(number)
except AssertionError:
    print("The number you entered was incorrect")


















