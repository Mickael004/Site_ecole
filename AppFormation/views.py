from django.shortcuts import render
from AppHome.models import Formation
from .models import *
# Create your views here.


def inscrire_formation(request,form_id):
    formation = Formation.objects.get(id=form_id)
    user = request.session.get('client')


    context = {
        'detail_formation':formation,
        'user': user
    }
    return render(request,'formulaire_inscription.html',context)

def validation_inscription(request):
    if request.method == 'POST':
        nom =  request.POST.get('nom')
        prenom =  request.POST.get('prenom')
        adresse =  request.POST.get('adresse')
        telephone =  request.POST.get('telephone')
        formation =  request.POST.get('formation')
        frais_formation = request.POST.get('frais_formation')
        date_debut = request.POST.get('date_debut')
        choix_non_paye = request.POST.get('choix_non_payer') == 'on'
        choix_paye = request.POST.get('choix_payer') == 'on'

        inscription = FormationInscrit(
            nom=nom,
            prenom=prenom,
            adresse=adresse,
            telephone=telephone,
            formation=formation,
            frais_formation=frais_formation,
            date_debut = date_debut,
            choix_non_paye = choix_non_paye,
            choix_paye = choix_paye
        )

        inscription.save()

        if choix_non_paye:

            return True
        if choix_paye:
            return True
