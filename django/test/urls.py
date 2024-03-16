from django.urls import path, include
from .views import test1, test2, testError

# Qui abbiamo come viene diviso il "traffico" degli url che arrivano e smistiamo in base alla funzionalita che vogliamo

urlpatterns = [
    path('1', test1),
    path('2', test2),
    path('', testError),    #Qualsiasi cosa arriva che non matcha prima finisce qui
]