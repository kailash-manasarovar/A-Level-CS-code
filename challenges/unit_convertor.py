def convert_currency(orig, to, rate):
    amount = float(orig)
    conversion = amount * float(rate)
    print("{} is equal to {} {}.".format(orig, conversion, to))



orig = input("How much do you want to convert?")
to = input("What currency do you want back?")
rate = input("What is the rate right now?")


convert_currency(orig, to, rate)