from django.urls import path, include
from .views import test1, test2, testDefault, testError, TestingRoomViewA, TestingRoomViewB, CreateRoomView

# Qui abbiamo come viene diviso il "traffico" degli url che arrivano e smistiamo in base alla funzionalita che vogliamo

urlpatterns = [
    path('', testDefault),    #Qualsiasi cosa arriva che non matcha prima finisce qui
    path('1', test1),
    path('2', test2),
    path('viewCrea', TestingRoomViewA.as_view()),   #con questo posso mettere a mano tutti i parametri
    path('viewList', TestingRoomViewB.as_view()),
    path('create', CreateRoomView.as_view()),   #con questa sfrutto il tocken sessione nell'host
    path('<path:remainder>/', testError),
]
