from django.urls import path
from.import views
urlpatterns = [
    path('index',views.index , name='indexpage'),
    path('home', views.home,name='homepage'),
    path('signin',views.signin),
    # path('sig',views.sig),
    path('login',views.login),
    path('log',views.log),
    path('aboutus',views.aboutus),
]
