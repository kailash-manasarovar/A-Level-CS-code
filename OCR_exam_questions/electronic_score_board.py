#import numpy

class Board:
    def __init__(self):

        """Initializes the data."""
        self.rows_cols = [["" for x in range(15)] for y in range(3)]

        #board = numpy.zeros(3,15)


    def printBoard(self):
        for row in self.rows_cols:
            print(row)


    def clearDisplay(self):
        self.rows_cols = [["" for x in range(15)] for y in range(3)]


    def displayString(self, message, row, col):
        for i in range(len(message)):
            self.rows_cols[row][col+i] = message[i]


    def goalMessage(self, name, score, country):
        self.displayString("GOAL!",0,5)
        # figure out the name and goal bit
        self.displayString(name + " " + score,1,0)
        self.displayString(country,2,0)



esb1 = Board()
#esb1.displayString("hello", 1, 0)
#esb1.printBoard()
esb1.clearDisplay()
#esb1.displayString("BRAZIL", 1, 10)
esb1.goalMessage("EDUARDO SCHM", "01", "BRAZIL")
esb1.printBoard()