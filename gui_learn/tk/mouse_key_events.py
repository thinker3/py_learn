#!/usr/bin/env python
# encoding: utf-8


import Tkinter as tk


def key(event):
    print "pressed", event.keycode, event.keysym
    print event.x, event.y  # point in the frame
    print event.x_root, event.y_root  # point in the screen
    print event.state, event.time
    print event.type, event.widget


def left_click(event):
    frame.focus_set()
    print "left clicked at", event.x, event.y


def right_click(event):
    frame.focus_set()
    print "right clicked at", event.x, event.y

root = tk.Tk()
width = height = 400
frame = tk.Frame(root, width=width, height=height)
frame.bind("<Key>", key)
frame.bind("<Button-1>", left_click)
#frame.bind("<Button-2>", right_click)  # not right
frame.bind("<Button-3>", right_click)
frame.pack()
root.mainloop()
