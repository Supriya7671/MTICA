import sqlite3
carData=[
   (1, 'Audi', 52642),
   (2, 'Mercedes', 57127),
   (3, 'Skoda', 99999),
   (4, 'Volvo', 29000),
   (5, 'Bently', 350000),
   (6, 'citroen', 210000),
   (7, 'Hummer', 29000)
   ]
con = sqlite3.connect('mtica.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE Cars(Id INT,Name TEXT ,Price INT)")
cur.executemany("INSERT INTO Cars VALUES(?,?,?)",carData)
con.commit()
con.close()
print("values inserted.")

