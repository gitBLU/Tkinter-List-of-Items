# Tkinter-Lists

### Dynamically Adding Items to a List with Title and Information in a Tkinter Text Widget;


### With Text():
```python
AddItemList('Name', 'Carlos')
AddItemList('Money', '1000$')

list = ['Carlos', 'Henrique', 'Pinheiro', 'Davi', 'Luciano', 'Bruno']
for i in list:
    AddItemList(list.index(i), i)
```
### Result
![img](https://i.imgur.com/fCY3uKe.png)


### With Listbox():
```python
AddItemList('Name', 'Carlos')
AddItemList('Money', '1000$')
AddItemList('Title', 'Info', index)
list = ['Carlos', 'Henrique', 'Julio']
for i in list:
    AddItemList(list.index(i), i)
```
### Result
![img](https://i.imgur.com/pSU9aC3.png)
