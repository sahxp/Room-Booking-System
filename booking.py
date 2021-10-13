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
    sql = "SELECT * FROM Product WHERE type = 'r';"
    cur.execute(sql)
    a = cur.fetchall()
    a = [list(i) for i in a]
    for i in range(len(a)):    
        a[i].append(json.loads(a[i][5])[0])
    print(a)
    db.commit()

add_user('test','test','test@test.com','1234','test')