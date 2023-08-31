from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
# from.forms import*
# Create your views here.


def index(request):
    Boo=Books.get_all_books();
    print(Books)
    return render(request, 'index.html',{'Books' : Boo})

def home(request):
    Boo=Books.get_all_books();
    return render(request,'home.html',{'Books' : Boo})

def signin(request):
    if request.method == 'GET':
       return render(request,'signin.html')
    else:
        postData = request.POST
        name= postData.get('a1')
        email= postData.get('a2')
        pwd= postData.get('a3')
#error msg
        model = user(name = name,
                    email = email, 
                    pwd = pwd,)
        error_msg = None
        if(not name):
            error_msg = "Name is required"
        elif(not email):
            error_msg="Email is Required"
        elif(not pwd):
            error_msg="Password is Required"
        elif len(pwd)<8:
            error_msg="Password must be at least 8 characters"
        # elif user.isExist(True) :
        #     error_msg = "User already exists"


    if not error_msg:
        model.register()
        return redirect('homepage')
    
    else:
        return render(request,'signin.html',{'error':error_msg})
# def sig(request):
#     u=user()
#     u.name=request.GET['a1']
#     u.email=request.GET['a2']
#     u.pwd=request.GET['a3']
#     u.save()
#     return redirect('home.html')

def login(request):
    return render(request,'login.html')

def log(request):
    a=request.GET['b1']
    b=request.GET['b2']
    if user.objects.filter(email=a,pwd=b):
        z=user.objects.get(email=a)
        return redirect('homepage',{'a':z})
    else:
        return render(request,'login.html')
    
def aboutus(request):
    return render(request,'aboutus.html')