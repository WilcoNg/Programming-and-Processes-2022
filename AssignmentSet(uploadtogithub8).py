from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

root = Tk()
root.title('Set Assignments List')
root.geometry("800x500")

conn = sql.connect('database.db')
cur = conn.cursor()
cur.execute('create table if not exists assignments (primary_key integer PRIMARY KEY, title text, subject text, topic text, date_set text, date_due text)')

Subjects = [
    "Chemistry",
    "Calculus",
    "Physics",
    "English",
    "Biology",
    "Geography",
    "Programming"
]

subjectoption = StringVar()

subjectoption.set("Chemistry")



#------------------------------- Functions--------------------------------
e1 = ttk.Entry(root, width=20)
e2 = ttk.OptionMenu(root, subjectoption, *Subjects)
e3 = ttk.Entry(root, width=20)
e4 = ttk.Entry(root, width=20)
e5 = ttk.Entry(root, width=20)

def addassignment():

    title = e1.get()
    subject = subjectoption.get()
    topic = e3.get()
    date_set = e4.get()
    date_due = e5.get()
    if len(title)==0:
        messagebox.showinfo('Empty Entry', 'Enter assignment name')
    elif len(subject)==0:
        messagebox.showinfo('Empty Entry', 'Enter subject')
    elif len(topic)==0:
        messagebox.showinfo('Empty Entry', 'Enter topic')
    elif len(date_set)==0:
        messagebox.showinfo('Empty Entry', 'Enter date set')
    elif len(date_due)==0:
        messagebox.showinfo('Empty Entry', 'Enter date due')
    else:
        query = 'insert into assignments(title, subject, topic, date_set, date_due) values (?, ?, ?, ?, ?)'
        cur.execute(query, [title, subject, topic, date_set, date_due])
        conn.commit()
        listUpdate(title, subject, topic, date_set, date_due)
        e1.delete(0,'end')
        e3.delete(0,'end')
        e4.delete(0,'end')
        e5.delete(0,'end')

def listUpdate(title, subject, topic, date_set, date_due):
    t1.insert('end', title)
    t2.insert('end', subject)
    t3.insert('end', topic)
    t4.insert('end', date_set)
    t5.insert('end', date_due)

def select(title, subject, topic, date_set, date_due, val):
    t1.activate(val)
    t2.activate(val)
    t3.activate(val)
    t4.activate(val)
    t5.activate(val)
    print(val)

def delOne(title, subject, topic, date_set, date_due):
    try:
        conn = sql.connect('database.db')
        cur = conn.cursor()
        val = t1.curselection() or t2.curselection() or t3.curselection() or t4.curselection() or t5.curselection()
        select(title, subject, topic, date_set, date_due, val)
        cur.execute('delete from assignments where primary_key = ?', [val[0] + 1])
        conn.commit()
        t1.delete(val)
        t2.delete(val)
        t3.delete(val)
        t4.delete(val)
        t5.delete(val)
    except:
        messagebox.showinfo('Cannot Delete', 'No assignment Item Selected')


def deleteAll():
    get_all = "SELECT * FROM assignments"
    print(cur.execute(get_all).fetchall())
    mb = messagebox.askyesno('Delete All','Are you sure?')
    if mb==True:
        cur.execute('delete from assignments')
        conn.commit()
        t1.delete(0, 'end')
        t2.delete(0, 'end')
        t3.delete(0, 'end')
        t4.delete(0, 'end')
        t5.delete(0, 'end')
        get_all = "SELECT * FROM assignments"
        print(cur.execute(get_all).fetchall())

def bye():
    root.destroy()

def retrieveDB():
    get_all = "SELECT * FROM assignments"
    databaselist = cur.execute(get_all).fetchall()
    for parameters in databaselist:
        print(parameters[1], parameters[2], parameters[3], parameters[4], parameters[5])
        t1.insert('end', parameters[1])
        t2.insert('end', parameters[2])
        t3.insert('end', parameters[3])
        t4.insert('end', parameters[4])
        t5.insert('end', parameters[5])


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

t1 = Listbox(root, exportselection=False, width=20, height=20, selectmode='SINGLE')
t2 = Listbox(root, exportselection=False, width=20, height=20, selectmode='SINGLE')
t3 = Listbox(root, exportselection=False, width=20, height=20, selectmode='SINGLE')
t4 = Listbox(root, exportselection=False, width=20, height=20, selectmode='SINGLE')
t5 = Listbox(root, exportselection=False, width=20, height=20, selectmode='SINGLE')

b1 = ttk.Button(root, text='Add assignment', width=20, command=addassignment)
b2 = ttk.Button(root, text='Delete', width=20, command=lambda:delOne(e1.get(), subjectoption.get(), e3.get(), e4.get(), e5.get()))
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

retrieveDB()

root.mainloop()

conn.commit()
cur.close()
