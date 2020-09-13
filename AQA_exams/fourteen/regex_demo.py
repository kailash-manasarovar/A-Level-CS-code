# https://www.w3schools.com/python/python_regex.asp
# Chapter 20 page 165
# https://docs.python.org/3/library/re.html
import re

# pattern = r"Cookie"
# sequence = "Cookie"
# if re.match(pattern, sequence):
#     print("Match!")
# else: print("Not a match!")


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")


re.search(r'Co.k.e', 'Cookie').group()
re.search(r'^Eat', "Eat cake!").group()
re.search(r'cake$', "Cake! Let's eat cake").group()


