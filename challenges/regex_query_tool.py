import re

text_string = input("Please enter a string for checking.")
re_pattern = input("Please enter a regex pattern.")

pattern = re.compile(re_pattern)
if (pattern.match(text_string)):
    print("The text string is valid")
else:
    print("The text string is invalid")

# test scripts here
