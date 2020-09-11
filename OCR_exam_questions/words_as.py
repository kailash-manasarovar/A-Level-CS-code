words=["REMEMBER", "TO", "TAKE", "CHARLIE", "TO", "THE", "DENTIST", "THIS", "AFTERNOON"]

print(words)

# create the display with correct dimensions
display = []
for j in range(4):
    column = []
    for i in range(20):
        column.append("")
    display.append(column)
#print(display)



def update_display(words):
    row = 0
    col = 0

    for i in range(0, len(words)):
        #print("i = ", i)
        temp = words[i] + " "
        #print("Popped word = ", temp)

        if col + len(temp) > 20:
            row = row + 1
            col = 0

        for j in temp:
            #print(j)
            display[row][col] = j
            col = col + 1

    return display

print(update_display(words))



