from Tkinter import Tk

class GUI():
    def __init__(self):
        self.root = Tk()
        self.show()

    def show(self):
        self.root.deiconify()
        #self.root.attributes('-topmost', 1)
        #self.root.attributes('-topmost', 0)
        self.root.after(2000, self.hide)

    def hide(self):
        self.root.iconify()
        self.root.after(2000, self.show)

if __name__ == '__main__':
    gui = GUI()
    gui.root.mainloop()
