from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForms(UserCreationForm):
    class Meta:
        model = User;
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ];
        labels = {
            'username': 'Nombre Usuario',
            'first_name' : 'Primer nombre',
            'last_name' : 'Segundo Nombre',
            'email' : 'Correo electronico'
        };