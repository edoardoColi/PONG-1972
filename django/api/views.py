from django.shortcuts import render
from django.http import HttpResponse

def deafultPage(request):
    return HttpResponse("Hello i'm a bee(API)")
