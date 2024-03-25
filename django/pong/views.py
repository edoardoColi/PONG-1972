from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def pongPage(request):
    html_response = """
    <html>
    <head><title>Home Page</title></head>
    <body>
    <h1>Gioco Pong - default</h1>
    </body>
    </html>
    """
    return HttpResponse(html_response)
