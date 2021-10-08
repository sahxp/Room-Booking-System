import mysql.connector

db = mysql.connector.connect(
            host='127.0.0.1',
            username='root',
            password='a1234',
            database='booking system'
        ) 

cur = db.cursor()

sql = "select * from user;"

cur.execute(sql)
a = cur.fetchall()
print(a)