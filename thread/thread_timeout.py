import threading
from time import sleep


answer = ''
class Dosomething(threading.Thread):
    def __init__(self):
        super(Dosomething, self).__init__()

    def forever(self):
        global answer
        while 1:
            print 'sleeping...'
            sleep(1)
        answer = 'done'

    def limited(self, time=3):
        global answer
        while time > 0:
            print 'sleeping'
            sleep(1)
            time -= 1
        answer = 'done'

    def run(self):
        #self.limited()
        self.forever()

def main():
    print 'hello'
    t = Dosomething()
    #t.setDaemon(True)
    t.start()
    sleep(5)
    print t.is_alive()
    print answer
    print 'world'

main()
