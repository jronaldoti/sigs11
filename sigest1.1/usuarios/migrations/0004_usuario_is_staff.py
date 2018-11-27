# Generated by Django 2.1.3 on 2018-11-18 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_usuario_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designado para usuarios da equipe', verbose_name='Status de staff'),
        ),
    ]