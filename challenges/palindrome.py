input_string = input("Enter a string to check if it is a palindrome ")

# make it suitable for caseless comparison
input_string = input_string.casefold()

# reverse the string
reverse_string = reversed(input_string)

# check if the string is equal to its reverse
if list(input_string) == list(reverse_string):
   print("It is a palindrome")
else:
   print("It is not a palindrome")