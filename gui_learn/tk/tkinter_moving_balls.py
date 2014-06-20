#!/usr/bin/env python
# encoding: utf-8

import threading
import Queue
import random
import math
import time
import Tkinter

random.seed(0)

class App:
    def __init__(self, queue, width=400, height=300):
        self.width, self.height = width, height
        self.canvas = Tkinter.Canvas(width=width, height=height, bg='black')
        self.canvas.pack(fill='none', expand=False)
        self._oid = []
        self.canvas.after(10, self.move)

        self.queue = queue
        self.canvas.after(50, self.check_queue)

    def check_queue(self):
        try:
            x, y, rad, outline = self.queue.get(block=False)
        except Queue.Empty:
            pass
        else:
            self.create_moving_ball(x, y, rad, outline)
        self.canvas.after(50, self.check_queue)

    def move(self):
        width, height = self.width, self.height
        for i, (oid, r, angle, speed, (x, y)) in enumerate(self._oid):
            sx, sy = speed
            dx = sx * math.cos(angle)
            dy = sy * math.sin(angle)
            if y + dy + r> height or y + dy - r < 0:
                sy = -sy
                self._oid[i][3] = (sx, sy)
            if x + dx + r > width or x + dx - r < 0:
                sx = -sx
                self._oid[i][3] = (sx, sy)
            nx, ny = x + dx, y + dy
            self._oid[i][-1] = (nx, ny)
            self.canvas.move(oid, dx, dy)
        self.canvas.update_idletasks()
        self.canvas.after(10, self.move)

    def create_moving_ball(self, x=100, y=100, rad=20, outline='white'):
        oid = self.canvas.create_oval(x - rad, y - rad, x + rad, y + rad,
                outline=outline)
        oid_angle = math.radians(random.randint(1, 360))
        oid_speed = random.randint(2, 5)
        self._oid.append([oid, rad, oid_angle, (oid_speed, oid_speed), (x, y)])

def queue_create(queue, running):
    while running:
        if random.random() < 1e-6:
            print "Create a new moving ball please"
            x, y = random.randint(100, 150), random.randint(100, 150)
            color = random.choice(['green', 'white', 'yellow', 'blue'])
            queue.put((x, y, random.randint(10, 30), color))
        time.sleep(0) # Effectively yield this thread.

root = Tkinter.Tk()
running = [True]

queue = Queue.Queue()

app = App(queue)
app.create_moving_ball()
app.canvas.bind('<Destroy>', lambda x: (running.pop(), x.widget.destroy()))

thread = threading.Thread(target=queue_create, args=(queue, running))
thread.start()

root.mainloop()
