# -*- coding:utf-8 -*-
# Import required modules
import sys
from PySide.QtCore import QDateTime, QTimer, SIGNAL
from PySide.QtGui import QApplication, QWidget, QLCDNumber

class MyTimer(QWidget):
	""" Our Main Window class for Timer
	"""
	def __init__(self):
		""" Constructor Function
		"""
		QWidget.__init__(self)
		self.setWindowTitle('My Digital Clock')
		timer = QTimer(self)
		self.connect(timer, SIGNAL("timeout()"), self.updtTime)
		self.myTimeDisplay = QLCDNumber(self)
		self.myTimeDisplay.setSegmentStyle(QLCDNumber.Filled)
		self.myTimeDisplay.setDigitCount(8)
		self.myTimeDisplay.resize(500, 150)
		timer.start(1000)
		
	def updtTime(self):
		""" Function to update current time
		"""
		currentTime = QDateTime.currentDateTime().toString('hh:mm:ss')
		self.myTimeDisplay.display(currentTime)





######################################
# Main Function 
if __name__ == '__main__':
	# Exception Handling
	try: 
		myApp = QApplication(sys.argv)
		myWindow = MyTimer()
		myWindow.show()
		myApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name Error:", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print(sys.exc_info()[1])