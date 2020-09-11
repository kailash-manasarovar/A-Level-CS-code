# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import math


# To take coefficient input from the users
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

d = b**2-4*a*c # discriminant

if d < 0:
    print("This equation has no real solution")
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print("This equation has one solutions: ", x)
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print("This equation has two solutions: ", x1, " and", x2)