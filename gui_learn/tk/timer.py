#coding=utf8
from Tkinter import *

def messageWindow() :
    win = Toplevel()

    b = Button(win, text='DING DING DING',
               bg="blue", fg="yellow",
               activebackground="red", activeforeground="white",
               padx=root.winfo_screenwidth()/2,
               pady=root.winfo_screenheight()/2,
               command=quit)
    b.pack()

    root.mainloop()

def show_alert():
    root.bell()
    messageWindow()
    quit()

def start_timer() :
    root.after(scale.get() * 1000, show_alert)

root = Tk()

minutes = Label(root, text="Minutes:")
minutes.grid(row=0, column=0)

scale = Scale(root, from_=1, to=45, orient=HORIZONTAL, length=300)
scale.grid(row=0, column=1)

button = Button(root, text="Start timer", command=start_timer)
button.grid(row=1, column=1, pady=5, sticky=E)

root.mainloop()
