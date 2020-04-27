
from django import forms

from apps.adopcion.models import Persona, solicitud


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona;
        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio'
        ];

        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'edad': 'Edad',
            'telefono' : 'Telefono',
            'email' : 'Correo electronico',
            'domicilio' : 'Direccion'
        };

        widgets  = {
            'nombre' : forms.TextInput(attrs= {'class': 'form-control'}),
            'apellido' :  forms.TextInput(attrs= {'class': 'form-control'}),
            'edad' : forms.NumberInput(),
            'telefono' : forms.NumberInput(),
            'email' : forms.TextInput(),
            'domicilio' : forms.TextInput(attrs= {'class': 'form-control'})
        }
    

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = solicitud;

        fields = [
            'numero_mascotas',
            'razones'
        ];

        labels = {
            'numero_mascotas': 'numero_mascotas',
            'razones' : 'razones'
        };

        widgets: {
            'numero_mascotas' : forms.NumberInput(),
            'razones' : forms.TextInput(attrs= {'class': 'form-control'})
        }