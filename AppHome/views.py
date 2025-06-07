from django.shortcuts import render
from .models import *
from django.db.models import Q # pour faire une recherche filtrer

# Create your views here.
def accueilpage(request):
    formation_tous = Formation.objects.all()
    formation = Formation.objects.order_by('-date_pub')[:3]#Affichage seulement les 3 premier le nouveaux

    forma_unique = set(form.nom for form in formation_tous) #Formation avec d esorina ny doublon
                        # for form in formation_tous:
                        #     form.nom
    context = {
        'formation': formation,
        'form_unique':forma_unique,
        'tous_formation':formation_tous
    }
    return render(request,'Accueil.html',context)



def aff_detail(request,form_id):
    formation = Formation.objects.get(id=form_id)
    context = {
        'detail_formation':formation
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

