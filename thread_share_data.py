import threading
from time import sleep


answer = ''
class Dosomething(threading.Thread):
    def __init__(self):
        super(Dosomething, self).__init__()

    def forever(self):
        global answer
        while 1:
            if answer == 'q':
                break
            if answer:
                print answer
                answer = ''
            sleep(0.1)

    def run(self):
        self.forever()

def main():
    global answer
    t = Dosomething()
    t.start()
    while answer != 'q':
        answer = raw_input('>')
        sleep(0.2)


main()
