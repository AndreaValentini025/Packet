from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'AttivitaProgettuale'
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='mylogin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inserimento/', views.modulo, name='modulo'),
    path('modulo/', views.RichiestaCreateView.as_view(), name='richiesta'),
    path('richiestaComp/', views.RichiestaDetailView.as_view(), name='richiestaComp'),
    path('success/', views.success, name='success'),
    path('archivio/', views.RichiestaListView.as_view(), name='archivio_richieste'),
    path('gestione/<int:pk>/', views.GestioneRichiestaView.as_view(), name='gestione'),
    path('update/<int:richiesta_id>/', views.update_state, name='update'),
    path('redirect/', views.next_page, name='redirect'),
    path('generate/', views.generate_pdf, name='generate'),
    path('<pk>/delete/', views.RichiestaDeleteView.as_view(), name='delete'),
    path('prova/', views.GestioneLoginView.as_view(), name="prova"),
    path('access/', views.access, name="access")
]
