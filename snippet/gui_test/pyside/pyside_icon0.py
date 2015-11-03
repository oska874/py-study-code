# -*- coding:utf-8 -*-
# Import required modules
import sys
from PySide.QtGui import QApplication, QWidget, QIcon,QLabel,QPushButton,QMessageBox,QDesktopWidget,QStyle
class SampleWindow(QWidget):
	""" Our main window class
	"""
	def __init__(self):
		""" Constructor Function
		"""
		QWidget.__init__(self)
		self.setWindowTitle("Icon Sample")
		self.center()
		#self.setGeometry(300, 300, 200, 150)

	def setIcon(self):
		""" Function to set Icon
		"""
		appIcon = QIcon('icon.png')
		self.setWindowIcon(appIcon)

	def setIconModes(self):
		myIcon1 = QIcon('icon.png')
		myLabel1 = QLabel('sample', self)
		pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
		myLabel1.setPixmap(pixmap1)
		myLabel1.setToolTip('active icon')

		myIcon2 = QIcon('icon.png')
		myLabel2 = QLabel('sample', self)
		pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
		myLabel2.setPixmap(pixmap2)
		myLabel2.move(50, 0)

		myIcon3 = QIcon('icon.png')
		myLabel3 = QLabel('sample', self)
		pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
		myLabel3.setPixmap(pixmap3)
		myLabel3.move(100, 0)

	def setButton(self):
		""" Function to add a quit button
		"""
		myButton = QPushButton('Quit', self)
		myButton.move(50, 100)
		myButton.clicked.connect(self.quitApp)

	def quitApp(self):
		""" Function to confirm a message from the user
		"""
		userInfo = QMessageBox.question(self, 'Confirmation',
			"This will quit the application. Do you want to Continue?",
			QMessageBox.Yes | QMessageBox.No)

		if userInfo == QMessageBox.Yes:
			myApp.quit()
		if userInfo == QMessageBox.No:
			pass

	def center(self):
		""" Function to center the application
		"""
		qRect = self.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		qRect.moveCenter(centerPoint)
		self.move(qRect.topLeft())

	def setAboutButton(self):
		""" Function to set About Button
		"""
		self.aboutButton = QPushButton("About Me", self)
		self.aboutButton.move(130, 100)
		self.aboutButton.clicked.connect(self.showAbout)
	def showAbout(self):
		""" Function to show About Box
		"""
		QMessageBox.about(self.aboutButton, "About MyWin",
		"PySide is a cross-platform tool for generating GUI Programs.")

	def setQtAboutButton(self):
		""" Function to set About Button
		"""
		self.aboutQtButton = QPushButton("About Qt", self)
		self.aboutQtButton.move(130, 130)
		self.aboutQtButton.clicked.connect(self.showQtAbout)
	def showQtAbout(self):
		""" Function to show About Box
		"""
		QMessageBox.aboutQt(self.aboutQtButton, "About PySide")


###########################
if __name__ == '__main__':
	# Exception Handling
	try:
		myApp = QApplication(sys.argv)
		myApp.setStyle("macintosh")
		myWindow = SampleWindow()
		myWindow.setIcon()
		myWindow.setIconModes()
		myWindow.setButton()
		myWindow.setAboutButton()
		myWindow.setQtAboutButton()
		myWindow.show()
		myApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name Error:", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print(sys.exc_info()[1])