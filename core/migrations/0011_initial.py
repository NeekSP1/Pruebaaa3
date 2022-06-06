# Generated by Django 4.0.4 on 2022-06-05 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0010_delete_idc_remove_registro_id_remove_registroc_id_and_more'),
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
            name='IdC',
            fields=[
                ('idContacto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de contacto')),
                ('Nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroC',
            fields=[
                ('NombreP', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('Apellido', models.CharField(max_length=10, verbose_name='Apellido')),
                ('Email', models.CharField(max_length=20, verbose_name='E-mail')),
                ('Asunto', models.CharField(max_length=9, verbose_name='Asunto')),
                ('Asunto2', models.CharField(max_length=20, verbose_name='Asunto2')),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.id')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('NombreP', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('Edad', models.CharField(max_length=2, verbose_name='Edad')),
                ('Email', models.CharField(max_length=20, verbose_name='E-mail')),
                ('Telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('Contrasena', models.CharField(max_length=20, verbose_name='Contrasena')),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.id')),
            ],
        ),
    ]
