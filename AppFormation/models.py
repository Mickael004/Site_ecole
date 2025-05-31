from django.db import models
from AppHome.models import Formation

# Create your models here.
class FormationInscrit(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    dateN = models.DateField()
    formation = models.CharField(max_length=50)
    frais_formation = models.CharField(max_length=20)
    date_Debut = models.TextField()
    date_Inscription = models.DateTimeField(auto_now_add=True)
    choix_non_payer = models.BooleanField(default=False)
    choix_payer = models.BooleanField(default=False)
    def __str__(self):
        return self.nom