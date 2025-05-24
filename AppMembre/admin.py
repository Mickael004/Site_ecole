from django.contrib import admin
from .models import*

# Register your models here.
class DashMembre(admin.ModelAdmin):
    list_display = ('nom','prenom','adresse','telephone','photo','email','date_inscription','password')
admin.site.register(Membres,DashMembre)