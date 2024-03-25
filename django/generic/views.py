from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def redirect_to_game(request):
    return redirect('/games/pong')

def homePage(request):
    html_response = """
    <html>
    <head><title>Home Page</title></head>
    <body>
    <h1>Pagina home - default</h1>
    <p><a href="/games/">Play Games</a></p>
    <p><a href="/user/">User</a></p>
    </body>
    </html>
    """
    return HttpResponse(html_response)

def errorPage(request):
    html_response = """
    <html>
    <head><title>Error Page</title></head>
    <body>
    <h1>Pagina non trovata - default</h1>
    <p><a href="/">Back home</a></p>
    </body>
    </html>
    """
    return HttpResponse(html_response)

def gamesPage(request):
    html_response = """
    <html>
    <head><title>Games Page</title></head>
    <body>
    <h1>Pagina dai giochi - default</h1>
    <p><a href="/games/pong/">Play Pong</a></p>
    </body>
    </html>
    """
    return HttpResponse(html_response)
