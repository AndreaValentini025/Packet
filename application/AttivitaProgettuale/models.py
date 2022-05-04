from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Professore(models.Model):
    nome = models.CharField(max_length=40)
    cognome = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.nome + ' ' + self.cognome


class Richiesta(models.Model):
    STATI_POSSIBILI = [
        (0, 'Richiesta non ancora visionata'),
        (1, 'Richiesta inviata al professore, in attesa della sua approvazione'),
        (2, 'Richiesta convalidata dal professore, in attesa della registrazione'),
        (3, 'Richiesta evasa correttamente'),
        (-1, 'Richiesta rifiutata')
    ]
    nome = models.CharField(max_length=40)
    cognome = models.CharField(max_length=40)
    codice_fiscale = models.CharField(max_length=16)
    matricola = models.CharField(max_length=6)
    tutor = models.ForeignKey(User.objects.filter(groups__name='Professore'), on_delete=models.DO_NOTHING)
    sede = models.CharField(max_length=254)
    durata = models.IntegerField()
    data_inizio = models.DateField('data inizio attività')
    data_fine = models.DateField('data fine attività')
    obiettivi = models.TextField()
    autocertificazione = models.FileField(upload_to='uploads/%Y/%m/%d/')
    stato = models.IntegerField(choices=STATI_POSSIBILI, default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, default=timezone.now()-datetime.timedelta(minutes=10))
