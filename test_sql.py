import sqlite3

conn = sqlite3.connect("new_joiners.db")
cursor = conn.cursor()
cursor.execute (""" CREATE TABLE IF NOT EXISTS new_employees(id INTEGER PRIMARY KEY, name TEXT, department TEXT) """)
cursor.execute("INSERT INTO new_employees(name, department) VALUES ('John Doe', 'Engineering')")
conn.commit()

cursor.execute("select * from new_employees")
#print
for row in cursor.fetchall():
    print(row)
    
conn.close()