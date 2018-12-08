# Generated by Django 2.1.3 on 2018-12-04 06:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentePastoral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('appaterno', models.CharField(max_length=45)),
                ('edad', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('ubicacion', models.CharField(max_length=45)),
                ('img', models.CharField(default='i3.png', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('appaterno', models.CharField(max_length=45)),
                ('edad', models.CharField(max_length=45)),
                ('comunidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comunidad')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='fecha_evento')),
                ('descripcion', models.CharField(max_length=255)),
                ('comunidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comunidad')),
            ],
        ),
        migrations.CreateModel(
            name='MinistroComunion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('appaterno', models.CharField(max_length=45)),
                ('edad', models.CharField(max_length=45)),
                ('comunidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comunidad')),
            ],
        ),
        migrations.CreateModel(
            name='Sacramento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2018, 12, 4, 3, 1, 44, 619516))),
                ('estado', models.CharField(default='En Espera', max_length=45)),
                ('comunidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comunidad')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Sacramento'),
        ),
        migrations.AddField(
            model_name='evento',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Solicitud'),
        ),
        migrations.AddField(
            model_name='agentepastoral',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comunidad'),
        ),
        migrations.AddField(
            model_name='agentepastoral',
            name='sacramento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Sacramento'),
        ),
    ]