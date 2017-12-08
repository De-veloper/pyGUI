from Tkinter import *
# w = Label ( master, option, ... )
root = Tk()

var = StringVar()

label = Label( root, textvariable=var, relief=RAISED, underline=3)

var.set("Hey!? How are you doing?")

label.pack()

root.mainloop()