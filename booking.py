import mysql.connector
import json
from datetime import datetime

def add_user(fname,lname,email,password,username,productId):
    db = mysql.connector.connect(
                host='bkswbs4odw5c3n23xb77-mysql.services.clever-cloud.com',
                username='ucvuplrivukdot0v',
                password='2yEAa5V6jv16Bm1d6sq7',
                database='bkswbs4odw5c3n23xb77'
            ) 

    cur = db.cursor()
    number =1234567890
    # sql = "INSERT INTO sql6443052.User (fname, lname, email, password, username) VALUE ('"+fname+"','"+lname+"','"+email+"','"+password+"','"+username+"');"
    # sql = "SELECT * FROM User where email='test@test.com';"
    # sql = "SELECT * FROM Product WHERE type = 'r';"
    # sql = "SELECT * FROM Product where productId = '"+str(1)+"';"
    # now = datetime.now()
    # date = now.strftime("%Y-%m-%d")
    # sql = f"INSERT INTO Transaction (productId,date,length,type,amount,fname,lname,email,number) VALUE ({productId},'{date}',4,'r',3999,'{fname}','{lname}','{email}','{number}')"
    sql = "SELECT transactionId FROM Transaction ORDER BY transactionId DESC LIMIT 1;"
    cur.execute(sql)
    a = cur.fetchall()
    # a = [list(i) for i in a]
    #a = list(a[0])
    #images = json.loads(a[5])
    # images = json.loads(a[0][5])
    transactionId = list(a[0])[0]
    print(transactionId)
    #print(images)
    db.commit()

add_user('test','test','test@test.com','1234','test',1)