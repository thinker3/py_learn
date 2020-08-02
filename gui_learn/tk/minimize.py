import tkinter as tk


class App(object):
    def __init__(self):
        self.root = tk.Tk()
        tk.Label(self.root, text="main window").pack()
        self.t = tk.Toplevel()
        tk.Label(self.t, text="tool window").pack()
        self.root.bind("<Unmap>", self.OnUnmap)
        self.root.bind("<Map>", self.OnMap)

    # not work on Ubuntu

    def OnMap(self, event):
        # show the tool window
        self.t.wm_deiconify()

    def OnUnmap(self, event):
        # withdraw the tool window
        self.t.wm_withdraw()

if __name__ == "__main__":
    app = App()
    app.root.mainloop()
