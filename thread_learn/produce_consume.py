import threading
import time

lock = threading.Lock()
num = 0
class producer(threading.Thread):
	def run(self):
		global num
		while 1:
				time.sleep(10)
				num += 10
				print(10, 'made')
				print(num, 'total')

class consumer(threading.Thread):
	def run(self):
		global num
		while 1:
				import random
				sold = random.randint(1,5)
				if num >= sold:
						num -= sold
						print(sold, 'sold')
				time.sleep(3)
				print(num, 'left')

producer().start()
time.sleep(1)
consumer().start()
		
