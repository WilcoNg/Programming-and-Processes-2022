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
cur.execute('create table if not exists assignments (primary_key integer PRIMARY KEY, title text, subject text, topic text, date_set text, date_due text)')

assignment = []
#------------------------------- Functions--------------------------------
class assignment_parameters():
    def __init__(self, title, subject, topic, date_set, date_due):
        self.title = title
        self.subject = subject
        self.topic = topic
        self.date_set = date_set
        self.date_due = date_due

e1 = ttk.Entry(root, width=20)
e2 = ttk.Entry(root, width=20)
e3 = ttk.Entry(root, width=20)
e4 = ttk.Entry(root, width=20)
e5 = ttk.Entry(root, width=20)

def addassignmenttitle():
    test1 = assignment_parameters(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
    tit = test1.title
    sub = test1.subject
    top = test1.topic
    set = test1.date_set
    due = test1.date_due
    if len(tit)==0:
        messagebox.showinfo('Empty Entry', 'Enter assignment name')
    elif len(sub)==0:
        messagebox.showinfo('Empty Entry', 'Enter subject')
    elif len(top)==0:
        messagebox.showinfo('Empty Entry', 'Enter topic')
    elif len(set)==0:
        messagebox.showinfo('Empty Entry', 'Enter date set')
    elif len(due)==0:
        messagebox.showinfo('Empty Entry', 'Enter date due')
    else:
        assignment.append(tit)
        assignment.append(sub)
        assignment.append(top)
        assignment.append(set)
        assignment.append(due)
        cur.execute('insert into assignments(title, subject, topic, date_set, date_due) values (?, ?, ?, ?, ?)', (tit, sub, top, set, due))
        listUpdate()
        e1.delete(0,'end')
        e2.delete(0,'end')
        e3.delete(0,'end')
        e4.delete(0,'end')
        e5.delete(0,'end')

def listUpdate():
    clearList()
    t1.insert('end', assignment[0])
    t2.insert('end', assignment[1])
    t3.insert('end', assignment[2])
    t4.insert('end', assignment[3])
    t5.insert('end', assignment[4])

def clearList():
    t1.delete(0,'end')
    t2.delete(0,'end')
    t3.delete(0,'end')
    t4.delete(0,'end')
    t5.delete(0,'end')

def delOne():
    try:
        val = t1.get(t1.curselection())
        if val in assignment:
            assignment.remove(val)
            listUpdate()
            cur.execute('delete from assignments where title = ?', (val,))
    except:
        messagebox.showinfo('Cannot Delete', 'No assignment Item Selected')

def deleteAll():
    mb = messagebox.askyesno('Delete All','Are you sure?')
    if mb==True:
        while(len(assignment)!=0):
            assignment.pop()
        cur.execute('delete from assignments')
        listUpdate()

def bye():
    print(assignment)
    root.destroy()

def retrieveDB():
    while(len(assignment)!=0):
        assignment.pop()
    for row in cur.execute('select title from assignments'):
        assignment.append(row[0])




#------------------------------- Function Design --------------------------------

l1 = ttk.Label(root, text = 'Assignment List')
l2 = ttk.Label(root, text='Enter assignment title: ')
l3 = ttk.Label(root, text='Enter Subject: ')
l4 = ttk.Label(root, text='Enter Topic: ')
l5 = ttk.Label(root, text='Enter Date-Set: ')
l6 = ttk.Label(root, text='Enter Date-Due: ')
l7 = ttk.Label(root, text = 'Title')
l8 = ttk.Label(root, text='Subject')
l9 = ttk.Label(root, text='Topic')
l10 = ttk.Label(root, text='Date Set')
l11 = ttk.Label(root, text='Date Due')

e2 = ttk.Entry(root, width=20)
e3 = ttk.Entry(root, width=20)
e4 = ttk.Entry(root, width=20)
e5 = ttk.Entry(root, width=20)

t1 = Listbox(root, width=20, height=20, selectmode='SINGLE')
t2 = Listbox(root, width=20, height=20, selectmode='SINGLE')
t3 = Listbox(root, width=20, height=20, selectmode='SINGLE')
t4 = Listbox(root, width=20, height=20, selectmode='SINGLE')
t5 = Listbox(root, width=20, height=20, selectmode='SINGLE')

b1 = ttk.Button(root, text='Add assignment', width=20, command=addassignmenttitle)
b2 = ttk.Button(root, text='Delete', width=20, command=delOne)
b3 = ttk.Button(root, text='Delete all', width=20, command=deleteAll)
b4 = ttk.Button(root, text='Exit', width=20, command=bye)


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
