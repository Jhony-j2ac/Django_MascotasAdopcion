from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from apps.usuario.forms import RegistroForms
# Create your views here.
class RegistroUsarios(CreateView):
    template_name = "usuarios/RegisterView.html";
    model = RegistroForms;
    form_class = RegistroForms;
    success_url = reverse_lazy('adopcion:SolicitudListView');
