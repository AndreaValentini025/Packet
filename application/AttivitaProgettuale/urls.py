from django.urls import path, include
from . import views

app_name = 'AttivitaProgettuale'
urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('inserimento/', views.modulo, name='modulo'),
    path('modulo/', views.RichiestaCreateView.as_view(), name='richiesta'),
    path('richiestaComp/', views.RichiestaDetailView.as_view(), name="richiestaComp"),
    path('success/', views.success, name='success'),
    path('archivio/', views.RichiestaListView.as_view(), name="archivio_richieste"),
    path('gestione/<int:pk>/', views.GestioneRichiestaView.as_view(), name='gestione'),
]
