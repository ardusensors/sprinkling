from datetime import datetime
import sqlite3
from dailytimer import dtimer

conn = sqlite3.connect('database.db')
c = conn.cursor()
id = ('1',)
c.execute('SELECT id, strftime("%H",`start`), strftime("%M",`start`), strftime("%H", `end`), strftime("%M", `end`), runonce, t1, t2 FROM relays')
#tmp = c.fetchone()
print 'current time:',datetime.now()
for row in c:
	print 'id:',row[0] , 'start:', row[1],':',row[2], 'end:', row[3], ':' , row[4]
	dtimer(row[1],row[2],row[3],row[4])
