import sys
import pyhk
 
def fun():
    print "Do something"

def exit():
    sys.exit()

 
hot = pyhk.pyhk()
 
# letters must be upper
#hot.addHotkey(['Ctrl', 'Alt', 'Z'], fun)
hot.addHotkey(['Ctrl', 'Lwin', 'Z'], fun)
hot.addHotkey(['Ctrl', 'Alt', 'Q'], exit)
 
hot.start()
