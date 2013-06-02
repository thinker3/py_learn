import threading
import time

lock = threading.Lock()
class Myclass(threading.Thread):
	def __init__(self, name):
		super(Myclass, self).__init__()
		self.name = name
	
	def run(self):
		lock.acquire()
		for l in self.name:
			print l
			time.sleep(1)
		lock.release()


t1 = Myclass('abcde')
t2 = Myclass('12345')

t1.start()
t2.start()
