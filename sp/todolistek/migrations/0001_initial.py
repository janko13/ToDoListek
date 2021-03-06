# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opravilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('O_ime', models.CharField(max_length=50)),
                ('O_kategorija', models.CharField(max_length=50)),
                ('O_casovna_zahtevnost', models.CharField(max_length=50)),
                ('O_opraviti_do', models.CharField(max_length=50)),
                ('O_pomembnost', models.CharField(max_length=50)),
                ('O_opis', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Uporabnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('U_ime', models.CharField(max_length=50)),
                ('U_email', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='opravilo',
            name='O_uporabnik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolistek.Uporabnik'),
        ),
    ]
