from time import sleep
from Tkinter import Tk

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close_handler)
        self.root.mainloop()

    def close_handler(self):
        self.root.iconify()
        self.root.after(100, self.root.deiconify())

if __name__ == '__main__':
    gui = GUI()
