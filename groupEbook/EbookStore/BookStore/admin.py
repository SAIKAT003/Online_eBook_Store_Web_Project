from django.contrib import admin
from .models import *

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name' ,'price' ]

class CUstomer(admin.ModelAdmin):
    list_display = ['name' ,'email' ]

admin.site.register(Books , AdminProduct)
admin.site.register(user )
admin.site.register(order)