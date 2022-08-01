from tkinter import *
from tkinter import messagebox

task_list = []

def newTask():
    global my_entry
    global lb
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter an assignment.")

def deleteTask():
    global lb
    lb.delete(ANCHOR)

def assignment():
    global my_entry
    global lb
    ws = Tk()
    ws.geometry('500x450+500+200')
    ws.title('Manage assignments')
    ws.config(bg='#5f6368')
    ws.resizable(width=False, height=False)

    frame = Frame(ws)
    frame.pack(pady=10)

    lb = Listbox(frame, width=25, height=8, font=('Times', 18), bd=0, fg='#464646', highlightthickness=0, selectbackground='#a6a6a6', activestyle="none")

    lb.pack(side=LEFT, fill=BOTH)

    for item in task_list:
        lb.insert(END, item)

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)

    my_entry = Entry(ws, font=('times', 24))

    my_entry.pack(pady=20)

    button_frame = Frame(ws)
    button_frame.pack(pady=20)

    addTask_btn = Button(button_frame, text='Add assignment', font=('times 14'), bg='#cfe2f3', padx=20, pady=10, command=newTask)
    addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    delTask_btn = Button(button_frame, text='Delete assignment', font=('times 14'), bg='#cfe2f3', padx=20, pady=10, command=deleteTask)

    delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    ws.mainloop()


window=Tk()
btn=Button(window, text="Add assignment", bg='#cfe2f3', command=assignment)
btn.place(x=100, y=100)
window.geometry("300x200+10+10")
window.title('Discord Classroom')
window.config(bg='#5f6368')
window.mainloop()
