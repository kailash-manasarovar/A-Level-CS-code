# the first thing the program does is add every tag in a piece of text to the data structure A
# Practice Papers Set 1 Paper 1 Q6
from data_structures.queue import Queue

html_code = "<html><head><title></title></head><body></body></html>"
data_structure_A = Queue()

start_tag_position = 0
for i in range(len(html_code)):
    if html_code[i] == ">":
        data_structure_A.enqueue(html_code[start_tag_position:i+1])
        start_tag_position = i+1

#print(data_structure_A.size())
#print(data_structure_A)

# data structure b is given a closing tag, and gives the corresponding opening tag = HASHMAP
# i.e. data_structure_b.get("</head>") returns "<head>"
# we don't have to pseudocode it, we assume it works
# here is the Python implementation
data_structure_B = {
	"</head>" : "<head>",
	"</title>" : "</title>",
	"</body>" : "<body>",
	"</html>" : "</html>"
}

# data structure C is a stack, let's make a new stack
from data_structures import stack
data_structure_C = stack.Stack()

def check_tags(data_structure):
     valid = True
     while valid is True and data_structure_A.isEmpty() is not True:
         tag = data_structure_A.dequeue()
         # if tag is a closing tag, check against data_structure_b hashmap
         if tag[1:2]=="/":
             if data_structure_B.get(tag) != tag.replace("/",""):
                print(tag)
                print(tag.replace("/",""))
                valid = False
             else:
                 data_structure_C.push(tag)
                 valid = True
     return valid


# need to fix this
print(check_tags(data_structure_A))