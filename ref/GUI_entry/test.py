from Tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.insert(0, 'username')
E1.pack(side = RIGHT)

top.mainloop()