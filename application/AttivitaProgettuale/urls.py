from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'AttivitaProgettuale'
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/AttivitaProgettuale/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inserimento/', views.modulo, name='modulo'),
    path('modulo/', views.RichiestaCreateView.as_view(), name='richiesta'),
    path('richiestaComp/', views.RichiestaDetailView.as_view(), name='richiestaComp'),
    path('success/', views.success, name='success'),
    path('archivio/', views.RichiestaListView.as_view(), name='archivio_richieste'),
    path('gestione/<int:pk>/', views.GestioneRichiestaView.as_view(), name='gestione'),
]
