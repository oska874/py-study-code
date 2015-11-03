# -*- coding:utf-8 -*-

# Import required modules
import sys
import time
from PySide.QtGui import QApplication, QWidget

class SampleWindow(QWidget):
	""" Our main window class
	"""
	# Constructor function
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Sample Window")
		self.setGeometry(300, 300, 200, 150)
		self.setMinimumHeight(100)
		self.setMinimumWidth(250)
		self.setMaximumHeight(200)
		self.setMaximumWidth(800)
		
if __name__ == '__main__':
	# Exception Handling
	try:
		myApp = QApplication(sys.argv)
		myWindow = SampleWindow()
		myWindow.show()
		time.sleep(3)
		myWindow.resize(300, 300)
		myWindow.setWindowTitle("Sample Window Resized")
		myWindow.repaint()
		myApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name Error:", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print (sys.exc_info()[1])