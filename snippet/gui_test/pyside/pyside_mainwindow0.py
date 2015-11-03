# -*- coding:utf-8 -*-
# Import required modules
import sys, time
from PySide.QtGui import QApplication, QMainWindow,QStatusBar,QLabel,QProgressBar

class MainWindow(QMainWindow):
	""" Our Main Window Class
	"""
	def __init__(self):
		""" Constructor Fucntion
		"""
		QMainWindow.__init__(self)
		self.setWindowTitle("Main Window")
		self.setGeometry(300, 250, 400, 300)
		self.statusLabel = QLabel('Showing Progress')
		self.progressBar = QProgressBar()
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(100)

	def CreateStatusBar(self):
		""" Function to create Status Bar
		"""
		self.myStatusBar = QStatusBar()
		self.progressBar.setValue(10)
		self.myStatusBar.addWidget(self.statusLabel, 1)
		self.myStatusBar.addWidget(self.progressBar, 2)
		#self.myStatusBar.showMessage('Ready', 2000)
		self.setStatusBar(self.myStatusBar)

	def ShowProgress(self):
		""" Function to show progress
		"""
		while(self.progressBar.value() < self.progressBar.maximum()):
			self.progressBar.setValue(self.progressBar.value() + 10)
			time.sleep(1)
		self.statusLabel.setText('Ready')



################
if __name__ == '__main__':
	# Exception Handling
	try:
		myApp = QApplication(sys.argv)
		mainWindow = MainWindow()
		mainWindow.CreateStatusBar()
		mainWindow.show()
		mainWindow.ShowProgress()
		myApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name Error:", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print(sys.exc_info()[1])