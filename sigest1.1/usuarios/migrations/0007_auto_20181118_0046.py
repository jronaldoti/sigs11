# Generated by Django 2.1.3 on 2018-11-18 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20181117_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='aluno',
            new_name='user',
        ),
    ]