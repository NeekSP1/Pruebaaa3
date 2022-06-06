from django import forms
from django.forms import ModelForm
from .models import Registro
from .models import RegistroC


class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields =['NombreP', 'Edad', 'Email', 'Telefono','Contrasena']

class RegistroForm(ModelForm):
    class Meta:
        model = RegistroC
        fields =['NombreP', 'Apellido', 'Email', 'Asunto','Asunto2']