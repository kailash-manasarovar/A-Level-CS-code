# COMPLETED CODE for EXERCISE 6
# -----------------------------
# This exercise introduces  
#   * The radio button widget
#

# MAKE THE FOLLOWING CHANGES
#   * change the text of the radio buttons to colours
#   * when the selection is made, change th background colour of the label
#

from tkinter import *

root = Tk()

# Method handles radio button selection
#    * Create a string showing which choice selected
#    * Use this in the label
def sel():
   rb = var.get()
   selection = "You selected the option " + str(rb)
   label["text"] = selection
   if rb == 1:
      label["background"] = "red"
   elif rb == 2:
      label["background"] = "green"
   else:
      label["background"] = "blue"

# Integer control variable 
#   Holds the selection of the radio button 
var = IntVar()

# Create 3 radio buttons. Each has the same control variable
#
R1 = Radiobutton(root, text="Red", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Green", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Blue", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

# Create a label. Intially blank
label = Label(root, background = "purple", text="No selection")
label.pack()

# Start the main loop
root.mainloop()
