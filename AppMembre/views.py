from django.shortcuts import render,redirect
from .models import Membres
import re #regex
from datetime import datetime
import hashlib

# Create your views here.
def loginpage(request):
    return render(request,'login.html')

def registerpage(request):
    return render(request,'register.html')

def mdp_crypter(password):
    #Hachage 
    mdp = hashlib.sha384()
    mdp.update(password.encode('utf-8'))
    return mdp.hexdigest()

def inserer_photo(request,nom):
    if request.FILES.get("photo"):
        image = request.FILES.get("photo")
        #Enregistrement avec nom unique
        with open(f"static/images/{nom}.jpg","wb") as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        return f"{nom}.jpg"

def inscrire_membre(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get("prenom")
        adresse = request.POST.get("adresse")
        telephone = request.POST.get("telephone")
        photo = request.FILES.get("photo")
        emails = request.POST.get("email")
        password = request.POST.get("password")
        confirm_pwd = request.POST.get("confirm_pwd")

        if nom and prenom and emails:
            if not Membres.objects.filter(email=emails).exists():
                if password==confirm_pwd:
                    if len(password)>= 8 and re.search(r'[A-Za-z]',password) and re.search(r'[0-9]',password):
                        aff = prenom
                        long_nom = len(nom)
                        dernier = f"{aff[:3]}_{long_nom}"
                        
                        inscrire = Membres(
                            nom=nom,
                            prenom = prenom,
                            adresse = adresse,
                            telephone = telephone,
                            photo = f"static/images/{inserer_photo(request,dernier)}" ,
                            email = emails,
                            date_inscription = datetime.now(),
                            password = mdp_crypter(password)
                            
                        )
                        inscrire.save()
                        #creation session

                        request.session['client'] = {
                            "id" : inscrire.id,
                            "nom" : inscrire.nom,
                            "prenom" : inscrire.prenom,
                            "email" : inscrire.email,
                            "photo" : inscrire.photo
                        }
                        return redirect("http://127.0.0.1:8000/")
                    else:
                       return render(request,'register.html',{'erreur':"Mots de passe doit inclure au moins 8 caractères et inclue les lettre et les  chiffre"}) 
                else:
                    return render(request,'register.html',{'erreur':"Mots de passe ne correspond pas"})
            else :
                return render(request,'register.html',{'erreur':"Email Deja une compte"})


        else:
            return render(request,'register.html',{'erreur':"Tous les champs sont obligatoire"})
        
def deconnection (request):
    request.session.clear()
    return render(request,"login.html")