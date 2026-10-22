from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
	def __init__(self, width, height):
		super().__init__()
		self.resize(width, height)
		self.setWindowTitle("NoteMe")
		self.setWindowIcon(QIcon('./Window/Image/Icon.png'))
