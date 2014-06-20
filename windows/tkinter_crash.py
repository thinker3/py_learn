#!/usr/bin/env python
# encoding: utf-8

import os
import time
import Queue
import threading
import Tkinter as tk

dirname = os.path.dirname(os.path.abspath(__file__))
word_path = os.path.join(dirname, 'word.txt')
sleep_interval = 0.05


class ReadWord(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.daemon = True  # needed

    def run(self):
        while 1:
            time.sleep(sleep_interval)
            self.read_word()

    def read_word(self):
        if os.path.exists(word_path):
            f = open(word_path, 'r')
            word = f.readline()
            f.close()
            os.popen('del %s' % word_path)
            if word:
                self.queue.put(word)


class App(object):
    def __init__(self, queue):
        self.queue = queue
        self.root = tk.Tk()
        self.root.geometry('100x100')
        self.frame = tk.Frame(self.root)
        self.message = tk.StringVar(value="hello")
        msg_label = tk.Label(self.frame, textvariable=self.message)
        msg_label.pack()
        self.frame.pack()
        self.frame.after(10, self.show_word)

    def show_word(self):
        if not self.queue.empty():
            word = self.queue.get()
            self.message.set(word)
            self.frame.update()
            self.root.deiconify()
            self.root.attributes('-topmost', 1)
            self.root.attributes('-topmost', 0)
            self.root.focus_force()
        self.frame.after(100, self.show_word)

queue = Queue.Queue()
ReadWord(queue).start()
App(queue).root.mainloop()
