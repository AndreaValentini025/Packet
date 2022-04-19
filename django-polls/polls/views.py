from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django import forms
import ipywidgets as widgets

from .models import Choice, Question, Richiesta, Professore


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions.
        (not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def modulo(request):
    return render(request, 'polls/paginaProva.html')


"""
class RichiestaForm(forms.ModelForm):
    class Meta:
        model = Richiesta
        fields = ['nome','cognome','codice_fiscale','matricola','tutor','sede',
                  'durata','data_inizio','data_fine','obiettivi','autocertificazione']
        widgets = {
            'data_inizio': widgets.DatePicker(
                            description='Data Inizio Attività',
                            disabled=False,
                            attrs={
                                'label_tag' : 'Data Inizio Attività',
                                'help_text' : ''
                            }

                        ),
            'data_fine': widgets.DatePicker(
                            description='Data Fine Attività',
                            disabled=False,
                            attrs={
                                'label_tag': 'Data Fine Attività',
                                'help_text': ''
                            }
                        )
        }


class RichiestaCreateView(generic.CreateView):
    form_class = RichiestaForm
    model = Richiesta
    template_name = 'polls/richiesta_new_form.html'


"""


class RichiestaCreateView(generic.CreateView):
    model = Richiesta
    fields = ['nome','cognome','codice_fiscale','matricola','tutor','sede','durata','data_inizio','data_fine','obiettivi','autocertificazione']
    template_name = 'polls/richiesta_new_form.html'

    def get_form(self, form_class):
        form = super(RichiestaCreateView, self).get_form(form_class)
        form.fields['data_fine'].widget.attrs.update({'class': 'datepicker'})
        form.fields['data_inizio'].widget.attrs.update({'class': 'datepicker'})
        return form

