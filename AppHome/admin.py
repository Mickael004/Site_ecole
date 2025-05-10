from django.contrib import admin
from .models import*

# Register your models here.
class DashFormation(admin.ModelAdmin):
    list_display=('nom','description','image','frais_formation','duree','date_pub','debut_formation','nom_prof','detail_programme')
admin.site.register(Formation,DashFormation)