from django.shortcuts import render, redirect
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
# panier frais
    # if 'panier' not in request.session:
    #     request.session['panier'] = []
    # cart = request.session["panier"]
    # donner = {
    #     "id_formation": form_id,
    #     "formation":formation.nom,
    #     "frais_formation":formation.frais_formation
    # }

    # if donner in cart:
    #     cart.append(donner)
    #     request.session.modified = True
    donner = {
        "id_formation": form_id,
        "formation":formation.nom,
        "frais_formation":formation.frais_formation
    }
    if 'panier' not in request.session:
        request.session['panier'] = []

    request.session['panier'].append(donner)
    request.session.modified = True

    return render(request,'formulaire_inscription.html',context)

def supprimerPanier(request,form_id):
    if 'panier' in request.session:
        panier = request.sessio['panier']
        for index, form in enumerate(panier):
            if form['id_formation'] == form_id:
                del panier[index]
                break
        request.session['panier'] = panier
    return redirect("payement_inscription")

def validation_inscription(request):
    if request.method == 'POST':
        nom =  request.POST.get('nom')
        prenom =  request.POST.get('prenom')
        adresse =  request.POST.get('adresse')
        dateN = request.POST.get('dateN')
        telephone =  request.POST.get('telephone')
        formation =  request.POST.get('formation')
        frais_formation = request.POST.get('frais_formation')
        date_Debut = request.POST.get('date_Debut')
        choix_non_payer = request.POST.get('choix_non_payer') == 'on'
        choix_payer = request.POST.get('choix_payer') == 'on'

        inscription = FormationInscrit(
            nom=nom,
            prenom=prenom,
            adresse=adresse,
            telephone=telephone,
            dateN=dateN,
            formation=formation,
            frais_formation=frais_formation,
            date_Debut = date_Debut,
            choix_non_payer = choix_non_payer,
            choix_payer = choix_payer
        )

        inscription.save()

        if choix_non_payer:
            return redirect("confirmation_inscription")
        if choix_payer:
            return redirect("payement_inscription")
        
    return render(request,'formulaire_inscription.html')

def payement_inscription(request):
    # formation = FormationInscrit.objects.get(id=form_id)
    # user = request.session.get('client')
    # context = {
    #     'formation_inscrit':formation,
    #     'user': user
    # }
    return render(request,'payement.html')


def confirmation_inscription(request):
    return render(request,'confirmation_inscription.html')

