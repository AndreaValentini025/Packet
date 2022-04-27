=====
AttivitaProgettuale
=====

AttivitaProgettuale è un'applicazione sviluppata da due studenti
di ingegneria informatica per la gestione semi automatizzata
delle richieste di attività progettuale presso
l'Università degli studi di Modena e Reggio Emilia.


Guida Rapida
-----------

1. Aggiungere "AttivitaProgettuale" al campo INSTALLED_APPS in setting come segue::

    INSTALLED_APPS = [
        ...
        'AttivitaProgettuale',
    ]

2. Includere la configurazione URL per AttivitaProgettuale in urls.py del proprio progetto come segue::

    path('AttivitaProgettuale/', include('AttivitaProgettuale.urls')),

3. Eseguire ``python manage.py migrate`` per creare i modelli di AttivitaProgettuale.

4. Avvia il server di sviluppo e visita http://127.0.0.1:8000/admin/
   per gestire le richieste.

5. Visita http://127.0.0.1:8000/AttivitaProgettuale/ per accedere all'app.
