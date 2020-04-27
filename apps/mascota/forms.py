from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model= Mascota;

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna'
        ]

        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'apellido',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha rescate',
            'persona': 'Persona que adopta',
            'vacuna': 'Vacunas'
        }

        widgets = {
            'nombre': forms.TextInput(attrs= {'class': 'form-control'}),
            'sexo': forms.TextInput(attrs= {'class': 'form-control'}),
            'edad_aproximada': forms.NumberInput(attrs= {'class': 'form-control'}),
            'fecha_rescate': forms.DateTimeInput(), 
            'persona': forms.Select(attrs= {'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple()
        }
