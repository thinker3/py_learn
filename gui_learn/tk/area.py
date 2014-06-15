#coding=utf8
from Tkinter import *


def App(object):
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(self.parent)
        self.text_area_meaning = Text(self.frame, height=10, width=50, backgroud='white')
        self.scrollbar = Scrollbar(self.text_area_meaning)
        self.text_area_meaning.configure(yscrollcommand=self.scrollbar.set)

        self.frame.pack()
        self.text_area_meaning.pack(side=LEFT)
        self.scrollbar.pack(side=RIGHT, fill=Y)

root = Tk()
app = App(root)
root.title('ROOT')
root.mainloop()
