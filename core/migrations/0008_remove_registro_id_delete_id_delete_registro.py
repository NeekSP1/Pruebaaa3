# Generated by Django 4.0.4 on 2022-06-05 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='Id',
        ),
        migrations.DeleteModel(
            name='Id',
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
    ]