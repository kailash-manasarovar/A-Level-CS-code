# Complete code for EXERCISE 5
# -------------------
# This exercise introduces  
#   * Menus
#   * Dialogs
#
# The exercise aims are to introduce menus and dialogs

from tkinter import *

app = Tk()
app.title("File Changer")
app.geometry('400x400')


# Variables
# ---------
fileName = None
fileContents = None
fileChanged = False

# Create handlers for menu items
# ------------------------------
# These function handle the menu selections
# 
# exitApp: 
#   - check no unsaved changes
# giveHelp: ask a pointles question
# aboutMsg: show an info message
# openFile: use file open dialog
#   - check for unsaved changes
#   - if file name chosen, read contents
# saveFile: save changes to file
#   - check file exists
#   - check for changes
# upperCmd: convert file to upper case
#   - check fil exists

def exitApp():
    if fileChanged:
       ans = messagebox.askquestion("Unsaved Changes", "Exit with unsaved changes?", \
                    default=messagebox.NO)
       if ans == "yes":
           app.destroy()
    else:
        app.destroy()

def giveHelp():
    ans = messagebox.askquestion("Not Much Help", "Are you sure you need help", \
                    default=messagebox.NO)

def aboutMsg():
    messagebox.showinfo("About Exercise 5", \
        "Application to change text file to upper case")

def openFile():
    if fileChanged:
        ans = messagebox.askquestion("Unsaved Changes", "Overwrite unsaved changes?", \
                    default=messagebox.NO)
        if ans == "no":
           return
    filename = filedialog.askopenfilename( \
        title="Choose a file to open", \
        filetypes=[("Text","*.txt"), ("All", "*")] )
    print(len(filename))
    if len(filename) > 0:
        readFile(filename)

def saveFile():
    if fileName == None:
        messagebox.showerror("No file", "No file open")
    elif not fileChanged:
        messagebox.showinfo("No changes", "File has not changed")
    else:
        writeFile()
        messagebox.showinfo("File written", "File updated")

def upperCmd():
    if fileName == None:
        messagebox.showerror("No file", "No file open")
        return
    upperCase()

# Actions on the file
#-------------------
def readFile(fname):
    global fileName, fileContents
    fileName = fname
    f = open(fileName)
    fileContents = f.read()
    f.close()

def writeFile():
    global fileChanged
    if fileChanged:
        f = open(fileName, 'w')
        f.write(fileContents)
        f.close()
        fileChanged = False 

def upperCase():
    global fileChanged, fileContents
    fileContents = fileContents.upper()
    fileChanged = True


# Create menu bar and menus
#-------------------
# The Menu widget is used twice
#   - for the menu bar
#   - for tne menu in the menu bar

menuBar = Menu(app)
app.winfo_toplevel()['menu'] = menuBar

file = Menu(menuBar)
file.add_command(label='Open', command=openFile)
file.add_command(label='Save', command=saveFile)
file.add_command(label='Quit', command=exitApp)
menuBar.add_cascade(label="File", menu=file)

edit = Menu(menuBar)
edit.add_command(label='Convert to upper', command=upperCmd)
menuBar.add_cascade(label="Edit", menu=edit)

hlp = Menu(menuBar)
hlp.add_command(label='Help', command=giveHelp)
hlp.add_command(label='About', command=aboutMsg)
menuBar.add_cascade(label="Help", menu=hlp)

app.mainloop()

