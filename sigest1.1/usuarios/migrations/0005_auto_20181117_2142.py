# Generated by Django 2.1.3 on 2018-11-18 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
    ]