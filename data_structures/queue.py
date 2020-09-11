# FIFO
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # push
    def enqueue(self, item):
        self.items.insert(0,item)

    # pop
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        result = ""
        for i in self.items:
            result = result + " " + str(i)
        return result


#
# q=Queue()
# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)
# print(q.size())
# print(q)