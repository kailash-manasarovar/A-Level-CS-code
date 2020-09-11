# http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html?highlight=linked%20list
# http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementinganOrderedList.html?highlight=linked%20list
# UNORDERED AND ORDERED LISTS
# first the Node class the lists will use
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

#temp = Node(93)
#print(temp.getData())


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

# mylist = UnorderedList()
#
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)
#
# print(mylist.size())
# print(mylist.search(93))
# print(mylist.search(100))
#
# mylist.add(100)
# print(mylist.search(100))
# print(mylist.size())
#
# mylist.remove(54)
# print(mylist.size())
# mylist.remove(93)
# print(mylist.size())
# mylist.remove(31)
# print(mylist.size())
# print(mylist.search(93))



# class OrderedList:
#     def __init__(self):
#         self.head = None
#
#     def search(self,item):
#         current = self.head
#         found = False
#         stop = False
#         while current != None and not found and not stop:
#             if current.getData() == item:
#                 found = True
#             else:
#                 if current.getData() > item:
#                     stop = True
#                 else:
#                     current = current.getNext()
#
#         return found
#
#     def add(self,item):
#         current = self.head
#         previous = None
#         stop = False
#         while current != None and not stop:
#             if current.getData() > item:
#                 stop = True
#             else:
#                 previous = current
#                 current = current.getNext()
#
#         temp = Node(item)
#         if previous == None:
#             temp.setNext(self.head)
#             self.head = temp
#         else:
#             temp.setNext(current)
#             previous.setNext(temp)
#
#     def isEmpty(self):
#         return self.head == None
#
#     def size(self):
#         current = self.head
#         count = 0
#         while current != None:
#             count = count + 1
#             current = current.getNext()
#
#         return count
#
#
# mylist = OrderedList()
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)
#
# print(mylist.size())
# print(mylist.search(93))
# print(mylist.search(100))
#
