from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib import messages #TODO
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_page(request):
    if request.user.is_authenticated:
        # magari aggiungere un messaggio pop-up che dice che sei gia loggato con messages (importato)
        return redirect('/user/'+request.user.username+'/')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        # else:
        #     return render(request, "generics/register.html", {"form":form})
        # retrieves the URL associated with the view name
    else:
        form = CustomUserCreationForm()
    return render(request, "generics/register.html", {"form":form})

@csrf_protect    
def logout_user(request):
    # should be used POST but is used GET method (because logout() sends a GET)
    if request.method == 'GET':
        logout(request)
        return redirect('/')
    else:
        return render(request, "generics/problem.html")

@login_required(login_url='/login/')
def profile_page(request, name):
    if request.user.is_authenticated and name == request.user.username:
        my_vars = {"name":name} # can also put an entire object here and I find it accessible in http, using {}, and can use it directly there
        return render(request, "generics/my_personal.html", my_vars)
    else:
        my_vars = {"name":name, "client":request.user.username} # can also put an entire object here and I find it accessible in http, using {}, and can use it directly there
        return render(request, "generics/notmy_personal.html", my_vars)

def home_page(request):
    return render(request, "generics/home.html")

def games_page(request):
    return render(request, "generics/games.html")

def error_page(request):
    return render(request, "generics/error.html")

def test_page(request):
    return render(request, "generics/test.html")
