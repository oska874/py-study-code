# -*- coding:utf-8 -*-

import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyFileDialog(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		openFile = QAction(QIcon('open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showFileDialog)

		inputName = QAction(QIcon('open.png'), 'input name', self)
		inputName.setStatusTip('input name')
		inputName.triggered.connect(self.showNameDialog)

		inputAge = QAction(QIcon('open.png'), 'input age', self)
		inputAge.setStatusTip('input age')
		inputAge.triggered.connect(self.showAgeDialog)

		choiceW= QAction(QIcon('open.png'), 'input age', self)
		choiceW.setStatusTip('choice')
		choiceW.triggered.connect(self.showChoiceDialog)

		printerDiag = QAction(QIcon('open.png'), 'input age', self)
		printerDiag.setStatusTip('print')
		printerDiag.triggered.connect(self.printDoc)

		findDiag = QAction(QIcon('open.png'), 'find', self)
		findDiag.setStatusTip('find')
		findDiag.triggered.connect(self.findDialog)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile) 
		
		inputbar = menubar.addMenu("input")
		inputbar.addAction(inputName) 
		inputbar.addAction(inputAge) 
		inputbar.addAction(choiceW) 

		editbar = self.menuBar()
		findMenu = editbar.addMenu("find")
		findMenu.addAction(findDiag)

		printBar = menubar.addMenu("print")
		printBar.addAction(printerDiag)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Example - File Dialog')
		self.show()

	def showFileDialog(self):
		fileDialog = QFileDialog(self)
		fileDialog.setFileMode(QFileDialog.AnyFile)
		fileDialog.setNameFilter("Text files(*.txt)")
		fileName, _ = fileDialog.getOpenFileName(self) #, "Open Text Files", "c:/", "Text files(*.txt)")
		if fileName != "":
			contents = open(fileName, 'r')
			with contents:
				data = contents.read()
				self.textEdit.setText(data)

	def showNameDialog(self):
		text, ok = QInputDialog.getText(self, 'Input Text Dialog','Enter your name:')
		if ok:
			print(str(text))
	def showAgeDialog(self):
		text, ok = QInputDialog.getInteger(self, 'Input Number Dialog','Enter your age:')
		if ok:
			print(str(text))

	def showChoiceDialog(self):
		strList = ['Ice Cream', 'Chocolates', 'Milk Shakes']
		text, ok = QInputDialog.getItem(self, 'Input Combo Dialog',
		'Enter your choice:', strList)
		if ok:
			print(str(text))

	def printDoc(self):
		document = QTextDocument("Sample Page")
		printer = QPrinter()
		myPrintDialog = QPrintDialog(printer, self)
		if myPrintDialog.exec_() != QDialog.Accepted:
			return
		document.print_(printer)

	def findDialog(self):
		myFindDialog = FindDialog()
		myFindDialog.exec_()

#self defined dialog
class FindDialog(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.findLabel = QLabel("Find &What:")
		self.lineEdit = QLineEdit()
		self.findLabel.setBuddy(self.lineEdit)
		self.caseCheckBox = QCheckBox("Match &Case")
		self.backwardCheckBox = QCheckBox("Search &Backward")
		self.findButton = QPushButton("&Find")
		self.findButton.setDefault(True)
		self.closeButton = QPushButton("Close")
		self.topLeftLayout = QHBoxLayout()
		self.topLeftLayout.addWidget(self.findLabel)
		self.topLeftLayout.addWidget(self.lineEdit)
		self.leftLayout = QVBoxLayout()
		self.leftLayout.addLayout(self.topLeftLayout)
		self.leftLayout.addWidget(self.caseCheckBox)
		self.leftLayout.addWidget(self.backwardCheckBox)
		self.rightLayout = QVBoxLayout()
		self.rightLayout.addWidget(self.findButton)
		self.rightLayout.addWidget(self.closeButton)
		self.rightLayout.addStretch()
		self.mainLayout = QHBoxLayout()
		self.mainLayout.addLayout(self.leftLayout)
		self.mainLayout.addLayout(self.rightLayout)
		self.findButton.clicked.connect(self.findText)
		self.setWindowTitle("Find")
		self.setLayout(self.mainLayout)
		self.show()
		
	def findText(self):
		mySearchText = self.lineEdit.text()
		if self.caseCheckBox.isChecked():
			caseSensitivity = Qt.CaseSensitive
		else:
			caseSensitivity = Qt.CaseInsensitive
		if self.backwardCheckBox.isChecked():
		#search functionality goes here...
			print("Backward Find ")
		else:
		#search functionality goes here...
			print("Forward Find")




if __name__ =='__main__':
	# Exception Handling
	try:
		myApp = QApplication(sys.argv)
		myDiag = MyFileDialog()
		myApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name Error:", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print(sys.exc_info()[1])