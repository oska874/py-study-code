# -*- coding:utf-8 -*-

# Import necessary modules
import sys
from PySide.QtGui import *
from PySide.QtCore import *


#inherited from qapplication and rewrite the notify
class MyApplication(QApplication):
	def __init__(self, args):
		super(MyApplication, self).__init__(args)
		
	def notify(self, receiver, event):
		if (event.type() == QEvent.KeyPress):
			QMessageBox.information(None, "Received Key Release EVent", "You Pressed: "+ event.text())
		return super(MyApplication, self).notify(receiver, event)

# Our main widget class
class MyWidget(QWidget):
# Constructor function
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Reimplementing Events")
		self.setGeometry(300, 250, 300, 100)
		self.myLayout = QVBoxLayout()
		self.myLabel = QLabel("Press 'Esc' to close this App")
		self.infoLabel = QLabel()
		self.myLabel.setAlignment(Qt.AlignCenter)
		self.infoLabel.setAlignment(Qt.AlignCenter)
		self.myLayout.addWidget(self.myLabel)
		self.myLayout.addWidget(self.infoLabel)
		self.myLabel1 = QLabel("Text 1")
		self.myLineEdit1 = QLineEdit()
		self.myLabel2 = QLabel("Text 2")
		self.myLineEdit2 = QLineEdit()
		self.myLabel3 = QLabel("Text 3")
		self.myLineEdit3 = QLineEdit()
		self.myLayout.addWidget(self.myLabel1)
		self.myLayout.addWidget(self.myLineEdit1)
		self.myLayout.addWidget(self.myLabel2)
		self.myLayout.addWidget(self.myLineEdit2)
		self.myLayout.addWidget(self.myLabel3)
		self.myLayout.addWidget(self.myLineEdit3)
		self.setLayout(self.myLayout)
		self.installEventFilter(self)

		# Function reimplementing Key Press, Mouse Click and Resize Events
	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()
	def mouseDoubleClickEvent(self, event):
		self.close()

	def mouseSingleClickEvent(self, event):
		self.myLineEdit3.setText("11111")
		self.close()

	def resizeEvent(self, event):
		self.infoLabel.setText("Window Resized to QSize(%d, %d)" % (event.size().width(), event.size().height()))

	# Function reimplementing event() function
	def event(self, event):
		if event.type()== QEvent.KeyRelease and event.key()== Qt.Key_Tab:
			self.myLineEdit3.setFocus()
			return True
		return QWidget.event(self,event)

	def eventFilter(self, receiver, event):
		if(event.type() == QEvent.MouseButtonPress):
			QMessageBox.information(None,"Filtered Mouse Press Event!!",'Mouse Press Detected')
			return True
		return super(MyWidget,self).eventFilter(receiver, event)

	def notify(self, receiver, event):
		#if (event.type() == QEvent.KeyPress):
		#	QMessageBox.information(None, "Received Key Release EVent", "You Pressed: "+ event.text())
		if(event.type() == QEvent.MouseButtonPress):
			QMessageBox.information(None,"Filtered Mouse Press Event!!",'Mouse Press Detected1111')
		return super(MyApplication, self).notify(receiver, event)


if __name__ =='__main__':
	# Exception Handling
	try:
		myApp = MyApplication(sys.argv)
		myWidget = MyWidget()
		myWidget.show()
		myApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name Error:", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print(sys.exc_info()[1])