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
        labelList = '%s%s:' % (pName,(x+1))
        Label( root, text=labelList, relief=RAISED,fg="red",font=("Helvetica", 16),padx=10, bd=0,width=5).grid(row=x)
        Label( root, text='ID', relief=RAISED,fg="red",font=("Helvetica", 16),padx=10, bd=0,width=5).grid(row=x,column=1)

        E[pName].append({'id':'','name':''})
        E[pName][x]['id'] = Entry(root, bd=5)
        E[pName][x]['id'].grid(row=(x), column=2)
        E[pName][x]['id'].insert(0, '%s' % rawdata[pName][x]['id'])
    

#Load FB, GA
listAllPixel('FB')
#listAllPixel('GA')
print E

#step3
#create a button to update value
#To do: to after update the value, show the update again

def submitBtn():
    with open('test.json', 'r') as f:
        json_data = json.load(f)
        
        for x in range(len(json_data['FB'])):
            json_data['FB'][x]['id'] = E['FB'][x]['id'].get() #change id here
        #for y in range(len(json_data['GA'])):
        #    json_data['GA'][y]['id'] = E['GA'][y]['id'].get() #change id here

    with open('test.json', 'w') as f:
        f.write(json.dumps(json_data))
        f.close()

    Label(root,text='Updated!').grid(row=5,column=0)
    
    b.grid_forget(); #remvoe from the view
    c.grid(row=5)
    

    print "Updated!"
    print json.dumps(json_data)

b = Button(root, text="Submit", command=submitBtn)
b.grid(row=7)

c = Button(root, text="Cancel", command=root.destroy)
c.grid(row=7,column=1)


root.mainloop()