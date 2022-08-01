from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

#main class containing the functions as well as certain parameters
#made the code tidy and suited the conventions of python programming
class MainApp(Tk):
    #kw and kwarg is so that the class and its contents can inherit all the properties of tkinter
    #this was so that I didn't need to type out everything in the parameters each time
    def __init__(self, *kw, **kwarg):
        Tk.__init__(self, *kw, **kwarg)

        #window dimensions and title
        self.title('Set Assignments List')
        self.geometry("800x500")

        #list of subjects for the drop down menu
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

        #to make the list into a dropdown menu
        self.subjectoption = StringVar()

        #defult selected option for the drop down
        self.subjectoption.set("Chemistry")

        #fill and expand is used to make sure that the window takes up as much space as it's allowed
        self.frame = ttk.Frame(self)
        self.frame.pack(fill="both", expand=1)

        #labels/text
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

        #entry boxes as well as the dropdown menu widget for subjects in e2
        self.e1 = ttk.Entry(self.frame, width=20)
        self.e2 = ttk.OptionMenu(
            self.frame,
            self.subjectoption,
            *self.Subjects
            )
        self.e3 = ttk.Entry(self.frame, width=20)
        self.e4 = ttk.Entry(self.frame, width=20)
        self.e5 = ttk.Entry(self.frame, width=20)

        #Listbox dimensions as well as false exportselection inorder to keep the selected text highlighted
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

        #button widgets each with a different function attached to it
        #button 2 is for the delete one row hence the parameters along with lambda to bypass the undefined variables
        self.b1 = ttk.Button(
            self.frame,
            text='Add assignment',
            width=20,
            command=self.add_assignment
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
            command=self.delAll
            )
        self.b4 = ttk.Button(
            self.frame,
            text='Exit',
            width=20,
            command=self.bye,
            )

        #placements for each of the components
        #place was used instead of pack as it allows for specific x and y coords which helped alot with the delicate allignment of my program
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

    #add assignment function
    def add_assignment(self):
        #each of the values from the input boxes as well as the drop down menu is given
        title = self.e1.get().strip()
        subject = self.subjectoption.get()
        topic = self.e3.get().strip()
        date_set = self.e4.get().strip()
        date_due = self.e5.get().strip()
        #if a certain input box is empty then the corresponding message will pop up for that box
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
        #if none of the input boxes are empty then the program will add the values to the database
        else:
            #query was written seperately as it was long and would be messy in the ()
            query = 'insert into assignments(title, subject, topic, date_set, date_due) \
            values(?, ?, ?, ?, ?)'
            cur.execute(query, [title, subject, topic, date_set, date_due])
            #saves the new values into the database
            conn.commit()
            self.listUpdate(title, subject, topic, date_set, date_due)
            #removes what is in the input boxes so that the user can type the next values in without having to delete the previous ones
            self.e1.delete(0, 'end')
            self.e3.delete(0, 'end')
            self.e4.delete(0, 'end')
            self.e5.delete(0, 'end')

    #updates the current list and places the values into the listboxes
    def listUpdate(self, title, subject, topic, date_set, date_due):
        #end is used so that the new values are placed at the end of the list instead of at the start
        self.t1.insert('end', title)
        self.t2.insert('end', subject)
        self.t3.insert('end', topic)
        self.t4.insert('end', date_set)
        self.t5.insert('end', date_due)

    #allows for the user to click one and highlight the other values in the row which helps to differentiate what values correspond with each other
    def select(self, title, subject, topic, date_set, date_due, val):
        self.t1.activate(val)
        self.t2.activate(val)
        self.t3.activate(val)
        self.t4.activate(val)
        self.t5.activate(val)

    #delete one assignment function
    def delOne(self, title, subject, topic, date_set, date_due):
        #try and except is used for the display error window
        try:
            conn = sql.connect('database.db')
            cur = conn.cursor()
            #val is what is used to identify and delete the row in both the listbox and in the database
            #val is the value of what the user's mouse clicks
            val = self.t1.curselection() or \
                self.t2.curselection() or \
                self.t3.curselection() or \
                self.t4.curselection() or \
                self.t5.curselection()
            #selects the other options in the row/from the same assignment
            self.select(title, subject, topic, date_set, date_due, val)
            #deletes them from the database using the primary key value of the row hence the val[0] + 1 as primary key starts from 1 not 0
            cur.execute(
                'delete from assignments where primary_key = ?',
                [val[0] + 1]
                )
            #saves database
            conn.commit()
            #deletes from the listbox (visually)
            self.t1.delete(val)
            self.t2.delete(val)
            self.t3.delete(val)
            self.t4.delete(val)
            self.t5.delete(val)
        except:
            #popup message for the error
            messagebox.showinfo('Cannot Delete', 'No assignment Item Selected')

    #delete all function
    def delAll(self):
        #message box asking if the user is sure
        mb = messagebox.askyesno('Delete All', 'Are you sure?')
        #if no is clicked then the message box is just closed hence no need for an elif or else
        if mb is True:
            #deletes everything
            cur.execute('delete from assignments')
            #saves database
            conn.commit()
            #deletes everything in each of the listboxes
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            self.t3.delete(0, 'end')
            self.t4.delete(0, 'end')
            self.t5.delete(0, 'end')

    #closes program
    def bye(self):
        #destroys window
        self.destroy()

    #when the program is opened this function displays the saved values from the database (if nothing is in databases then nothing is displayed)
    def retrieveDB(self):
        #selects all the database
        get_all = "SELECT * FROM assignments"
        databaselist = cur.execute(get_all).fetchall()
        for parameters in databaselist:
            #places them into their corresponding lists
            self.t1.insert('end', parameters[1])
            self.t2.insert('end', parameters[2])
            self.t3.insert('end', parameters[3])
            self.t4.insert('end', parameters[4])
            self.t5.insert('end', parameters[5])

#calls the class on start
root = MainApp()

#defines and creates the database sql
conn = sql.connect('database.db')
cur = conn.cursor()
#outlines the database table
cur.execute('create table if not exists assignments(primary_key integer PRIMARY KEY, \
title text, subject text, topic text, date_set text, date_due text)')

#runs the retrieve function so that when the program is opened the values in the database are already displayed/saved
root.retrieveDB()

root.mainloop()

#saves database and closes it
conn.commit()
cur.close()
