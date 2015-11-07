# -*- coding:utf-8 -*-
import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyDialog(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.fd = QWizard()
		self.fd.show()

if __name__ == '__main__':
	MyApp = QApplication(sys.argv)
	md = MyDialog()
	MyApp.exec_()
	sys.exit()