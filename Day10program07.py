import sqlite3 as lite
con = lite.connect('mtica.db')

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE Cars(
        Id INT,Name TEXT,Price INT)''')
print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")

cur.execute("INSERT INTO Cars VALUES(3,'Skoda',29000)")
cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
cur.execute("INSERT INTO Cars VALUES(5,'Bently',350000)")
cur.execute("INSERT INTO Cars VALUES(6,'citroen',210000)")
cur.execute("INSERT INTO Cars VALUES(7,'Hummer',29000)")
con.commit()
print("values in table car inserted.")
