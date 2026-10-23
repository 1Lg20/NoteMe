import platform
import os
import Config
import Window.Window_Manager
from Storage import Conf_Loader
from Storage.Local_DB_Manager import DB_Check

def Folder_Check():
	OS=platform.system()
	if OS=="Linux":
		if not os.path.exists(Config.UserFolder):
			os.makedirs(Config.UserFolder, exist_ok=True)
	elif OS=="Windows":
		print("Todo")
	else:
		print("OS not recognize")
		exit()

def main():	
	Config.UserFolder=os.path.join(os.path.expanduser("~"), ".NoteMe")
	Folder_Check()
	Settings=Conf_Loader.load_config()
	DB_Check()
	Window.Window_Manager.Create(Settings)
	
if __name__ == "__main__":
	main()