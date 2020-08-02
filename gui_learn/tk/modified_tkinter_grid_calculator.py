from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Label, Style
from tkinter.ttk import Entry


class Example(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)   
        self.initUI()
        
    def initUI(self):
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        
        for i in range(5):
            self.rowconfigure(i, pad=9)
            if i<4:
                self.columnconfigure(i, pad=3)
        
        matrix = {
                'Cls': [1, 0],
                'Back': [1, 1],
                'Close': [1, 3],
                '7': [2, 0],
                '8': [2, 1],
                '9': [2, 2],
                '/': [2, 3],
    
                '4': [3, 0],
                '5': [3, 1],
                '6': [3, 2],
                '*': [3, 3],
    
                '1': [4, 0],
                '2': [4, 1],
                '3': [4, 2],
                '-': [4, 3],
    
                '0': [5, 0],
                '.': [5, 1],
                '=': [5, 2],
                '+': [5, 3],
                }

        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        for k, v in list(matrix.items()):
            v.append(Button(self, text=k))
            v[2].grid(row=v[0], column=v[1])
        self.matrix = matrix
        self.pack(padx=5, pady=5)

def main():
    root = Tk()
    root.title("Calculator")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
