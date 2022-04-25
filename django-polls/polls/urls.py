from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('inserimento/', views.modulo, name='modulo'),
    path('modulo/', views.RichiestaCreateView.as_view(), name='richiesta'),
    # path('datiInseriti/', views.createRichiesta, name='datiInseriti'),
    path('richiestaComp/', views.RichiestaDetailView.as_view(), name="richiestaComp"),
    path('success/', views.success, name='success'),
    path('archivio/', views.RichiestaListView.as_view(), name="archivio_richieste"),
    path('gestione/<int:pk>/', views.GestioneRichiestaView.as_view(), name='gestione'),
]
