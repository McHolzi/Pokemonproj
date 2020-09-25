import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#class my_Button(QPushButton):
 #   def __init__(self,name):
  #      super().__init__()
   #     self.setText(name)

class Fenster(QWidget):
    a=False
    def __init__(self):
        super().__init__()
        self.a = False
        self.initMe()
    
    def uicomp(self):
        button = QPushButton('neu',self)
        button.move(100,100)
        button.show()
    def initMe(self):
        QToolTip.setFont(QFont('Arial', 10))
        self.setGeometry(50,50,500,500)
        button = QPushButton('Drück',self)
        button.move(50,50)
        button.clicked.connect(self.uicomp)
        label = QLabel('Ein Label...\nneue zeile',self)
        label.move(200,100)
        self.show()

   
    

app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())