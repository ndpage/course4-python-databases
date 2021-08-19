import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor() # Cursor opens a record (similar to file handle)

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
 CREATE TABLE Counts (email TEXT, count INTEGER)
'''
)
