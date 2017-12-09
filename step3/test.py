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
#var = StringVar()
#label = Label( root, textvariable=var, relief=RAISED, underline=3)
#var.set('Test')
#label.pack()

for x in rawdata["FB"]:
    FBvar = StringVar()
    FBPixel = Label( root, textvariable=FBvar, relief=RAISED)
    FBList = 'FB: %s' % x['id']
    FBvar.set(FBList)
    FBPixel.pack()

GAvar = StringVar()
GAPixel = Label( root, textvariable=GAvar, relief=RAISED)
GAvar.set('GA1: %s' % rawdata["GA"][0]["id"])
GAPixel.pack()

root.mainloop()