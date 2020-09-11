mylist = ["Linux", "Mac OS" , "Windows"]
# Print the first list element
print(mylist[0])
# Print the last element
# Negative values starts the list from the end
print(mylist[-1])
# Sublist - first and second element
print(mylist[0:2])
# Add elements to the list
mylist.append("Android")
# Print the content of the list
for element in mylist:
    print(element)
    
mylist2 = ["Linux", "Linux" , "Windows"]
print(mylist2)
# remove duplicates from the list
mylist2 = list(set(mylist2))
print(mylist2)