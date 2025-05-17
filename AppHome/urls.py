from django.urls import path
from .views import*

urlpatterns = [
    path(r'',accueilpage,name='accueilpage'),
    path(r'detail_formation/<int:id>',aff_detail,name='detail_form'),
    path(r'topus/formation/',aff_tous,name='plus_formation'),
    path(r'search',rechercher,name='rechercher'),

    path(r'apropos',apropospage,name='apropospage'),
]