# Generated by Django 2.1.3 on 2018-11-19 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_orientador_supervisor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orientador',
            new_name='Advisor',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='is_orientador',
            new_name='is_advisor',
        ),
    ]