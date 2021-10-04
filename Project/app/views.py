from django.shortcuts import render, redirect
import pyautogui as pag

# Create your views here.
def login(request):
    if (request.method == 'POST'):
        pag.alert(text=request.POST['email']+' '+request.POST['password'], title="Request")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_id = 1
        username = 'test'
        return redirect('/home/'+str(user_id)+'/'+username)
    
    return render(request,'index.html')

def home(request,userId, username):
    return render(request,'index.html')

def listing_stay(request):
    return render(request,'index.html')