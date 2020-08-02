import sys
from time import sleep
from PyQt4.QtCore import *
 
class A(QObject):
    def __init__(self):
        QObject.__init__(self)
 
    def afunc (self):
        self.emit(SIGNAL("go"))    
 
    def bfunc(self):
        print("Hello World!")
 
if __name__=="__main__":
    app=QCoreApplication(sys.argv)
    a=A()
    QObject.connect(a,SIGNAL("go"),a.bfunc)
    while 1:
        a.afunc()    
        sleep(1)
    sys.exit(app.exec_())
