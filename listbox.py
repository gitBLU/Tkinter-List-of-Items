'''
    Dynamically Adding Items to a List with Title and Information in a Tkinter Listbox;
    Examples:
        AddItemList('Name', 'Carlos')
        AddItemList('Money', '1000$')
        list = ['Carlos', 'Henrique', 'Julio']
        for i in list:
            AddItemList(list.index(i), i)
'''

from tkinter import *  
  
def AddItemList(title, info, index=-1):
    if index == -1:
        box.insert(END, str(title) + ': ' + str(info))
    else:
        box.insert(index, str(title) + ': ' + str(info))

root = Tk()  
  
root.geometry("300x250")  
root.title('Listbox List')
box = Listbox(root)  

list = ['Carlos', 'Henrique', 'Julio']
for i in list:
    AddItemList(list.index(i), i)

del_bt = Button(root, text='Remove', command = lambda listbox=box: listbox.delete(ANCHOR))
del_bt.pack()
box.pack() 
root.mainloop()  

