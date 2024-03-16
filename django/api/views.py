from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("Hello i'm a bee(API)")
