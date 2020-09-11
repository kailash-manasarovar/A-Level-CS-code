# Completed CODE for EXERCISE 3
# -------------------
# This exercise introduces  
#   * Difference border styles
#   * Pack options: 
#
# The exercise aims explores layout
from tkinter import *
import random

app = Tk() # Create the top-level window
app.title("GUI Example") # OPTIONALLY set the title

#
# Create two frames and lay these out beside each other
# Make them fill the space allocated and expand this if possible. 
# Draw a grooved border so you can see the boundary.
#
lFrame = Frame(app, bd=5, relief=GROOVE)
rFrame = Frame(app, bd=5, relief=GROOVE)
lFrame.pack(side='left',fill=BOTH, expand=1)
rFrame.pack(side='right',fill=BOTH, expand=1)

#
# Create labels inside the frames
#   - A and B inside the left frame
#   - C and D inside the right frame
#
b1 = Label(lFrame, text="A", bg='blue', width=12)
b2 = Label(lFrame, text="B", bg='white', width=12)
b3 = Label(rFrame, text="C", bg='white', width=12)
b4 = Label(rFrame, text="D", bg='blue', width=12)

#
# Pack A / C t the top and B / D at the bottom of the
#   frames that contain them
# Allow labels to fill space which expands equally 
b1.pack(side='top', fill=BOTH, expand=1)
b2.pack(side='bottom', fill=BOTH, expand=1)
b3.pack(side='top', fill=BOTH, expand=1)
b4.pack(side='bottom', fill=BOTH, expand=1)


app.mainloop() # Start the main loop
