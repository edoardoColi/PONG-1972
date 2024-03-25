from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_game, name='redirect_to_game'),

    #sotto per test ho dei numeri per fare le prove
    path('user/<int:id>', views.user_page, name='user_page'), #qui vorrei che l'utente scrivesse user e venisse mandato in user/<codice univoco> della sua area utente, se non so chi e' devo autenticarlo, se chiede quella di un altro mostro
    path('games/pong', views.pong_game, name='pong_game'),
]
