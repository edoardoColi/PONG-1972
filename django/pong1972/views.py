from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def pong_page(request):
    return render(request, "pong1972/home.html")
