# Generated by Django 2.1.3 on 2018-12-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(help_text='Defina seu nome completo, exemplo: Fulano da Silva', max_length=255, verbose_name='Nome completo'),
        ),
    ]