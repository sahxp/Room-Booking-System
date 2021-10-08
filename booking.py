import mysql.connector

db = mysql.connector.connect(
            host='127.0.0.1',
            username='root',
            password='',
            database='booking system'
        ) 

cur = db.cursor()

sql = "select * from user';"

cur.execute(sql)
a = cur.fetchall()
print(a)