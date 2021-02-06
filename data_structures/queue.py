# FIFO
# class Queue:
#     def __init__(self):
#         self.items = []
#         #front_pointer = 0
#         #back_pointer = len(self.items)
#
#     def isEmpty(self):
#         return self.items == []
#
#     # push
#     def enqueue(self, item):
#         self.items.insert(0,item)
#
#     # pop
#     def dequeue(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
#     def __str__(self):
#         result = ""
#         for i in self.items:
#             result = result + " " + str(i)
#         return result


class Queue:
    def __init__(self):
        self.items = [None] * 8
        self.front_pointer = 0 # maybe front point is always 0
        self.back_pointer = 0

    def isEmpty(self):
        # if fp and bp are at 0 and item at 0 is None
        # return true
        pass

    # push
    def enqueue(self, item):
        # check if queue full
        # if not, move all items up 1, add the item at front pointer
        # amend front and back pointer
        pass

    # pop
    def dequeue(self):
        # check if queue full
        # remove item at end of queue
        pass

    def size(self):
        # return back pointer - 1?
        pass

    def __str__(self):
        result = ""
        for i in self.items:
            result = result + " " + str(i)
        return result

q=Queue()
q.enqueue(4)
q.enqueue('dog')
print(q)
q.enqueue(True)
print(q.size())
print(q)