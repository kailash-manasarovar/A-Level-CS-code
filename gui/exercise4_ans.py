# Comleted code for EXERCISE 4
# -------------------
# Press key
#   r - red shapes
#   y - yellow shape
#   f - fill off
#   F - fill on
#   s - square
#   c - circle
#
# The exercise aims are draw on the canvas and using more advanced events
from tkinter import *

app = Tk() # Create the top-level window
app.title("GUI Example 4") # OPTIONALLY set the title
app.geometry('400x400')  # OPTIONALLY set the size

# Create a canvas
# -----------------
#   - background is blue (this is a bit odd)
#   - make it as large as the main window
w = Canvas(app, bg='blue') 
w.pack(expand = 1, fill = BOTH)

# Event bindings
# --------------
#   Bind mouse or key press events to function
#

# Handler for the SHAPE key press event
# -------------------------------------
shape = "s"
def sKey(event):
    global shape
    print("Now drawing squares")
    shape = "s"
    
def cKey(event):
    global shape
    print("Now drawing circles")
    shape = "c"

# Bind the shape keys TO THE WINDOW
#   s for square
#   c for square
app.bind("<KeyPress-s>", sKey)
app.bind("<KeyPress-c>", cKey)

# Handler for the Colour key press event
# -------------------------------------
fillColour = None
colour = "yellow"

def fKey(event):
    global fillColour
    print("Now drawing transparent shapes")
    fillColour = None

def FKey(event):
    global fillColour
    print("Now drawing filled shapes")
    fillColour = colour

def changeColour(col):
    global fillColour, colour
    print("Now drawing in", col)
    colour = col
    if fillColour != None:
        fillColour = colour

def rKey(event):
    changeColour("red")
    
def yKey(event):
    changeColour("yellow")

app.bind("<KeyPress-f>", fKey)
app.bind("<KeyPress-F>", FKey)
app.bind("<KeyPress-r>", rKey)
app.bind("<KeyPress-y>", yKey)


# Handler for a mouse click event
# -------------------------------
#   Draw shape at mouse click   
#   
# Size is fixed
X = 50
Y = 50
def mouseClick(event):
    mx = event.x
    my = event.y
    if shape == "s":
        w.create_rectangle(mx, my, mx+X, my+Y, \
            width=5, outline=colour, fill=fillColour)
    else:
        w.create_oval(mx, my, mx+X, my+Y, width=5, \
            outline=colour, fill=fillColour)
    
# Bind the mouse click TO THE CANVAS
#   bind has a pattern and a function name
#   The pattern is "<Button-1>"
#      ... the different mouse buttons have difference numbers
w.bind("<Button-1>", mouseClick)


app.mainloop() # Start the main loop
