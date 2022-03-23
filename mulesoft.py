import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE mulesoft")
mycursor.execute("CREATE DATABASE mulesoft")
mycursor.execute("USE mulesoft")
mycursor.execute("CREATE TABLE movies(name VARCHAR(255), "
                 "actor VARCHAR(255), "
                 "actress VARCHAR(255), "
                 "director VARCHAR(255), "
                 "year INT(4))")
sql = "INSERT INTO movies(name, actor, actress, director, year) VALUES (%s , %s, %s, %s, %s)"
val = [
  ('HIGHWAY', 'RANDEEP HOODA', 'ALIA BHATT', 'IMTIAZ ALI', 2014),
  ('RAAZI', 'VICKY KAUSHAL', 'ALIA BHATT', 'MEGHNA GULZAR', 2018),
  ('GOLD', 'AKSHAY KUMAR', 'ILEANA DCRUZ', 'DHARMENDRA SURESH DESAI', 2016),
  ('TALVAR', 'IRRFAN KHAN', 'KONKONA SEN SHARMA', 'MEGHNA GULZAR', 2015),
  ('PIKU', 'AMITABH BACCHAN', 'DEEPIKA PADUKONE', 'SHOOJIT SIRCAR', 2015),
  ('BAJIRAO MASTANI', 'RANVEER SINGH', 'DEEPIKA PADUKONE', 'SANJAY LEELA BHANSALI',2015)
]
mycursor.executemany(sql, val)

mycursor.execute("SELECT * FROM movies")

result = mycursor.fetchall()

for row in result:
    print(row)

print("")
mycursor.execute("SELECT * FROM movies WHERE actress = 'ALIA BHATT';")

result = mycursor.fetchall()

for row in result:
    print(row)
