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

# s=Stack()
#
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())