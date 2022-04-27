# Generated by Django 4.0.4 on 2022-04-27 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AttivitaProgettuale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('cognome', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Richiesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('cognome', models.CharField(max_length=40)),
                ('codice_fiscale', models.CharField(max_length=16)),
                ('matricola', models.CharField(max_length=6)),
                ('sede', models.CharField(max_length=254)),
                ('durata', models.IntegerField()),
                ('data_inizio', models.DateField(verbose_name='data inizio attività')),
                ('data_fine', models.DateField(verbose_name='data fine attività')),
                ('obiettivi', models.TextField()),
                ('autocertificazione', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('stato', models.IntegerField(choices=[(0, 'Richiesta non ancora visionata'), (1, 'Richiesta inviata al professore, in attesa della sua approvazione'), (2, 'Richiesta convalidata dal professore, in attesa della registrazione'), (3, 'Richiesta evasa correttamente'), (-1, 'Richiesta rifiutata')], default=0, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AttivitaProgettuale.professore')),
            ],
        ),
    ]
