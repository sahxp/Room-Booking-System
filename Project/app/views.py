from django.shortcuts import render, redirect
from django.contrib import messages
import mysql.connector
import pyautogui as pag

# Create your views here.
def login(request):
    if (request.method == 'POST'):
        email = request.POST.get("customer[email]")
        password = request.POST.get("customer[password]")
        if (email=="" or password ==""):
            print("Enter all Fields")
            messages.error(request,'Enter all Fields')
            return render(request,'login.html')
        else:
            db = mysql.connector.connect(
                    host='sql6.freemysqlhosting.net',
                    username='sql6443052',
                    password='8yCMcmme2d',
                    database='sql6443052'
                ) 
            cur = db.cursor()

            sql = "SELECT * FROM sql6443052.User WHERE email = '"+email+"';"

            cur.execute(sql)

            a = cur.fetchall()

            if (len(a) == 0):
                messages.error(request,"Email not registered")
            else:
                db_password = a[0][4]
                db_username = a[0][5]
                db_userId = a[0][0]
                if (db_password==password):
                    return redirect(str(db_userId)+'/'+str(db_username))
                else:
                    messages.error(request,"Incorrect Password")

        return render(request,'login.html')
    
    return render(request,'login.html')

def signup(request):
    if (request.method == 'POST'):
        email = request.POST.get("customer[email]")
        password = request.POST.get("customer[password]")
        fname = request.POST.get("customer[first_name]")
        lname = request.POST.get("customer[last_name]")
        username = request.POST.get("customer[user_name]")
        if (email=="" or password ==""or fname =="" or lname=="" or username==""):
            print("Enter all Fields")
            messages.error(request,'Enter all Fields')
            return render(request,'signup.html')
        else:
            db = mysql.connector.connect(
                    host='sql6.freemysqlhosting.net',
                    username='sql6443052',
                    password='8yCMcmme2d',
                    database='sql6443052'
                ) 

            cur = db.cursor()

            sql = "INSERT INTO sql6443052.User (fname, lname, email, password, username) VALUE ('"+fname+"','"+lname+"','"+email+"','"+password+"','"+username+"');"

            try:
                cur.execute(sql)
            except:
                messages.error(request,'Email or Username already registered')
                return render(request,'signup.html')

            db.commit()

            messages.success(request,'Added the user')

    return render(request,'signup.html')

def home(request,userId, username):
    return render(request,'index.html')

def details(request,userId,username,productId):
    return render(request,'details.html')