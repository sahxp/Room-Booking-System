from django.shortcuts import render

# Create your views here.
def login(request):
    if (request.method == 'POST'):
        print(request)
    
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')
