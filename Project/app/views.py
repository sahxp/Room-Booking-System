from django.shortcuts import render
import pyautogui as pag

# Create your views here.
def login(request):
    if (request.method == 'POST'):
        pag.alert(text=request.POST['email']+' '+request.POST['password'], title="Request")
        email = request.POST.get("email")
        password = request.POST.get("password")
    
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')
