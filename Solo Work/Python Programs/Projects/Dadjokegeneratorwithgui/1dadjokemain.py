from tkinter import *
from johnsdadjokes import *
from tkmacosx import *
root = Tk()
root.title("Dadjokegenerator++")
lbl1 = Label(text="start by clicking the button", bg="#4F4948", fg="white")

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
root['bg'] = '#4F4948'
lbl1.pack()
btn1.pack()
root.mainloop()
