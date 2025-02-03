from django.shortcuts import render
from .models import register
# Create your views here.
def start(request): 
    return render(request, "start.html")
def game(request):
    return render(request, "game.html")
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def contact(request):
    return render(request, "contact.html")

def reg(request):
    return render(request, "register.html")

def adminlayout(request):
    return render (request,"adminlayout.html")

def viewusers(request):
    return render (request,"viewusers.html")

def insert(request):
    fullname=request.GET['fullname']
    email=request.GET['email']
    password=request.GET['password']
    address=request.GET['address']
    
    r=register()
    r.fullname=fullname
    r.email=email
    r.password=password
    r.address=address
    r.save()
    return render(request, "register.html",{"msg":"registration successful"})
def logincheck(request):
    email1=request.GET['email']
    password1=request.GET['password']
    r=None
    try:
        r=register.objects.get(email=email1,password=password1)
        print("r=",r)
    except Exception as ex:
        print(ex)
        return render(request, "login.html",{"msg":"loginsucessfull"})
    return render(request,"game.html")
