from django.db import models
import datetime
class Books(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    class Meta:
        db_table = "books"
    def get_all_books():
       return Books.objects.all()
    
    def get_book_price():
       return Books.price
    
    @staticmethod
    def get_books_by_id(ids):
        return Books.objects.filter(id__in=ids)  
    
    @staticmethod
    def delet(ids):
     u=Books.objects.get(id=ids)
     return u.delete()
    
    def register(self):
     self.save()
# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)
    class Meta:
        db_table="user"
    def get_all_user():
       return user.objects.all()
    
    def register(self):
     self.save()
    
    @staticmethod
    def get_user_by_email(email):
      try:
        return user.objects.get(email=email)
      except:
         return False
      
    @staticmethod
    def get_user_by_id(ids):
        return user.objects.filter(id=ids)
      
    @staticmethod
    def isExist(self):
       if user.objects.filter(email=self.email):
        return True
       else:
        return False
       
class order(models.Model):
    Book = models.ForeignKey(Books , on_delete=models.CASCADE)
    customer = models.ForeignKey(user , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.today)
    status= models.BooleanField(default=False)
    class Meta:
        db_table="order"
    def placeorder(self):
       self.save()
    
    def get_all_orders():
       return order.objects.all()

    @staticmethod
    def get_orders_by_customer(user_id):
       return order\
              .objects\
               .filter(customer = user_id)\
                .order_by('date')
    

class admin1(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_pwd=models.CharField(max_length=50)
    class Meta:
        db_table="Admin"

    @staticmethod
    def get_admin_by_email(admin_email):
      try:
        return user.objects.get(admin_email=admin_email)
      except:
         return False
      

# class admin_book(models.Model):
#     def dele(request,id):
#         u=Books.objects.get(id=id)
#         u.delete()