# Practice Papers Set 2 Paper 2 Section B
class Player:

    def __init__(self, id, position, money):
        self.id = id
        self.position = position
        self.money = money

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition):
        self.position = newPosition

    def getMoney(self):
        return self.money

    def setMoney(self, amount):
        self.money = amount

class Card:

    def __init__(self, amount, text):
        self.amount = amount
        self.text = text

    def getAmount(self):
        return self.amount

    def getText(self):
        return self.text


deck = [Card(1.20, "winner"), Card(-2, "loser"), Card(3.40, "hello")] # up to 40 cards maximum
headPointer = 0


def pick_deck(currentPlayer):

    global headPointer

    amount = deck[headPointer]
    print(deck[headPointer])

    currentPlayer.money = currentPlayer.getMoney() + amount

    headPointer = headPointer + 1




p = Player(10)
pick_deck(p)