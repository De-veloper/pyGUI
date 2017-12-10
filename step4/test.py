from Tkinter import *

import json
#from pprint import pprint

# w = Label ( master, option, ... )

root = Tk()

def listAllPixel(pName):
	# step 1: read a json file
    rawdata = json.load(open('test.json')) # 'u' in string
    data = json.dumps(rawdata) # the whole data become string
    # Step 2: show data in GUI
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
#create a button to update value
#To do: to after update the value, show the update again

def submitBtn():
    with open('test.json', 'r') as f:
        json_data = json.load(f)
        json_data['FB'][0]['id'] = "4h4440" #change id here
    with open('test.json', 'w') as f:
        f.write(json.dumps(json_data))
        f.close()
    listAllPixel('FB')
    listAllPixel('GA')
    print "Updated!"

b = Button(root, text="Submit", command=submitBtn)
b.pack()


root.mainloop()