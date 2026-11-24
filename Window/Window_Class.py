from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from Storage import Local_DB_Manager

# Main Window class

class MainWindow(QMainWindow):
	def __init__(self, width, height):
		super().__init__()
		self.resize(width, height)
		self.setWindowTitle("NoteMe")
		self.setWindowIcon(QIcon('./Window/Image/Icon.png'))
		self.__Container=QWidget()
		self.__layout=QVBoxLayout()
		self.__Container.setLayout(self.__layout)
		self.setCentralWidget(self.__Container)
		self.__righe=[]
		self.__GetNote()

	def __GetNote(self):
		Group=Local_DB_Manager.DB_GetGroup()
		#self.__righe.append
		for element in Group:
			Notes=Local_DB_Manager.DB_GetNote(element[0])
			self.__righe.append({
				"widget":QWidget(), 
				"layout":{
					"main":QVBoxLayout(),
					"title":QWidget(),
					"titleLayout":QVBoxLayout(),
					"Notes":QWidget(),
					"NotesLayout":QHBoxLayout(),
				} 
				})
			id=len(self.__righe)-1

			self.__righe[id]["widget"].setLayout(self.__righe[id]["layout"]["main"])
			self.__righe[id]["widget"].setStyleSheet("border: 2px solid red;")
			self.__righe[id]["layout"]["main"].addWidget(self.__righe[id]["layout"]["title"])
			self.__righe[id]["layout"]["main"].addWidget(self.__righe[id]["layout"]["Notes"])
			self.__righe[id]["layout"]["title"].setLayout(self.__righe[id]["layout"]["titleLayout"])
			self.__righe[id]["layout"]["Notes"].setLayout(self.__righe[id]["layout"]["NotesLayout"])
			self.__righe[id]["layout"]["titleLayout"].addWidget(QLabel(element[1]))
			self.__righe[id]["layout"]["titleLayout"].setAlignment(Qt.AlignmentFlag.AlignCenter)
			self.__righe[id]["layout"]["NotesLayout"].setAlignment(Qt.AlignmentFlag.AlignCenter)
			for note in Notes:				
				self.__righe[id]["layout"]["NotesLayout"].addWidget(QLabel(note[2]))
			self.__layout.addWidget(self.__righe[id]["widget"])
