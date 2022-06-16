from django.contrib import admin

# Register your models here.

from .models import Studente, Richiesta

admin.site.register(Studente)
admin.site.register(Richiesta)
