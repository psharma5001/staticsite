from django.shortcuts import render
from multiprocessing import AuthenticationError
from web.models import Website
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    ctx = {}
    return render(request,'index.html',ctx)

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        userName=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(userName,email, pass1)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        user=authenticate(username=userName, password=pass1)
        from django.contrib.auth import login
        login(request,user)

    return render(request, 'signup.html')
def login(request):
    if request.method=="POST":
        userName=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=userName, password=password)
        from django.contrib.auth import login
        login(request, user)
       # messages.success(request,"Login")
        return redirect('/')

    return render(request,'login.html')

def about(request):
    #ctx = {}
    return render(request,'about.html')

def elements(request):
    #ctx = {}
    return render(request,'elements.html')
    
    
def generic(request):
    #ctx = {}
    return render(request,'generic.html')