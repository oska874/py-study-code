# -*- mode: python -*-
import sys, time
from PySide.QtGui import QApplication, QWidget,QMainWindow,QPushButton,QLabel,QLineEdit
from PySide.QtGui import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout

class MainWindow(QWidget):
	""" Our Main Window class
	"""
	def __init__(self):
		""" Constructor Function
		"""
		QWidget.__init__(self)
		self.setWindowTitle("Horizontal Layout")
		self.setGeometry(300, 250, 400, 300)
	def SetHLayout(self):
		""" Function to add buttons and set the layout
		"""
		horizontalLayout = QHBoxLayout(self)
		hButton1 = QPushButton('Button 1', self)
		hButton2 = QPushButton('Button 2', self)
		hButton3 = QPushButton('Button 3', self)
		hButton4 = QPushButton('Button 4', self)
		horizontalLayout.addWidget(hButton1)
		horizontalLayout.addWidget(hButton2)
		horizontalLayout.addWidget(hButton3)
		horizontalLayout.addWidget(hButton4)
		self.setLayout(horizontalLayout)

	def SetVLayout(self):
		verticalLayout = QVBoxLayout(self)
		vButton1 = QPushButton('Button 1', self)
		vButton2 = QPushButton('Button 2', self)
		vButton3 = QPushButton('Button 3', self)
		vButton4 = QPushButton('Button 4', self)
		verticalLayout.addWidget(vButton1)
		verticalLayout.addWidget(vButton2)
		verticalLayout.addStretch()
		verticalLayout.addWidget(vButton3)
		verticalLayout.addWidget(vButton4)
		self.setLayout(verticalLayout)

	def SetGLayout(self):
		gridLayout = QGridLayout(self)
		gButton1 = QPushButton('Button 1', self)
		gButton2 = QPushButton('Button 2', self)
		gButton3 = QPushButton('Button 3', self)
		gButton4 = QPushButton('Button 4', self)
		gButton5 = QPushButton('Button 5', self)
		gridLayout.addWidget(gButton1, 0, 0)
		gridLayout.addWidget(gButton2, 0, 1)
		gridLayout.addWidget(gButton3, 1, 0, 1, 2)
		gridLayout.addWidget(gButton4, 2, 0)
		gridLayout.addWidget(gButton5, 2, 1)
		self.setLayout(gridLayout)

	def SetFLayout(self):
		formLayout = QFormLayout(self)
		labelUsername = QLabel("Username")
		txtUsername = QLineEdit()
		labelPassword = QLabel("Password")
		txtPassword = QLineEdit()
		formLayout.addRow(labelUsername, txtUsername)
		formLayout.addRow(labelPassword, txtPassword)
		self.setLayout(formLayout)




if __name__ == '__main__':
	myapp = QApplication(sys.argv)
	mw = MainWindow()
	#mw.SetHLayout()
	#mw.SetVLayout()
	#mw.SetGLayout()
	mw.SetFLayout()
	mw.show()
	myapp.exec_()
