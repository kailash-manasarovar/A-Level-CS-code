import pickle

#INVENTORY = 1001

class Item():
    def __init__(self):
        self.ID = self.Location = 0
        self.Description = self.Status = self.Name = self.Commands = self.Results = ""



def createItems(Items):

    for Count in range(0, 10):
        TempItem = Item()
        TempItem.ID = Count
        TempItem.Description = Count
        TempItem.Status = Count
        TempItem.Location = Count
        TempItem.Name = Count
        TempItem.Commands = Count
        TempItem.Results = Count
        Items.append(TempItem)
    return Items






def DisplayInventory(Items):
    print(Items)
#    print("You are currently carrying the following items:")
#    for Thing in Items:
#        if Thing.Location == INVENTORY:
#            print(Thing.Name)


def main_runner():
    Items = []
    createItems(Items)

    for i in Items:

        print(i.Name)


main_runner()