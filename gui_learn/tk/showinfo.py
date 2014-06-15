#coding=utf8
import Tkinter as tk
import tkMessageBox as mb


class App(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Root')
        self.root.geometry("500x500")
        self.frame = tk.Frame(self.root)
        #self.config_text()
        self.set_var()
        self.content.pack()
        self.button.pack()
        self.frame.pack()

    def config_text(self):
        self.content = tk.Label(self.frame, text="hello")
        self.button = tk.Button(self.frame, text='Show', command=self.change)

    def set_var(self):
        self.var = tk.StringVar(value="hello")
        self.content = tk.Label(self.frame, textvariable=self.var)
        self.button = tk.Button(self.frame, text='Show', command=self.var_change)

    def change(self):
        # not change immediately
        self.content.config(text="world")
        #self.content.pack()  # no help
        mb.showinfo("Title", "Hi", parent=None)
        self.content.config(text="hello")

    def var_change(self):
        self.var.set("world")
        mb.showinfo("Title", "Hi", parent=None)
        self.var.set("hello")


def main():
    app = App()
    app.root.mainloop()

if __name__ == '__main__':
    main()
