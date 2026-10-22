import sys
from PyQt6.QtWidgets import QApplication
import Window.Window_Class as Window_Class

def Create(Settings):
	app = QApplication(sys.argv)
	window=Window_Class.MainWindow(Settings["Width"], Settings["Height"])
	window.show()
	sys.exit(app.exec())