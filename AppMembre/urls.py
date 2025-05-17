from django.urls import path
from .views import *

urlpatterns = [
    
    path(r'login/',loginpage,name='loginpage'),
    path(r'inscription/',registerpage,name='registerpage'),
    path(r"inscription",inscrire_membre,name="inscrire_membre")
]