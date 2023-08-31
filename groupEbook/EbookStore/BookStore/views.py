from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
from .forms import *
# from.forms import*
# Create your views here.
def dele(request , id):
    u=Books.objects.get(id=id)
    u.delete()
    return redirect('../Add_Books#{{Books.id}}')

def edit(request , id):
    u= Books.objects.get(id=id)
    return render(request , 'edit.html',{'a':u})
def edcode(request , id):
    t=Books.objects.get(id=id)
    f=uform(request.GET, instance=t)
    if f.is_valid():
        f.save()
        return redirect('../Add_Books')
    return render( request, 'edit.html',{'a':t})

class Add_Books(View):
     def post(self,request):
        postData = request.POST
        B_name= postData.get('B_name')
        B_price= postData.get('B_price')
        B_Desc= postData.get('B_Desc')
        B_img= postData.get('B_img')
        #error msg
        model = Books(name = B_name,
                    price = B_price, 
                    description = B_Desc,
                    image = B_img,)
        model.register()
        return redirect('Add_Books')
     def get(self,request):
        Boo=Books.get_all_books()
        return render(request,'Add_Books.html',{'Books' : Boo})


class Home(View):
    def post(self,request):
        
        books=request.POST.get('books')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity = cart.get(books)
            if quantity:
                if remove:
                    cart[books]=quantity-1
                else:
                    cart[books]=quantity+1
            else:
                cart[books] = 1
        else:
            cart={}
            cart[books] = 1
        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect("/home")
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        print("you are:" ,request.session.get('email'))
        Boo=Books.get_all_books()
        return render(request,'home.html',{'Books' : Boo})
    
    
def index(request):
    Boo=Books.get_all_books()
    # print(Books)
    return render(request, 'index.html',{'Books' : Boo})  

class Signup(View):
    def get(self,request):
        return render(request,'signin.html')
    def post(self,request):
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
        #  elif user.isExist() :
        #     error_msg = "User already exists"


         if not error_msg:
            model.pwd=make_password(model.pwd)
            model.register()
            return redirect('/login')
    
         else:
            return render(request,'signin.html',{'error':error_msg})
         
         
class Login(View):
    def get(self,request):
          return render(request,'login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        model=user.get_user_by_email(email)
        error_message=None
        if model:
              flag=check_password(password,model.pwd)
              if flag:
                request.session['user']=model.id
                request.session['email']=model.email
                request.session.get('cart').clear()
                return redirect('homepage')
              else:
                error_message='Email or password invalid !!'
        else:
              error_message='Email or password invalid !!'
        return render(request,'login.html',{'error':error_message})
    
def aboutus(request):
    return render(request,'aboutus.html')

class Cart(View):
    def post(self,request):
        books=request.POST.get('books')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity = cart.get(books)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(books)
                    else:
                        cart[books]=quantity-1
                else:
                    cart[books]=quantity+1
            else:
                cart[books] = 1
        else:
            cart={}
            cart[books] = 1
        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect("/cart")
    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}

        ids=list(request.session.get('cart').keys())
        model=Books.get_books_by_id(ids)
        print(model)
        return render(request,'cart.html',{'books' : model})

class Checkout(View):
    def post(self,request):
        cart=request.session.get('cart')
        book=Books.get_books_by_id(list(cart.keys()))
        User=request.session.get('user')
        print(cart , book, User)
        for book in book:
            Order=order(Book=book,
                        customer=user(id=User),
                        quantity=cart.get(str(book.id)),
                        price=book.price)
            Order.save()
        request.session['cart']={}
        return redirect('/cart')
 
class Orders(View):
    def get(self,request):
        customer = request.session.get('user')
        orders=order.get_orders_by_customer(customer)
        return render(request ,'order.html', {'orders' : orders})  
    

class Admin1(View):
      def post(self,request):
        return redirect("/admin1")
    
      
      def get(self , request):
        return render(request,'admin1.html')
    
class Admin_login(View):
    def get(self,request):
          return render(request,'admin_login.html')
    def post(self,request):
        email = request.POST.get('admin_email')
        password = request.POST.get('admin_pwd')
        model=admin1.get_user_by_email(email)
        error_message=None
        if model:
              flag=check_password(password,model.pwd)
              if flag:
                request.session['admin']=model.id
                request.session['admin_email']=model.email
                return redirect('Admin_Page')
              else:
                error_message='Email or password invalid !!'
        else:
              error_message='Email or password invalid !!'
        return render(request,'admin_login.html',{'error':error_message})
    
class Customer(View):
    def get(self,request):
        customer=user.get_all_user()
        return render(request,'Customers.html',{'user' : customer})
      
class Admin_order(View):
    def get(self,request):
        orders=order.get_all_orders()
        return render(request ,'admin_order.html', {'orders' : orders})

class Addpage(View):
    def get(self,request):
        return render(request,'Addpage.html')
    
   