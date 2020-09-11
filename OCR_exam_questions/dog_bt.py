from data_structures.binary_tree import Node



name = input("Enter name of breed")
root = Node("Dog1")
root.insert("Bouncer")
root.insert("Boxer")
root.insert("Chihuahua")
root.insert("Fido")
root.insert("Hound")
root.insert("Fox")
breedNode = root

not_there = False

while breedNode.left != name and not_there == False:
    if name < breedNode.data:
        if breedNode.left != None:
            breedNode = breedNode.left
        else:
            not_there = True
    else: #must be greater
        if breedNode.right != None:
            breedNode = breedNode.right
        else:
            not_there = True

if not_there == True:
    print(name + " is not in the list")
else:
    print(name + " is in the list")


