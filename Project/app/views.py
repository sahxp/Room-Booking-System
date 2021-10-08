from django.shortcuts import render, redirect
import pyautogui as pag

# Create your views here.
def login(request):
    if (request.method == 'POST'):
        pag.alert(text=request.POST['customer[email]']+' '+request.POST['customer[password]'], title="Request")
        email = request.POST.get("customer[email]")
        password = request.POST.get("customer[password]")
        user_id = 1
        username = 'test'
        return redirect(str(user_id)+'/'+username)
    
    return render(request,'login.html')

def signup(request):
    if (request.method == 'POST'):
        email = request.POST.get("customer[email]")
        password = request.POST.get("customer[email]")
    return render(request,'signup.html')

def home(request,userId, username):
    return render(request,'index.html')

def details(request,userId,username,productId):
    return render(request,'details.html')