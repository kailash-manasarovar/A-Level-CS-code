# Practice Papers Set 1 Paper 2 Section B
grid  = [[" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", "R", "Y", "R", " ", " ", " "],
         [" ", "Y", "R", "R", "Y", " ", " "],
         ["R", "Y", "R", "R", "Y", "R", " "],
    ]



def player_turn(letter, column):
    # check is colum full
    if grid[0][column] != " ":
        print("column is full")
    else:
        for i in range(len(grid)-1, 0, -1):
            if grid[i][column] == " ":
                grid[i][column] = letter
                break

print(grid)
player_turn("Y", 2)
print(grid)


def playDisc(removeColumn):
    grid[0][removeColumn] = " "
    for i in range(1, len(grid)-2):
        grid[i][removeColumn] = grid[i-1][removeColumn]
