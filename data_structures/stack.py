# LIFO
class Stack:
    # new method or constructor
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    # pop takes the item off
    def pop(self):
        return self.items.pop()

    # peek has a peek at it
    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        result = ""
        for i in self.items:
            result = result + " " + str(i)
        return result

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
print(s)



# LIFO
class StackSolution:
    # new method or constructor
    def __init__(self):
        self.items = [None] * 8
        self.pointer = 0

    def isEmpty(self):
        if self.pointer == 0 and self.peek() == None:
            return True
        else:
            return False

    def push(self, item):
        if self.pointer < 7:
            self.items[self.pointer] = item
            self.pointer += 1
        else:
            print("I think the stack is full")

    # pop takes the item off
    def pop(self):
        if self.pointer is not None:
            return self.items[self.pointer]
        else:
            print("nothing in the stack")

    # peek has a peek at it
    def peek(self):
        return self.items[self.pointer-1]

    def size(self):
        # the stack is always going to be size=8
        return len(self.items)

    def __str__(self):
        result = ""
        for i in self.items:
            result = result + " " + str(i)
        return result