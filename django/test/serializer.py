from rest_framework import serializers
from .models import TestingRoom

class TestingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingRoom
        fields = ('id','code','host','working','created_at','votes')        #id e' la primary key che identifica il modello(automaticamente create quando si inserisce un nuovo modello)

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingRoom
        fields = ('working', 'votes')
