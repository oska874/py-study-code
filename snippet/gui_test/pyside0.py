# Import the necessary modules required
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QLabel
# Main Function
if __name__ == '__main__':
	# Create the main application
	myApp = QApplication(sys.argv)
	# Create a Label and set its properties
	appLabel = QLabel()
	appLabel.setText("Hello, World!!!\n Look at my first app using PySide")
	appLabel.setAlignment(Qt.AlignCenter)
	appLabel.setWindowTitle("My First Application")
	appLabel.setGeometry(300, 300, 250, 175)
	# Show the Label
	appLabel.show()
	# Execute the Application and Exit
	myApp.exec_()
	#sys.exit()