#coding=utf8
from time import sleep
from Tkinter import Tk, Toplevel
import Tkinter

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title("Test")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry("550x250+%d+%d" % (screen_width/2-275, screen_height/2-125))
        self.root.protocol("WM_DELETE_WINDOW", self.close_handler)
        self.root.mainloop()

    def close_handler(self):
        self.root.iconify()
        self.root.call('wm', 'deiconify', '.')


if __name__ == '__main__':
    gui = GUI()
