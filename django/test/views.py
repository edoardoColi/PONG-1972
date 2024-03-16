from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics     #ci permette di creare classi che ereditano da una generica API view
from .serializer import TestingRoomSerializer
from .models import TestingRoom
 
##
# Funzioni test
##
def test1(request):
    return HttpResponse("<h1>My Test 1</h1>")
def test2(request):
    return HttpResponse("<h1>My Test 2</h1>")
def testError(request):
    return HttpResponse("<h1>Error, not implemented test</h1>")

class TestingRoomViewA(generics.CreateAPIView):
    queryset = TestingRoom.objects.all()
    serializer_class = TestingRoomSerializer

class TestingRoomViewB(generics.ListAPIView):
    queryset = TestingRoom.objects.all()
    serializer_class = TestingRoomSerializer
