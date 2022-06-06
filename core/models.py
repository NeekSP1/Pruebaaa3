from django.db import models

# Create your models here.

class   Id(models.Model):
    idRegistro = models.IntegerField(primary_key=True, verbose_name='Id de registro')
    Nombre = models.CharField(max_length=50, verbose_name='Nombre')

    def __int__(self):
        return self.idRegistro

# modelo para el vehiculo

class Registro(models.Model):
    NombreP = models.CharField(max_length=6, primary_key=True, verbose_name='Nombre')
    Edad = models.CharField(max_length=2, verbose_name='Edad')
    Email = models.CharField(max_length=20,  verbose_name='E-mail')
    Telefono = models.CharField(max_length=9, verbose_name='Telefono')
    Contrasena = models.CharField(max_length=20,  verbose_name='Contrasena')
    Id = models.ForeignKey(Id, on_delete=models.CASCADE)

    def __str__(self):
        return self.NombreP


class   IdC(models.Model):
    idContacto = models.IntegerField(primary_key=True, verbose_name='Id de contacto')
    Nombre = models.CharField(max_length=50, verbose_name='Nombre')

    def __int__(self):
        return self.idContacto


class RegistroC(models.Model):
    NombreP = models.CharField(max_length=10, primary_key=True, verbose_name='Nombre')
    Apellido = models.CharField(max_length=10, verbose_name='Apellido')
    Email = models.CharField(max_length=20,  verbose_name='E-mail')
    Asunto = models.CharField(max_length=9, verbose_name='Asunto')
    Asunto2 = models.CharField(max_length=20,  verbose_name='Asunto2')
    Id = models.ForeignKey(Id, on_delete=models.CASCADE)

    def __str__(self):
        return self.NombreP