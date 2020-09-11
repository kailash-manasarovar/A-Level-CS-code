# COMPLETED CODE for EXERCISE 2B
# ------------------------------
# This exercise introduces  
#   * The label widget (part A)
#   * The entry widget (part B)
#
# The exercise explores setting and getting attributes

from tkinter import *

# Create the top level window
app = Tk()
app.title("GUI Example")
app.geometry('200x100')

# This method 
#    * check if text has been entered
#    * if no text: make button red
#    * if text: copy it to the label
#    * then change button text to "Clear Text" and set a second command
def copyTextToLabel():
    t = v.get()
    if len(v.get()) == 0: # check if the text is null
        b1['bg'] = 'red'  # set button background red
    else:
        l1['text'] = v.get() # otherwise update the label text
        b1['bg'] = b1BgColor # restore button background
        b1['text'] = 'Clear Text' # ... and text
        b1['command'] = clearEntryText # ... and command

# This method 
#    * clear the text for the Entry widget
#    * restores the button command and text
def clearEntryText():
    v.set("")
    b1['text'] = 'Copy Text'
    b1['command'] = copyTextToLabel
    

# Create a button
b1 = Button(app, text="Copy Text", command=copyTextToLabel)
b1BgColor = b1['bg']

# Create a label
l1 = Label(app, text="Text is displayed here")

# A StringVar is a special variable that can be used to
# hold the string entered in an Entry widget
#
# Use v.get() to get the string from the variable
v = StringVar()

# Create an entry widget
e1 = Entry(app, textvariable = v)

# Pack the three widget into the window
l1.pack(side='bottom')
b1.pack(side='bottom')
e1.pack(side='bottom')

app.mainloop()
