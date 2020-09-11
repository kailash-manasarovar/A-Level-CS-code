# SAMPLE ASSESSMENT MATERIAL Paper 2 Q10
class Tower:

    # constructor new()
    def __init__(self):
        self.arraypole = []
        self.counter = 0

    # tells you if the stack is empty
    def isEmpty(self):
        return self.arraypole == []

    # puts an element on the stack
    def push(self, diskValue):
        #if self.isEmpty():
        if self.counter == 0:
            self.arraypole.append(diskValue)
        # this part does the validation of the diskValue making sure it is smaller than the one there
        elif diskValue < self.arraypole[self.counter]:
            self.arraypole.append(diskValue)
            self.counter = self.counter + 1
        # this is what happens if the move is invalid
        else:
            print("Invalid move")

    # take an element off the stack
    def pop(self):
        return self.arraypole.pop()

    # looks at the top of the stack but doesn't remove any elements
    def peek(self):
        if self.isEmpty():
            print(999)
        else:
            print(self.arraypole[len(self.arraypole) - 1])

    # tells you how big the stack is
    def size(self):
        return len(self.arraypole)

    # prints the stack
    def __str__(self):
        result = ""
        for i in self.arraypole:
            result = result + " " + str(i)
        return result



noOfDisks = 5

tower1 = Tower()
tower2 = Tower()
tower3 = Tower()


i=noOfDisks
while i>0:
    tower1.push(i)
    i=i-1

finished = False

while finished != True:

    # set finished to False if noOfDisks = 999

    # make the valid move between tower1 and tower3
    if tower3.isEmpty():
        tower3.push(tower1.pop())
    elif tower3.peek() < tower1.peek():
        pass
    else:
        tower3.peek() > tower1.peek()
        tower3.push(tower1.pop())

    # make the valid move between tower1 and tower2

    # make the valid move between tower3 and tower2
