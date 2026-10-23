UserFolder=""
UserPreference="/UserPreference.json"
UserNote="/Notes.db"

GroupTableCreate="CREATE TABLE 'Group' ( ID INTEGER PRIMARY KEY AUTOINCREMENT, GroupName TEXT NOT NULL )"
GroupTable=[(0, 'ID', 'INTEGER', 0, None, 1), (1, 'GroupName', 'TEXT', 1, None, 0)]
NoteTableCreate="CREATE TABLE 'Note' ( ID INTEGER PRIMARY KEY AUTOINCREMENT, Group_ID INTERGET NOT NULL, Title TEXT NOT NULL, Content TEXT NOT NULL )"
NoteTable=[(0, 'ID', 'INTEGER', 0, None, 1), (1, 'Group_ID', 'INTERGET', 1, None, 0), (2, 'Title', 'TEXT', 1, None, 0), (3, 'Content', 'TEXT', 1, None, 0)]

Defconf={
	"Width":1000,
	"Height":800,
	"Theme":"OS",
	"DefLocation":"Local"
}