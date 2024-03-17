from django.db import models
import string
import random

# Un modello e', dato un database standard di colonne e tabelle per mantenere le informazioni, un'astrazione per averle in django.
# Invece di creare una tabella creiamo un modello, nel quale possiamo usace codice python per modificare informazioni piu facilmente

# Idealmente vogliamo views leggeri(poca logica) e models pesanti(molta logica)

def generate_unique_code():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase,k=8))
        if TestingRoom.objects.filter(code=code).count() == 0:
            break
    return code

class TestingRoom(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True) #unique significa al massimo un code per Room
    host = models.CharField(max_length=40, unique=True) #unique significa al massimo un host per Room
    working = models.BooleanField(null=False, default=False)
    votes = models.IntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # Possiamo anche aggiungere metodi in questa classe
    # def is_host(host)