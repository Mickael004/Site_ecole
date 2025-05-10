from django.urls import path
from .views import*

urlpatterns = [
    path(r'',accueilpage,name='accueilpage'),
    path(r'apropos',apropospage,name='apropospage'),
    path(r'login',loginpage,name='loginpage'),
    path(r'inscription',registerpage,name='registerpage'),
]