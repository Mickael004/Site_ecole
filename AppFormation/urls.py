from django.urls import path
from .views import*

urlpatterns = [
    path(r'formation/<int:form_id>/',inscrire_formation,name="inscrire_formation"),
    path(r'formation/<int:form_id>',validation_inscription,name=validation_inscription)
]