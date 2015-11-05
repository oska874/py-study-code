# -*- coding:utf-8 -*-

# Import necessary modules
import sys
from PySide.QtGui import *
from PySide.QtCore import *


class MyWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.myListWidget1 = QListWidget()
		self.myListWidget2 = QListWidget()
		self.myListWidget2.setViewMode(QListWidget.IconMode)
		#drag and drop
		self.myListWidget1.setAcceptDrops(True)
		self.myListWidget1.setDragEnabled(True)
		self.myListWidget2.setAcceptDrops(True)
		self.myListWidget2.setDragEnabled(True)
		
		self.setGeometry(300, 350, 500, 150)
		self.myLayout = QHBoxLayout()
		self.myLayout.addWidget(self.myListWidget1)
		self.myLayout.addWidget(self.myListWidget2)

		l1 = QListWidgetItem(QIcon('blue_bird.png'),"Angry Bird Blue")
		l2 = QListWidgetItem(QIcon('red_bird.png'),"Angry Bird Red")
		l3 = QListWidgetItem(QIcon('green_bird.png'),"Angry Bird Green")
		l4 = QListWidgetItem(QIcon('black_bird.png'),"Angry Bird Black")
		l5 = QListWidgetItem(QIcon('white_bird.png'),"Angry Bird White")

		self.myListWidget1.insertItem(1, l1)
		self.myListWidget1.insertItem(2, l2)
		self.myListWidget1.insertItem(3, l3)
		self.myListWidget1.insertItem(4, l4)
		self.myListWidget1.insertItem(5, l5)

		QListWidgetItem(QIcon('gray_pig.png'), "Grey Pig", self.myListWidget2)
		QListWidgetItem(QIcon('brown_pig.png'), "Brown Pig", self.myListWidget2)
		QListWidgetItem(QIcon('green_pig.png'), "Green Pig", self.myListWidget2)

		self.setWindowTitle('Drag and Drop Example');
		self.setLayout(self.myLayout)

if __name__ =='__main__':
	# Exception Handling
	try:
		myApp = QApplication(sys.argv)
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