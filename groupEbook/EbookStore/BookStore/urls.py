from django.urls import path
from.import views
from .views import *
urlpatterns = [
    path('index',views.index , name='indexpage'),
    path('home', Home.as_view(),name='homepage'),
    path('signin',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('aboutus',views.aboutus),
    path('cart', Cart.as_view(),name='Cart'),
    path('check-out', Checkout.as_view(),name='Checkout'),
    path('order', Orders.as_view(),name='order'),
    path('del/<int:id>', views.dele),
    path('edit/<int:id>', views.edit),
    path('edcode/<int:id>', views.edcode),
    path('admin1',Admin1.as_view(),name="Admin_Page"),
    path('admin_login',Admin_login.as_view(),name="admin_login"),
    path('Customers',Customer.as_view(),name="Customers"),
    path('Add_Books',Add_Books.as_view(),name="Add_Books"),
    path('admin_order',Admin_order.as_view(),name="admin_order"),
    path('Addpage',Addpage.as_view(),name="Addpage"),

]
