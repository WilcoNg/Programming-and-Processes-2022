from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql


class MainApp(Tk):
    def __init__(self, *kw, **kwarg):
        Tk.__init__(self, *kw, **kwarg)

        self.title('Set Assignments List')
        self.geometry("800x500")

        self.Subjects = [
            "Chemistry",
            "Calculus",
            "Physics",
            "English",
            "Biology",
            "Geography",
            "Psychology",
            "Statistics",
            "History",
            "Programming"
        ]

        self.subjectoption = StringVar()

        self.subjectoption.set("Chemistry")

        self.frame = ttk.Frame(self)
        self.frame.pack(fill="both", expand=1)

        self.l1 = ttk.Label(self.frame, text='Assignment List')
        self.l2 = ttk.Label(self.frame, text='Enter assignment title: ')
        self.l3 = ttk.Label(self.frame, text='Enter Subject: ')
        self.l4 = ttk.Label(self.frame, text='Enter Topic: ')
        self.l5 = ttk.Label(self.frame, text='Enter Date-Set: ')
        self.l6 = ttk.Label(self.frame, text='Enter Date-Due: ')
        self.l7 = ttk.Label(self.frame, text='Title')
        self.l8 = ttk.Label(self.frame, text='Subject')
        self.l9 = ttk.Label(self.frame, text='Topic')
        self.l10 = ttk.Label(self.frame, text='Date Set')
        self.l11 = ttk.Label(self.frame, text='Date Due')

        self.e1 = ttk.Entry(self.frame, width=20)
        self.e2 = ttk.OptionMenu(
            self.frame,
            self.subjectoption,
            *self.Subjects
            )
        self.e3 = ttk.Entry(self.frame, width=20)
        self.e4 = ttk.Entry(self.frame, width=20)
        self.e5 = ttk.Entry(self.frame, width=20)

        self.t1 = Listbox(
            self.frame,
            exportselection=False,
            width=20, height=20,
            selectmode='SINGLE'
            )
        self.t2 = Listbox(
            self.frame,
            exportselection=False,
            width=20, height=20,
            selectmode='SINGLE'
            )
        self.t3 = Listbox(
            self.frame,
            exportselection=False,
            width=20, height=20,
            selectmode='SINGLE'
            )
        self.t4 = Listbox(
            self.frame,
            exportselection=False,
            width=20, height=20,
            selectmode='SINGLE'
            )
        self.t5 = Listbox(
            self.frame,
            exportselection=False,
            width=20, height=20,
            selectmode='SINGLE'
            )

        self.b1 = ttk.Button(
            self.frame,
            text='Add assignment',
            width=20,
            command=self.addassignment
            )
        self.b2 = ttk.Button(
            self.frame,
            text='Delete',
            width=20,
            command=lambda: self.delOne(
                        self.e1.get(),
                        self.subjectoption.get(),
                        self.e3.get(),
                        self.e4.get(),
                        self.e5.get()
                        ))
        self.b3 = ttk.Button(
            self.frame,
            text='Delete all',
            width=20,
            command=self.deleteAll
            )
        self.b4 = ttk.Button(
            self.frame,
            text='Exit',
            width=20,
            command=self.bye
            )

        self.l1.place(x=50, y=10)
        self.l2.place(x=50, y=395)
        self.l3.place(x=200, y=395)
        self.l4.place(x=350, y=395)
        self.l5.place(x=500, y=395)
        self.l6.place(x=650, y=395)
        self.l7.place(x=50, y=40)
        self.l8.place(x=200, y=40)
        self.l9.place(x=350, y=40)
        self.l10.place(x=500, y=40)
        self.l11.place(x=650, y=40)

        self.e1.place(x=50, y=415)
        self.e2.place(x=200, y=415)
        self.e3.place(x=350, y=415)
        self.e4.place(x=500, y=415)
        self.e5.place(x=650, y=415)

        self.b1.place(x=100, y=465)
        self.b2.place(x=250, y=465)
        self.b3.place(x=400, y=465)
        self.b4.place(x=550, y=465)

        self.t1.place(x=50, y=60)
        self.t2.place(x=200, y=60)
        self.t3.place(x=350, y=60)
        self.t4.place(x=500, y=60)
        self.t5.place(x=650, y=60)

    def addassignment(self):
        title = self.e1.get()
        subject = self.subjectoption.get()
        topic = self.e3.get()
        date_set = self.e4.get()
        date_due = self.e5.get()
        if len(title) == 0:
            messagebox.showinfo('Empty Entry', 'Enter assignment name')
        elif len(subject) == 0:
            messagebox.showinfo('Empty Entry', 'Enter subject')
        elif len(topic) == 0:
            messagebox.showinfo('Empty Entry', 'Enter topic')
        elif len(date_set) == 0:
            messagebox.showinfo('Empty Entry', 'Enter date set')
        elif len(date_due) == 0:
            messagebox.showinfo('Empty Entry', 'Enter date due')
        else:
            query = 'insert into assignments(title, subject, topic, date_set, date_du) \
            values(?, ?, ?, ?, ?)'
            cur.execute(query, [title, subject, topic, date_set, date_due])
            conn.commit()
            self.listUpdate(title, subject, topic, date_set, date_due)
            self.e1.delete(0, 'end')
            self.e3.delete(0, 'end')
            self.e4.delete(0, 'end')
            self.e5.delete(0, 'end')

    def listUpdate(self, title, subject, topic, date_set, date_due):
        self.t1.insert('end', title)
        self.t2.insert('end', subject)
        self.t3.insert('end', topic)
        self.t4.insert('end', date_set)
        self.t5.insert('end', date_due)

    def select(self, title, subject, topic, date_set, date_due, val):
        self.t1.activate(val)
        self.t2.activate(val)
        self.t3.activate(val)
        self.t4.activate(val)
        self.t5.activate(val)

    def delOne(self, title, subject, topic, date_set, date_due):
        try:
            conn = sql.connect('database.db')
            cur = conn.cursor()
            val = self.t1.curselection() or \
                self.t2.curselection() or \
                self.t3.curselection() or \
                self.t4.curselection() or \
                self.t5.curselection()
            self.select(title, subject, topic, date_set, date_due, val)
            cur.execute(
                'delete from assignments where primary_key = ?',
                [val[0] + 1]
                )
            conn.commit()
            self.t1.delete(val)
            self.t2.delete(val)
            self.t3.delete(val)
            self.t4.delete(val)
            self.t5.delete(val)
        except:
            messagebox.showinfo('Cannot Delete', 'No assignment Item Selected')

    def deleteAll(self):
        get_all = "SELECT * FROM assignments"
        print(cur.execute(get_all).fetchall())
        mb = messagebox.askyesno('Delete All', 'Are you sure?')
        if mb is True:
            cur.execute('delete from assignments')
            conn.commit()
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            self.t3.delete(0, 'end')
            self.t4.delete(0, 'end')
            self.t5.delete(0, 'end')
            get_all = "SELECT * FROM assignments"
            print(cur.execute(get_all).fetchall())

    def bye(self):
        self.destroy()

    def retrieveDB(self):
        get_all = "SELECT * FROM assignments"
        databaselist = cur.execute(get_all).fetchall()
        for parameters in databaselist:
            self.t1.insert('end', parameters[1])
            self.t2.insert('end', parameters[2])
            self.t3.insert('end', parameters[3])
            self.t4.insert('end', parameters[4])
            self.t5.insert('end', parameters[5])

root = MainApp()

conn = sql.connect('database.db')
cur = conn.cursor()
cur.execute('create table if not exists assignments(primary_key integer PRIMARY KEY, \
title text, subject text, topic text, date_set text, date_due text)')

root.retrieveDB()

root.mainloop()

conn.commit()
cur.close()
