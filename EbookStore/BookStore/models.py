from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    class Meta:
        db_table = "books"
    def get_all_books():
       return Books.objects.all()

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)
    class Meta:
        db_table="user"
    def register(self):
     self.save()
    
    def isExist(self):
       if user.objects.filter(email=self.email):
          return True

       return False