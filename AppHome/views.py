from django.shortcuts import render
from .models import *
from django.db.models import Q # pour faire une recherche filtrer

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

#recherche par nom
def rechercher(request):
    mots_recherhcer = request.GET.get("search","")
    donner = Formation.objects.filter(Q(nom__icontains=mots_recherhcer) | Q(nom_prof__icontains=mots_recherhcer)) if mots_recherhcer else Formation.objects.all() # Recherche par nom ou prof
    

    # if mots_recherhcer:
    #     donner = Formation.objects.filter(nom__icontains=mots_recherhcer)
    # else :
    #     donner = Formation.objects.all()

    if mots_recherhcer and not donner.exists():

        context ={
            'mots_rechercher' : mots_recherhcer,
            'erreur' : 'Aucune recherche trouvée'
        }
        return render(request,'tous_formation.html',context)
    else : 
        context ={
            'formation':donner,
            'mots_rechercher' : mots_recherhcer,
        }
        return render(request,'tous_formation.html',context)



def apropospage(request):
    return render(request,'Apropos.html')

def loginpage(request):
    return render(request,'login.html')

def registerpage(request):
    return render(request,'register.html')