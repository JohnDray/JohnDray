#Import Gui Apps
from tkinter import *
# Imports my jokes from the other python file
from johnsdadjokes import *
# Allows Mac Support for colours.
from tkmacosx import *
root = Tk()
# Gives the app a title
root.title("Dadjokegeneratorapp")
lbl1 = Label(text="start by clicking the button", bg="#4F4948", fg="white")

#app size to fit all the jokes
root.geometry("700x50")

def btn1click():
    lbl1.config(text=random.choice(ienfeijomodjwoqjrbufhwhfnoqhfonohoiauqoejoqj__Dadjokes))

btn1 = Button(
    root,
    text="Another Dad joke",
    borderless=True,
    bg="#11E8BD",
    command=btn1click
)
# Changes the background colours
root['bg'] = '#4F4948'

#makes my life easier to pack.
lbl1.pack()
btn1.pack()

root.mainloop()
