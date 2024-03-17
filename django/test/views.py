from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics     #ci permette di creare classi che ereditano da una generica API view
from rest_framework import status     #ci permette l'accesso allo stato http quando mandiamo indietra la risposta
from .serializer import TestingRoomSerializer, CreateRoomSerializer
from .models import TestingRoom
from rest_framework.views  import APIView
from rest_framework.response  import Response

##
# Funzioni test e classi
##
def test1(request):
    return HttpResponse("<h1>My Test 1</h1>")

def test2(request):
    return HttpResponse("<h1>My Test 2</h1>")

def testDefault(request):
    return HttpResponse("<h1>Test home</h1>")

def testError(request, remainder):
    return HttpResponse(f"<h1>Test Error, no matching for -{remainder}-</h1>")

class TestingRoomViewA(generics.CreateAPIView):
    queryset = TestingRoom.objects.all()
    serializer_class = TestingRoomSerializer

class TestingRoomViewB(generics.ListAPIView):
    queryset = TestingRoom.objects.all()
    serializer_class = TestingRoomSerializer

# possiamo usare def per smistare le POST, GET,... al metodo corretto
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        #aggiungo la chiave di sessione di un utente
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()   #se non la ha allora la creo

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():       #per controllare i dati che mi sono stati mandati
            working = serializer.data.get('working')        #I dati che sono in serializer.py - CreateRoomSerializer
            votes = serializer.data.get('votes')
            host = self.request.session.session_key
            queryset = TestingRoom.objects.filter(host=host)
            if queryset.exists():   #ma se la persona che si collega ha gia una stanza non voglio una stanza nuova ma aggiornare la sua di stanza
                room = queryset[0]
                room.working = working
                room.votes = votes
                room.save(update_fields=['working', 'votes'])
                return Response(TestingRoomSerializer(room).data, status=status.HTTP_200_OK)
            else:       # se invece non ha una room
                room = TestingRoom(host=host, working=working, votes=votes)
                room.save()
                #volgliamo comunque ritornare una risposta alla request, quindi serializziamo la room appena creata
                return Response(TestingRoomSerializer(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
