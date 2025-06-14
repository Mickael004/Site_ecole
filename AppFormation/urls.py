from django.urls import path
from .views import*

urlpatterns = [
    path(r'formation/<int:form_id>/',inscrire_formation,name="inscrire_formation"),
    path(r'formation',validation_inscription,name="validation_inscription"),
    path(r'formation/payement/',payement_inscription,name='payement_inscription'),
    path(r'formation/confirmation/',confirmation_inscription, name='confirmation_inscription'),
    path(r'formation/panier/<int:form_id>',supprimerPanier,name='supprimerPanier')
]