import datetime

from django.db import models

from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Professore(models.Model):
    nome = models.CharField(max_length=40)
    cognome = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)


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
    tutor = models.ForeignKey(Professore, on_delete=models.DO_NOTHING)
    sede = models.CharField(max_length=254)
    durata = models.IntegerField()
    data_inizio = models.DateField('data inizio attività')
    data_fine = models.DateField('data fine attività')
    obiettivi = models.TextField()
    autocertificazione = models.FileField(upload_to='uploads/%Y/%m/%d/')
    stato = models.IntegerField(choices=STATI_POSSIBILI, default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

