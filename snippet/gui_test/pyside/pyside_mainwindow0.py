# -*- coding:utf-8 -*-
# Import required modules
import sys, time
from PySide.QtGui import QApplication, QMainWindow,QStatusBar,QLabel,QProgressBar,QTextEdit,QMenuBar,QKeySequence,QAction,QIcon,QMessageBox,QToolBar

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
		self.progressBar.hide()

	def SetupComponents(self):
		""" Setting the central widget
		"""
		#add textedit in central
		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.CreateActions()
		#add menubar 
		self.CreateMenus()
		#add action for each menu
		self.fileMenu.addAction(self.newAction)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.exitAction)
		self.editMenu.addAction(self.copyAction)
		self.fileMenu.addSeparator()
		self.editMenu.addAction(self.pasteAction)
		self.helpMenu.addAction(self.aboutAction)
		#add toolbar
		self.CreateToolBar()
		self.mainToolBar.addAction(self.newAction)
		self.mainToolBar.addSeparator()
		self.mainToolBar.addAction(self.copyAction)
		self.mainToolBar.addAction(self.pasteAction)

	# Slots called when the menu actions are triggered
	def newFile(self):
		self.textEdit.setText('')

	def exitFile(self):
		self.close()

	def aboutHelp(self):
		QMessageBox.about(self, "About Simple Text Editor",
		"This example demonstrates the use of Menu Bar")

	def CreateActions(self):
		""" Function to create actions for menus
		"""
		#function divided into two parts: built-in and new defined
		self.newAction = QAction( QIcon('new.png'), '&New', 
			self, shortcut=QKeySequence.New,
			statusTip="Create a New File",triggered=self.newFile)

		self.exitAction = QAction( QIcon('exit.png'), 'E&xit',
			self, shortcut="Ctrl+Q", statusTip="Exit the Application",
			triggered=self.exitFile)

		self.copyAction = QAction( QIcon('copy.png'), 'C&opy',
			self, shortcut="Ctrl+C", statusTip="Copy",
			triggered=self.textEdit.copy)

		self.pasteAction = QAction( QIcon('paste.png'), '&Paste',
			self, shortcut="Ctrl+V",statusTip="Paste",
			triggered=self.textEdit.paste)

		self.aboutAction = QAction( QIcon('about.png'), 'A&bout',
			self, statusTip="Displays info about text editor",
			triggered=self.aboutHelp)

	# Actual menu bar item creation
	def CreateMenus(self):
		""" Function to create actual menu bar
		"""
		self.fileMenu = self.menuBar().addMenu("&File")
		self.editMenu = self.menuBar().addMenu("&Edit")
		self.helpMenu = self.menuBar().addMenu("&Help")

	def CreateToolBar(self):
		""" Function to create tool bar
		"""
		self.mainToolBar = self.addToolBar('Main')


################
if __name__ == '__main__':
	# Exception Handling
	try:
		myApp = QApplication(sys.argv)
		mainWindow = MainWindow()
		mainWindow.CreateStatusBar()
		mainWindow.SetupComponents()
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