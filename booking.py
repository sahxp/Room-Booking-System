import mysql.connector

def add_user(fname,lname,email,password,username):
    db = mysql.connector.connect(
                host='sql6.freemysqlhosting.net',
                username='sql6443052',
                password='8yCMcmme2d',
                database='sql6443052'
            ) 

    cur = db.cursor()

    sql = "INSERT INTO sql6443052.User (fname, lname, email, password, username) VALUE ('"+fname+"','"+lname+"','"+email+"','"+password+"','"+username+"');"
    #sql = "SELECT * FROM User;"
    cur.execute(sql)
    a = cur.fetchall()
    print(a)
    db.commit()

add_user('test','test','test@test.com','1234','test')