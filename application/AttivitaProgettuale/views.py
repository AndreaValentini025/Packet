from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Richiesta, Professore


def init(request):
    return render(request, 'registration/login.html')


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
    template_name = 'AttivitaProgettuale/gestore_richieste_new.html'


class RichiestaDetailView(generic.DetailView):
    model = Richiesta
    template_name = 'AttivitaProgettuale/richiesta_compilata.html'


def update_state(request, richiesta_id):
    try:
        richiesta = get_object_or_404(Richiesta, pk=richiesta_id)
    except(AttributeError):
        return render(request, 'AttivitaProgettuale/gestore_richieste_new.html', {
            'rich': richiesta,
            'error_message': "Solito errore",
        })
    else:
        richiesta.stato += 1
        richiesta.save()
        return HttpResponseRedirect(reverse('AttivitaProgettuale:archivio_richieste'))
