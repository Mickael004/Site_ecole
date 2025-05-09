from django.urls import path
from .views import*

urlpattern = [
    path(r'',accueilpage,name='accueilpage')
]