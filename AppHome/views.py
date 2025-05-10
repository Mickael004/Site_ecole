from django.shortcuts import render
from .models import *

# Create your views here.
def accueilpage(request):
    #formation = Formation.objects.all() [:3]#Afficher seulement les 3 premier formation
    formation = Formation.objects.order_by('-date_pub')[:3]#Affichage seulement les 3 premier le nouveaux
    context = {
        'formation': formation
    }
    return render(request,'Accueil.html',context)



def aff_detail(request,id):
    formation = Formation.objects.get(id=id)
    context = {
        'detail_fromation':formation
    }
    return render(request,'detail.html',context)
# def aff_tous(request):

def aff_tous(request):
    formation = Formation.objects.all()
    context = {
        'formation': formation
    }
    return render(request,'tous_formation.html',context)



def apropospage(request):
    return render(request,'Apropos.html')

def loginpage(request):
    return render(request,'login.html')

def registerpage(request):
    return render(request,'register.html')