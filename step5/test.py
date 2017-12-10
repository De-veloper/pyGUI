from Tkinter import *

import json
#from pprint import pprint

# w = Label ( master, option, ... )

root = Tk()

E = {'FB':[],'GA':[]} #defne Entry feild as an array,; make it as public

def listAllPixel(pName):
    # step 1: read a json file
    rawdata = json.load(open('test.json')) # 'u' in string
    data = json.dumps(rawdata) # the whole data become string
    # Step 2: show data in GUI
    for x in range(len(rawdata[pName])):
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED,fg="red",font=("Helvetica", 16),padx=10, bd=0,width=5)
        labelList = '%s%s:' % (pName,(x+1))
        var.set(labelList)
        label.pack()

        E[pName].append({'id':'','name':''})
        E[pName][x]['id'] = Entry(root, bd=5)
        E[pName][x]['id'].insert(0, '%s' % rawdata[pName][x]['id'])
        E[pName][x]['id'].pack()
    

#Load FB, GA
listAllPixel('FB')
listAllPixel('GA')
print E

#step3
#create a button to update value
#To do: to after update the value, show the update again

def submitBtn():
    with open('test.json', 'r') as f:
        json_data = json.load(f)
        
        for x in range(len(json_data['FB'])):
            json_data['FB'][x]['id'] = E['FB'][x]['id'].get() #change id here
        for y in range(len(json_data['GA'])):
            json_data['GA'][y]['id'] = E['GA'][y]['id'].get() #change id here

    with open('test.json', 'w') as f:
        f.write(json.dumps(json_data))
        f.close()

    label = Label(root,text='Updated!')
    label.pack()

    print "Updated!"
    print json.dumps(json_data)

b = Button(root, text="Submit", command=submitBtn)
b.pack()


root.mainloop()