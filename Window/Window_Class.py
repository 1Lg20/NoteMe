from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton, QScrollArea
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from Storage import Local_DB_Manager
from Window import Style
from functools import partial

# Main Window class

class MainWindow(QMainWindow):
	def __init__(self, width, height):
		super().__init__()
		self.resize(width, height)
		self.setWindowTitle("NoteMe")
		self.setWindowIcon(QIcon('./Window/Image/Icon.png'))
		self.__Container=QWidget()
		self.__layout=QVBoxLayout()
		self.__layout.setSpacing(0)
		self.__layout.setContentsMargins(0, 0, 0, 0)
		self.__layout.setAlignment(Qt.AlignmentFlag.AlignTop)
		self.__Container.setLayout(self.__layout)
		self.__ScrollArea=QScrollArea()
		self.__ScrollArea.setWidgetResizable(True)
		self.__ScrollArea.setWidget(self.__Container)
		self.setCentralWidget(self.__ScrollArea)
		self.__righe=[]
		self.__GetNote()

	def __GetNote(self):
		Group=Local_DB_Manager.DB_GetGroup()
		#self.__righe.append
		for element in Group:
			Notes=Local_DB_Manager.DB_GetNotesFromGroup(element[0])
			print(Notes)
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
			self.__righe[id]["layout"]["main"].addWidget(self.__righe[id]["layout"]["title"])
			self.__righe[id]["layout"]["main"].addWidget(self.__righe[id]["layout"]["Notes"])
			self.__righe[id]["layout"]["title"].setLayout(self.__righe[id]["layout"]["titleLayout"])
			self.__righe[id]["layout"]["Notes"].setLayout(self.__righe[id]["layout"]["NotesLayout"])
			self.__righe[id]["layout"]["titleLayout"].addWidget(QLabel(element[1]))
			self.__righe[id]["layout"]["titleLayout"].setAlignment(Qt.AlignmentFlag.AlignCenter)
			self.__righe[id]["layout"]["NotesLayout"].setAlignment(Qt.AlignmentFlag.AlignCenter)
			self.__righe[id]["layout"]["title"].setFixedHeight(50)
			self.__righe[id]["layout"]["title"].setStyleSheet(Style.Grouptitle)
			self.__righe[id]["layout"]["Notes"].setFixedHeight(Style.NoteContainerHeight)

			for note in Notes:	
				Note=QPushButton(note[2])			
				Note.setStyleSheet(Style.NoteCard)
				#Note.setAlignment(Qt.AlignmentFlag.AlignCenter)
				Note.setFixedHeight(Style.NoteCardHeight)
				Note.setFixedWidth(Style.NoteCardWidth)
				Note.setCursor(Qt.CursorShape.PointingHandCursor)
				Note.clicked.connect(partial(self.__premuto, note[0]))
				self.__righe[id]["layout"]["NotesLayout"].addWidget(Note)
				
			self.__layout.addWidget(self.__righe[id]["widget"])

	def __premuto(self, numero):
		print(Local_DB_Manager.DB_GetNoteFromID(numero))