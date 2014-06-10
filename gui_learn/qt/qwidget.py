import sys
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

class GUI(QtGui.QWidget):
    app = QtGui.QApplication(sys.argv)

    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()
        self.app.exec_()

    def initUI(self):               
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setGeometry(300, 300, 450, 150)        
        self.setWindowTitle('Test')    
        self.button = QtGui.QPushButton("Hello World", self)
        self.button.clicked.connect(self.sayHello)
        self.button.show()
        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", 
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
            self.showMinimized()
            if self.windowState() != Qt.WindowMinimized:
                self.setWindowState(Qt.WindowActive)

    def sayHello(self):
        print 'Hello'


if __name__ == '__main__':
    GUI()
