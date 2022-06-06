# Generated by Django 4.0.4 on 2022-06-05 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Id',
            fields=[
                ('idRegistro', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de registro')),
                ('Nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('NombreP', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('Edad', models.CharField(max_length=20, verbose_name='Edad')),
                ('Email', models.CharField(blank=True, max_length=20, null=True, verbose_name='E-mail')),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.id')),
            ],
        ),
    ]