'''
    Dynamically Adding Items to a List with Title and Information in a Tkinter Text Widget;

    Examples:
        AddItemList('Name', 'Carlos')
        AddItemList('Money', '1000$')

        list = ['Carlos', 'Henrique', 'Pinheiro', 'Davi', 'Luciano', 'Bruno']
        for i in list:
            AddItemList(list.index(i), i)

'''
from tkinter import *

def AddItemList(title, info):
    box.insert(END, str(title) + ': ' + str(info) + '\n')

root = Tk()
box = Text(root)

list = ['Carlos', 'Henrique', 'Pinheiro', 'Davi', 'Luciano', 'Bruno']

AddItemList('Name', 'Carlos')
AddItemList('Money', '1000$')

for i in list:
    AddItemList(list.index(i), i)

box.pack()
root.mainloop()
