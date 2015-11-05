# -*- coding:utf-8 -*-

# Import necessary modules
import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.amtLabel = QLabel('Loan Amount')
		self.roiLabel = QLabel('Rate of Interest')
		self.yrsLabel = QLabel('No. of Years')
		self.emiLabel = QLabel('EMI per month')
		self.emiValue = QLCDNumber()
		self.emiValue.setSegmentStyle(QLCDNumber.Flat)
		self.emiValue.setFixedSize(QSize(130,30))
		self.emiValue.setDigitCount(8)

		self.amtText = QLineEdit('10000')
		self.roiSpin = QSpinBox()
		self.roiSpin.setMinimum(1)
		self.roiSpin.setMaximum(15)

		self.yrsSpin = QSpinBox()
		self.yrsSpin.setMinimum(1)
		self.yrsSpin.setMaximum(20)

		self.roiDial = QDial()
		self.roiDial.setNotchesVisible(True)
		self.roiDial.setMaximum(15)
		self.roiDial.setMinimum(1)
		self.roiDial.setValue(1)

		self.yrsSlide = QSlider(Qt.Horizontal)
		self.yrsSlide.setMaximum(20)
		self.yrsSlide.setMinimum(1)

		self.calculateButton = QPushButton('Calculate EMI')

		self.myGridLayout = QGridLayout()
		self.myGridLayout.addWidget(self.amtLabel, 0, 0)
		self.myGridLayout.addWidget(self.roiLabel, 1, 0)
		self.myGridLayout.addWidget(self.yrsLabel, 2, 0)
		self.myGridLayout.addWidget(self.amtText, 0, 1)
		self.myGridLayout.addWidget(self.roiSpin, 1, 1)
		self.myGridLayout.addWidget(self.yrsSpin, 2, 1)
		self.myGridLayout.addWidget(self.roiDial, 1, 2)
		self.myGridLayout.addWidget(self.yrsSlide, 2, 2)
		self.myGridLayout.addWidget(self.calculateButton, 3, 1)
		self.setLayout(self.myGridLayout)

		self.setWindowTitle("A simple EMI calculator")
		self.roiDial.valueChanged.connect(self.roiSpin.setValue)
		self.connect(self.roiSpin, SIGNAL("valueChanged(int)"), self.roiDial.setValue)
		
		self.yrsSlide.valueChanged.connect(self.yrsSpin.setValue)
		self.connect(self.yrsSpin, SIGNAL("valueChanged(int)"), self.yrsSlide, SLOT("setValue(int)"))
		self.connect(self.calculateButton, SIGNAL("clicked()"), self.showEMI)

	def showEMI(self):
		loanAmount = float(self.amtText.text())
		rateInterest = float(self.roiSpin.value()) / 12 / 100
		noMonths = int(self.yrsSpin.value() * 12)
		emi = (loanAmount * rateInterest) * ( ( ( (1 + rateInterest) ** noMonths ) / ( ( (1 + rateInterest) ** noMonths ) - 1) ))
		self.emiValue.display(emi)
		self.myGridLayout.addWidget(self.emiLabel, 4, 0)
		self.myGridLayout.addWidget(self.emiValue, 4, 2)

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