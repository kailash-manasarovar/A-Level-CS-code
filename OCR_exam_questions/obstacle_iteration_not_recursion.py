# Practice Papers Set 1 Paper 2 Q2
import random

board = [["start", 1, 2, 3, 4, 5, 6, 7],
        [15, 14, 13, 12, 11, 10, 9, 8],
        [16, 17, 18, 19, 20, 21, 22, 23],
        [31, 30, 29, 28, 27, 26, 25, 24],
        [32, 33, 34, 35, 36, 37, 38, 39],
        [47, 46, 45, 44, 43, 42, 41, 40],
        [48, 49, 50, 51, 52, 53, 54, 55],
        ["end", 62, 61, 60, 59, 58, 57, 56]
    ]

class Obstacle:

    # constructor new()
    def __init__(self, x, y):
        self.x = x
        self.y = y

# recursion
def generateObstacle(diceNumber):
   if diceNumber == 0:
       return True
   else:
       x = random.randint(0,7)
       y = random.randint(0,7)
       board[x, y] = Obstacle(x, y)
       generateObstacle(diceNumber-1)


# iteration
def generateObstacleIteratively(diceNumber):
    while diceNumber != 0:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        # if board[x, y] == "" return True
        board[x, y] = Obstacle(x, y)
        diceNumber = diceNumber - 1