# Generated by Django 2.2.4 on 2019-08-25 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('ci', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Nro. de documento')),
                ('expedido', models.CharField(max_length=15, verbose_name='Expedido de CI')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombre Completo')),
                ('apellido_paterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido Materno')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo actual')),
                ('area', models.CharField(max_length=100, verbose_name='Area organizacional actual')),
                ('nroip', models.CharField(max_length=15, unique=True, verbose_name='Ip asignado')),
                ('nrointerno', models.IntegerField(default=0, verbose_name='Nro. interno asignado')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_eliminacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]