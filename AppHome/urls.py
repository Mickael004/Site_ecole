from django.urls import path
from .views import*

urlpatterns = [
    path(r'',accueilpage,name='accueilpage'),
    path(r'detail_formation/<int:id>',aff_detail,name='detail_form'),
    path(r'topus/formation/',aff_tous,name='plus_formation'),
    
    path(r'apropos',apropospage,name='apropospage'),
    path(r'login',loginpage,name='loginpage'),
    path(r'inscription',registerpage,name='registerpage'),
]