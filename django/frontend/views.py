from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def redirect_to_game(request):
    return redirect('/games/pong')

def user_page(response, id):
    my_vars = {"name":id}       #qui ci posso mettere anche tutto un oggetto e me lo ritrovo accessibile nel http e posso usarlo direttamente li
    return render(response,"frontend/userPage.html", my_vars)

def pong_game(response):
    return render(response,"frontend/gamePage.html", {})
