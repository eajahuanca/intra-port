# Generated by Django 2.2.4 on 2019-08-25 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0002_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='tipo',
            field=models.CharField(choices=[('BANNER', 'BANNER'), ('MODAL', 'MODAL')], default='BANNER', max_length=10, verbose_name='Tipo'),
        ),
    ]