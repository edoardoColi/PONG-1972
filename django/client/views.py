from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse

# Create your views here.
def redirect_to_account(request):
    if request.user.is_authenticated:
        return redirect('/user/'+request.user.username+'/')
    if request.method == "POST":
        form = RegisterForm(request. POST)
        if form.is_valid():
            form.save()
        return redirect('/user/login/')
    else:
        form = RegisterForm()
    return render(request, "client/register.html", {"form":form})

def user_page(request, name):
    return render(request, "client/userPage.html")
    # my_vars = {"name":name}       #qui ci posso mettere anche tutto un oggetto e me lo ritrovo accessibile nel http e posso usarlo direttamente li

    # html_response = """
    # <html>
    # <head><title>Home Page</title></head>
    # <body>
    # <h1>Ciao {name} - default</h1>
    # <a href="{% url 'logout' %}">Logout now</a>
    # </body>
    # </html>
    # """.format(**my_vars)

    # return HttpResponse(html_response)

def test_page(request):
    html_response = """
    <html>
    <head><title>Home Page</title></head>
    <body>
    <h1>Test - default</h1>
    </body>
    </html>
    """
    return HttpResponse(html_response)
