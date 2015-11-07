# -*- coding:utf-8 -*-
import sys
from PySide.QtGui import *
from PySide.QtCore import *


class MyWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.dateEdit = QDateEdit()
		self.dateEdit.setAlignment(Qt.AlignCenter)
		self.dateEdit.setWindowTitle("My Sec Application")
		self.dateEdit.show()


if __name__ == '__main__':
	MyApp = QApplication(sys.argv)
	mw = MyWidget()
	MyApp.exec_()
	sys.exit()


