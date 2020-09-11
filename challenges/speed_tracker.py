from datetime import datetime
import re

time_at_camera_A = input("The time recorded by camera A: ")
time_at_camera_B = input("The time recorded by camera B: ")
number_plate = input("Enter the number plate the camera records: ")

time_at_camera_A = datetime.strptime(time_at_camera_A, "%H:%M")
time_at_camera_B = datetime.strptime(time_at_camera_B, "%H:%M")
distance = 1

#something's wrong with this, what is it?
#average =  distance / (time_at_b - time_at_a)

# format the calculation correctly
time_it_takes = time_at_camera_B - time_at_camera_A
formatted_duration = (time_it_takes.seconds / 3600)
speed = distance / formatted_duration

print("The average time is {} mph".format(speed))


#check number plate
pattern = re.compile("[a-zA-Z]{2}\d{2} \d{3}")
if (pattern.match(number_plate)):
    print("Number plate is valid")
else:
    print("Number plate is invalid")



#create a file of speeders
if speed > 10:
    print("creating speeder file")
    speeders = open("cyclist.txt", "a")
    speeders.write("speeder1")
    speeders.write(" ")
    speeders.write(str(speed))
    speeders.write("mph\n")
    speeders.close()