import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        QToolTip.setFont(QFont('Arial', 10))
        button = QPushButton('Drück', self)
        button.move(50,50)
        button.clicked.connect(self.clicked)
        self.show()

    def clicked(self):
        print('button gedrückt')


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())