import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(50,50, 500,500)
w.setAutoFillBackground(True)
w.setWindowTitle('HalliHallo')
w.show()
app.exec_()