import os
import Config
import json

def Load_Def_Conf():
	print("Load Default Conf")
	with open(Config.UserFolder+Config.UserPreference, "w") as config:
		json.dump(Config.Defconf, config, indent=4)

def load_config():
	Settings={}	
	if not os.path.exists(Config.UserFolder+Config.UserPreference):
		print("Conf File not found")
		Load_Def_Conf()
	
	with open(Config.UserFolder+Config.UserPreference, "r") as config:
			Settings=json.load(config)

	return Settings