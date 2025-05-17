from django.db import models

# Create your models here.
class Membres(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='static/images/')
    email = models.EmailField()
    date_inscription = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"