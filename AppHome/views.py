from django.shortcuts import render

# Create your views here.
def accueilpage(request):
    return render(request,'Accueil.html')

def apropospage(request):
    return render(request,'Apropos.html')

def loginpage(request):
    return render(request,'login.html')

def registerpage(request):
    return render(request,'register.html')