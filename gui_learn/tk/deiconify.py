import tkinter as tk


class GUI(object):
    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.button = tk.Button(self.frame, text='Minimize',
                command=self.close_handler)
        self.button.pack()
        self.frame.pack()

    def close_handler(self):
        self.root.iconify()
        self.root.after(600, self.show)

    def show(self):
        self.root.deiconify()
        #self.root.attributes('-topmost', 1)
        #self.root.attributes('-topmost', 0)


if __name__ == '__main__':
    gui = GUI()
    gui.root.mainloop()
