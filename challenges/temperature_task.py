'''
Created on 9 Jun 2018

@author: katharinemurphy
'''
#global variables
number_of_days = 10
hottest_day_index = 0
coldest_day_index = 0
#test data
midday_temperature = [1,2,3,4,5,6,7,8,9,10]
midnight_temperature = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]

#input to the array
for i in range():
    while True:
        try:
            midday_temp = float(input("Please enter the midday temperature: "))
            midnight_temp = float(input("Please enter the midnight temperature: "))
        except ValueError:
            print("Error: You must only enter a number, such as 12.7")
        else:
            if midday_temp >= -15 and midday_temp <= 50:
                midday_temperature.append(midday_temp)  # temp only gets added to list when it fulfils the range rules
            if midnight_temp >= -15 and midnight_temp <= 50: 
                midnight_temperature.append(midnight_temp)
                break
            else:
                print("Entry out of range")  # if it fails the check, it gives an error message
       


# user defined function for average temperature
def average_temp(temp_array):
    if not temp_array:
        print("List is empty")
    else:
        total = 0
        for temperature in temp_array:
            total = total + temperature
            #test line
            print(total)
            average = (total / number_of_days)
    return average


print("Day average:", average_temp(midday_temperature))
print("Night average:", average_temp(midnight_temperature))


# max check user defined function
def max(array):
    highest_temperature = -273
    hottest_day_index = 0
    for temp in array:
        if temp > highest_temperature:
            highest_temperature = temp
            hottest_day_index = hottest_day_index + 1
    return highest_temperature    
        
# min check user defined function
def min(array):
    coldest_temperature = 500
    coldest_day_index = 0
    for temp in array:
        if temp < coldest_temperature:
            coldest_temperature = temp
            coldest_day_index = coldest_day_index + 1
    return coldest_temperature


print("Highest temperature:", max(midday_temperature), "on day", hottest_day_index)
print("Coldest temperature:", min(midnight_temperature), "on day", coldest_day_index)



