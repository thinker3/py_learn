import time
import threading

lock = threading.Lock()


class Myclass(threading.Thread):
    def __init__(self, name):
        super(Myclass, self).__init__()
        self.name = name

    def run(self):
        lock.acquire()
        for l in self.name:
            print(l)
            time.sleep(1)
        print()
        lock.release()


def ordered():
    t1 = Myclass('abcde')
    t2 = Myclass('12345')

    t1.start()
    t2.start()


if __name__ == '__main__':
    ordered()
