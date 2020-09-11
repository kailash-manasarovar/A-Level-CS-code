# user input
entry = int(input("Entry please"))

# set variables
max = 5
green_light = 1
red_light = 0

# do boolean check for BRP FALSE
if (max - entry) < 0:
    print(red_light)

# do boolean check for BRP TRUE
elif (max - entry >= 0) and (max - entry < 6):
    print(green_light)