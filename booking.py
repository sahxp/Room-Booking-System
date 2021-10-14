import mysql.connector
import json

def add_user(fname,lname,email,password,username):
    db = mysql.connector.connect(
                host='bkswbs4odw5c3n23xb77-mysql.services.clever-cloud.com',
                username='ucvuplrivukdot0v',
                password='2yEAa5V6jv16Bm1d6sq7',
                database='bkswbs4odw5c3n23xb77'
            ) 

    cur = db.cursor()

    # sql = "INSERT INTO sql6443052.User (fname, lname, email, password, username) VALUE ('"+fname+"','"+lname+"','"+email+"','"+password+"','"+username+"');"
    # sql = "SELECT * FROM User where email='test@test.com';"
    # sql = "SELECT * FROM Product WHERE type = 'r';"
    sql = "SELECT * FROM Product where productId = '"+str(1)+"';"
    cur.execute(sql)
    a = cur.fetchall()
    # a = [list(i) for i in a]
    a = list(a[0])
    images = json.loads(a[5])
    # images = json.loads(a[0][5])
    print(a)
    print(images)
    db.commit()

add_user('test','test','test@test.com','1234','test')