import mysql.connector
from django.shortcuts import render, redirect
import pyautogui as pag

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        db = mysql.connector.connect(
            host='localhost',
            username='root',
            password='Decent@124',
            database='movierecommendation'
        ) 

        cur = db.cursor()

        sql = "select * from movierecommendation.users where users.email = '"+email+"';"

        cur.execute(sql)
        a = cur.fetchall()
        if len(a) ==0:
            pag.alert(text="Email Id Not registered")
            return redirect('/')
        user_id = a[0][0]
        db_pass = a[0][2]
        username = a[0][3]
        if db_pass == password:
            pag.alert("You are logged in!")
            return redirect('home/'+str(user_id)+'/'+username)
        else:
            pag.alert("Wrong Password!")

    return render(request, 'login.html')