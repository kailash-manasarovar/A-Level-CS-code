# 2017 Paper 2 Q6
# ----------------------------------------------
# Stay Alive!
# More programs at UsingPython.com/programs
# ----------------------------------------------

# import the modules we need, for creating a GUI
import tkinter

# only press return once
okToPressReturn = True

# the player's attributes.
hunger = 20
boredom = 0
intelligence = 0
day = 0


# -------------------------------------------------------------------

def startGame(event):
    global okToPressReturn

    if okToPressReturn == False:
        pass

    else:
        # update the time left label.
        startLabel.config(text="")
        # start updating the values
        updateHunger()
        updateDay()
        updateDisplay()

        okToPressReturn = False


# -------------------------------------------------------------------

def updateDisplay():
    # use the globally declared variables above.
    global hunger
    global day
    global boredom
    global intelligence

    if hunger >= 50:
        catPic.config(image=hungryphoto)
    else:
        catPic.config(image=normalphoto)

    # update the time left label.
    hungerLabel.config(text="Hunger: " + str(hunger) + "%")

    # update the day' label.
    dayLabel.config(text="day: " + str(day))

    # update the boredom label.
    boredomLabel.config(text="Boredom: " + str(boredom) + "%")

    # update the intelligence label.
    intelligenceLabel.config(text="Intelligence: " + str(intelligence) + "%")

    # run the function again after 100ms.
    catPic.after(100, updateDisplay)


# -------------------------------------------------------------------

def updateHunger():
    # use the globally declared variables above.
    global hunger

    # decrement the hunger.
    hunger -= 1

    if isAlive():
        # run the function again after 500ms.
        hungerLabel.after(500, updateHunger)


# -------------------------------------------------------------------
# update intelligence

# -------------------------------------------------------------------
# update boredom

# -------------------------------------------------------------------


def updateDay():
    # use the globally declared variables above.
    global day

    # decrement the hunger.
    day += 1
    updateHunger()

    if isAlive():
        # run the function again after 5 seconds.
        dayLabel.after(5000, updateDay)


# -------------------------------------------------------------------

def feed():
    global hunger

    if isAlive():
        if hunger <= 50:
            hunger += 20
        else:
            hunger -= 20


# -------------------------------------------------------------------

def isAlive():
    global hunger

    if hunger <= 0:
        # update the start info label.
        startLabel.config(text="GAME OVER! YOU KILLED HIM/HER/IT!")
        return False
    else:
        return True


# -------------------------------------------------------------------


# create a GUI window.
root = tkinter.Tk()
# set the title.
root.title("Stay Alive!")
# set the size.
root.geometry("500x300")

# add a label for the start text.
startLabel = tkinter.Label(root, text="Press 'Return' to start!", font=('Helvetica', 12))
startLabel.pack()

# add a hunger label.
hungerLabel = tkinter.Label(root, text="Hunger: " + str(hunger), font=('Helvetica', 12))
hungerLabel.pack()

# add an intelligence label


# add a boredom label


# add a 'day' label.
dayLabel = tkinter.Label(root, text="Day: " + str(day), font=('Helvetica', 12))
dayLabel.pack()

# add a 'boredom' label.
boredomLabel = tkinter.Label(root, text="Boredome: " + str(boredom), font=('Helvetica', 12))
boredomLabel.pack()

# add an 'intelligence' label.
intelligenceLabel = tkinter.Label(root, text="Intelligence: " + str(intelligence), font=('Helvetica', 12))
intelligenceLabel.pack()

hungryphoto = tkinter.PhotoImage(file="hungry.gif")
normalphoto = tkinter.PhotoImage(file="normal.gif")

# add a cat image
catPic = tkinter.Label(root, image=normalphoto)
catPic.pack()

btnFeed = tkinter.Button(root, text="Feed Me", command=feed)
btnFeed.pack()

# run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)

# start the GUI
root.mainloop()