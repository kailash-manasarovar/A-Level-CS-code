# 2018 Paper 2 June Q6
class ItemQueue:

    # constructor new()
    def __init__(self):
        self.the_items = []
        self.head = 0
        self.tail = 0
        self.num_of_items = 0


    def set_num_of_items(self, number):
        self.num_of_items = number


    def get_num_of_items(self):
        return self.num_of_items



    def enqueuer(self, item):
        if self.num_of_items == 5:
            print("the queue is full, no more items can be added")
            return False
        else:
            self.the_items.insert(self.tail, item)
            if self.tail == 4:
                self.tail = 0
            else:
                self.tail = self.tail + 1
            self.num_of_items = self.num_of_items + 1
            return True





    def dequeuer(self):
        return self.the_items.pop(self.head)
        self.head = head + 1
        #return self.items.pop()



    # print the Queue
    def __str__(self):
        result = ""
        for i in self.the_items:
            result = result + " " + str(i)
        return result


myItems = ItemQueue()

def insert_items():
    while myItems.num_of_items < 5:
        new_item = input("Please enter an item")
        myItems.enqueuer(new_item)

    #myItems.dequeuer()

insert_items()

print(myItems)




