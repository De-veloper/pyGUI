from Tkinter import *

import json
from pprint import pprint

# w = Label ( master, option, ... )
# Try to read a json file

# step 1: read a json file
rawdata = json.load(open('test.json')) # 'u' in string
data = json.dumps(rawdata) # the whole data become string

#pprint(loaddata)
#pprint(rawdata)

# Step 2: show data in GUI
root = Tk()

def listAllPixel(pName):
    for x in range(len(rawdata[pName])):
	    var = StringVar()
	    label = Label( root, textvariable=var, relief=RAISED,fg="red",font=("Helvetica", 16),padx=10,bd=0)
	    labelList = '%s%s: %s' % (pName,(x+1),rawdata[pName][x]['id'])
	    var.set(labelList)
	    label.pack()

#Load FB, GA
listAllPixel('FB')
listAllPixel('GA')

#step3
#create a button

def submitBtn():
    print "click!"

b = Button(root, text="Submit", command=submitBtn)
b.pack()


root.mainloop()