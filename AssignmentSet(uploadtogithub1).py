from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

root = Tk()
frame = Frame(root)
root.title('Set Assignments List')
root.geometry("800x500")

conn = sql.connect('database.db')
cur = conn.cursor()
cur.execute('create table if not exists tasks (title text)')

task = []
#------------------------------- Functions--------------------------------
class assignment_parameters():
    def __init__(self, title, subject, topic, date_set, date_due):
        self.title = title
        self.subject = subject
        self.topic = topic
        self.date_set = date_set
        self.date_due = date_due

e1 = ttk.Entry(root, width=20)

def addTasktitle():
    test1 = assignment_parameters(e1.get(), "chem", "3.2", "26th", "30th")
    word = test1.title
    if len(word)==0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        task.append(word)
        cur.execute('insert into tasks values (?)', (word,))
        listUpdate()
        e1.delete(0,'end')

def listUpdate():
    clearList()
    for i in task:
        t1.insert('end', i)

def clearList():
    t1.delete(0,'end')

def delOne():
    try:
        val = t1.get(t1.curselection())
        if val in task:
            task.remove(val)
            listUpdate()
            cur.execute('delete from tasks where title = ?', (val,))
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')

def deleteAll():
    mb = messagebox.askyesno('Delete All','Are you sure?')
    if mb==True:
        while(len(task)!=0):
            task.pop()
        cur.execute('delete from tasks')
        listUpdate()

def bye():
    print(task)
    root.destroy()

def retrieveDB():
    while(len(task)!=0):
        task.pop()
    for row in cur.execute('select title from tasks'):
        task.append(row[0])




#------------------------------- Function Design --------------------------------

l1 = ttk.Label(root, text = 'Assignment List')
l2 = ttk.Label(root, text='Enter task title: ')
l3 = ttk.Label(root, text='Enter Subject: ')
l4 = ttk.Label(root, text='Enter Topic: ')
l5 = ttk.Label(root, text='Enter Date-Set: ')
l6 = ttk.Label(root, text='Enter Date-Due: ')
l7 = ttk.Label(root, text = 'Title')
l8 = ttk.Label(root, text='Subject')
l9 = ttk.Label(root, text='Topic')
l10 = ttk.Label(root, text='Date Set')
l11 = ttk.Label(root, text='Date Due')

e1 = ttk.Entry(root, width=20)
e2 = ttk.Entry(root, width=20)
e3 = ttk.Entry(root, width=20)
e4 = ttk.Entry(root, width=20)
e5 = ttk.Entry(root, width=20)

t1 = Listbox(root, width=20, height=20, selectmode='SINGLE')
t2 = Listbox(root, width=20, height=20, selectmode='SINGLE')
t3 = Listbox(root, width=20, height=20, selectmode='SINGLE')
t4 = Listbox(root, width=20, height=20, selectmode='SINGLE')
t5 = Listbox(root, width=20, height=20, selectmode='SINGLE')

b1 = ttk.Button(root, text='Add task', width=20, command=addTasktitle)
b2 = ttk.Button(root, text='Delete', width=20, command=delOne)
b3 = ttk.Button(root, text='Delete all', width=20, command=deleteAll)
b4 = ttk.Button(root, text='Exit', width=20, command=bye)

retrieveDB()
listUpdate()

#Place geometry
l1.place(x=50, y=10)
l2.place(x=50, y=395)
l3.place(x=200, y=395)
l4.place(x=350, y=395)
l5.place(x=500, y=395)
l6.place(x=650, y=395)
l7.place(x=50, y=40)
l8.place(x=200, y=40)
l9.place(x=350, y=40)
l10.place(x=500, y=40)
l11.place(x=650, y=40)


e1.place(x=50, y=415)
e2.place(x=200, y=415)
e3.place(x=350, y=415)
e4.place(x=500, y=415)
e5.place(x=650, y=415)

b1.place(x=100, y=465)
b2.place(x=250, y=465)
b3.place(x=400, y=465)
b4.place(x=550, y =465)

t1.place(x=50, y = 60)
t2.place(x=200, y = 60)
t3.place(x=350, y = 60)
t4.place(x=500, y = 60)
t5.place(x=650, y = 60)

root.mainloop()

conn.commit()
cur.close()
