import os
import Config
import json


# Load Default Conf
def Load_Def_Conf():
	print("Load Default Conf")
	with open(Config.UserFolder+Config.UserPreference, "w") as config:
		json.dump(Config.Defconf, config, indent=4)


# Check if conf exist ad load it, or call default Conf Loader
def load_config():
	Settings={}	
	if not os.path.exists(Config.UserFolder+Config.UserPreference):
		print("Conf File not found")
		Load_Def_Conf()
	
	with open(Config.UserFolder+Config.UserPreference, "r") as config:
			Settings=json.load(config)

	return Settings