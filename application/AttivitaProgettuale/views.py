import mimetypes
import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django import forms

from .models import Richiesta, Professore


def modulo(request):
    return render(request, 'AttivitaProgettuale/paginaProva.html')


class RichiestaCreateView(generic.CreateView):
    model = Richiesta
    fields = ['nome', 'cognome', 'codice_fiscale', 'matricola',
              'tutor', 'sede', 'durata', 'data_inizio', 'data_fine', 'obiettivi', 'autocertificazione']
    template_name = 'AttivitaProgettuale/richiesta_new_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(RichiestaCreateView, self).get_form(form_class)

        form.fields['data_fine'].widget.attrs.update({'class': 'datepicker'})
        form.fields['data_inizio'].widget.attrs.update({'class': 'datepicker'})
        return form

    def get_success_url(self):
        return reverse('AttivitaProgettuale:success')


def success(request):
    return render(request, 'AttivitaProgettuale/static_success.html')


class RichiestaListView(generic.ListView):
    model = Richiesta
    template_name = 'AttivitaProgettuale/lista_richieste.html'
    context_object_name = 'richieste_totali'

    def get_context_data(self, **kwargs):
        context = super(RichiestaListView, self).get_context_data(**kwargs)
        context['richieste_nv'] = Richiesta.objects.filter(stato__exact=0)
        context['richieste_ap'] = Richiesta.objects.filter(stato__exact=1)
        context['richieste_ar'] = Richiesta.objects.filter(stato__exact=2)
        return context


class GestioneRichiestaView(generic.DetailView):
    model = Richiesta
    template_name = 'AttivitaProgettuale/gestore_richieste.html'


'''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['path'] = self.object.autocertificazione.url.split('.')[0]
        return context
'''


class RichiestaDetailView(generic.DetailView):
    model = Richiesta
    template_name = 'AttivitaProgettuale/richiesta_compilata.html'
