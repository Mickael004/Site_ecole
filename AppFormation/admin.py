from django.contrib import admin
from .models import*

# Register your models here.
class DashFormationInscrit(admin.ModelAdmin):
    list_display=('nom','prenom','adresse','telephone','dateN','formation','frais_formation','date_Debut','date_Inscription','choix_non_payer','choix_payer')
admin.site.register(FormationInscrit,DashFormationInscrit)
