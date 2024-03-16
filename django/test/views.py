from django.shortcuts import render
from django.http import HttpResponse

##
# Funzioni test
##
def test1(request):
    return HttpResponse("<h1>My Test 1</h1>")
def test2(request):
    return HttpResponse("<h1>My Test 2</h1>")
def testError(request):
    return HttpResponse("<h1>Error, not implemented test</h1>")
