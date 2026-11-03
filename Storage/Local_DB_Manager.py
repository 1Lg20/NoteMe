import sqlite3
import Config


# Check DB if has the correct table, in case create it
def DB_Check():
	connection=sqlite3.connect(Config.UserFolder+Config.UserNote)
	connection.execute("PRAGMA foreign_keys = 1")
	cursor=connection.cursor()

	cursor.execute(f"PRAGMA table_info('Group')")
	columns = cursor.fetchall()
	if not columns == Config.GroupTable:
		print("Create Table Group")
		cursor.execute(Config.GroupTableCreate)
		connection.commit()
		cursor.execute(Config.CreateDefGroup)
		connection.commit()
	else:
		print("Table Group OK")

	cursor.execute(f"PRAGMA table_info('Note')")
	columns = cursor.fetchall()
	if not columns == Config.NoteTable:
		print("Create Table Note")
		cursor.execute(Config.NoteTableCreate)
		connection.commit()
	else:
		print("Table Note OK")

	connection.close()