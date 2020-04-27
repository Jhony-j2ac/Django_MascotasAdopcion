from django.urls import path, re_path, include
from apps.usuario.views import RegistroUsarios

urlpatterns = [
    path('Register', RegistroUsarios.as_view(), name="UserRegister")
];