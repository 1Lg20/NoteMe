import sqlite3
import Config

def DB_Check():
	connection=sqlite3.connect(Config.UserFolder+Config.UserNote)
	
	cursor=connection.cursor()
	cursor.execute(f"PRAGMA table_info('Note')")
	columns = cursor.fetchall()
	if not columns == Config.NoteTable:
		print("Create Table Note")
		cursor.execute(Config.NoteTableCreate)
		connection.commit()
	else:
		print("Table Note OK")

	cursor.execute(f"PRAGMA table_info('Group')")
	columns = cursor.fetchall()
	if not columns == Config.GroupTable:
		print("Create Table Group")
		cursor.execute(Config.GroupTableCreate)
		connection.commit()
	else:
		print("Table Group OK")

	connection.close()