from django.db import models

# Create your models here.
class Formation(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="static/images/")
    frais_formation = models.IntegerField(null=True,blank=True)
    duree = models.IntegerField()
    date_pub = models.DateField(auto_now_add=True)
    debut_formation = models.DateField(null=True,blank=True)
    nom_prof = models.CharField(max_length=200,null=True, blank=True)
    detail_programme = models.TextField()

    def __str__(self):
        return self.nom