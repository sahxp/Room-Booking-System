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
                    host='bkswbs4odw5c3n23xb77-mysql.services.clever-cloud.com',
                    username='ucvuplrivukdot0v',
                    password='2yEAa5V6jv16Bm1d6sq7',
                    database='bkswbs4odw5c3n23xb77'
                ) 
            cur = db.cursor()

            sql = "SELECT * FROM User WHERE email = '"+email+"';"

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
                    host='bkswbs4odw5c3n23xb77-mysql.services.clever-cloud.com',
                    username='ucvuplrivukdot0v',
                    password='2yEAa5V6jv16Bm1d6sq7',
                    database='bkswbs4odw5c3n23xb77'
                ) 

            cur = db.cursor()

            sql = "INSERT INTO User (fname, lname, email, password, username) VALUE ('"+fname+"','"+lname+"','"+email+"','"+password+"','"+username+"');"

            try:
                cur.execute(sql)
            except:
                messages.error(request,'Email or Username already registered')
                return render(request,'signup.html')

            db.commit()

            messages.success(request,'Added the user')

    return render(request,'signup.html')
    
def home(request,userId, username):

    return render(request,'index.html',context={'userId':userId,'username':username})

def rooms(request,userId, username):
    return render(request,'rooms.html',context={'userId':userId,'username':username})

def details(request,userId,username,productId):
    if (request.method == 'POST'):
        return redirect('/checkout/'+str(userId)+'/'+str(username)+'/'+str(productId)+'/')
    return render(request,'details.html',context={'userId':userId,'username':username,'productId':productId})

def checkout(request,userId,username,productId):
    return render(request,'checkout.html')

def subscription(request,userId, username):
    return render(request,'subscription.html')

def confirmation(request,userId,username,productId):
    return render(request,'confirmation.html')
