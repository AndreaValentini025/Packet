from django.contrib import admin

# Register your models here.

from .models import Professore, Richiesta

admin.site.register(Professore)
admin.site.register(Richiesta)
