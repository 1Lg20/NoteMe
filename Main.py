import json
import platform
import Window.Window_Manager

def main():
	Settings=load_config()
	Window.Window_Manager.Create(Settings)

def load_config():
	Settings={}
	print(platform.system())
	with open("./DefConf.json") as config:
		Settings=json.load(config)
	return Settings

if __name__ == "__main__":
	main()