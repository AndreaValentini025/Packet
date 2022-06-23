from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import Group


class Studente(models.Model):
    CLASSI_LAUREA = [
        ('L', 'Laurea Triennale'),
        ('LM', 'Laurea Magistrale'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codice_fiscale = models.CharField(max_length=16)
    matricola = models.CharField(max_length=6)
    classe = models.CharField(max_length=2, choices=CLASSI_LAUREA)

    def __str__(self):
        return self.nome + ' ' + self.cognome


def get_first_and_last_name(self):
    return self.first_name + ' ' + self.last_name


User = get_user_model()
User.add_to_class("__str__", get_first_and_last_name)


class Richiesta(models.Model):
    STATI_POSSIBILI = [
        (0, 'Richiesta non ancora visionata'),
        (1, 'Richiesta approvata'),
    ]
    studente = models.ForeignKey('Studente', on_delete=models.DO_NOTHING)
    tutor = models.CharField(max_length=60)
    sede = models.CharField(max_length=254)
    durata = models.IntegerField()
    data_inizio = models.DateField('data inizio attività')
    data_fine = models.DateField('data fine attività')
    obiettivi = models.TextField()
    autocertificazione = models.BooleanField(default=False)
    stato = models.IntegerField(choices=STATI_POSSIBILI, default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
