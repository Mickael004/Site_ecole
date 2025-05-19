from django.urls import path
from .views import *

urlpatterns = [
    
    path(r'login/',loginpage,name='loginpage'),
    path(r'login',connexion,name='connexion_page'),
    path(r'inscription/',registerpage,name='registerpage'),
    path(r"inscription",inscrire_membre,name="inscrire_membre"),
    path(r'login/',deconnexion,name='deconnexion')
]