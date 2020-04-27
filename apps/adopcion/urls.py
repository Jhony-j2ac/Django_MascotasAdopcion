from django.urls import path, re_path,  include
from apps.adopcion.views import index, Solicitud_ListView, Solicitud_CreateView, Solicitud_DeleteView, Solicitud_UpdateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(r"", index),
    path( "Solicitud_ListView", login_required(Solicitud_ListView.as_view()), name="SolicitudListView" ),
    path( "Solicitud_CreateView", login_required(Solicitud_CreateView.as_view()), name="SolicitudCreateView" ),
    re_path(r"^Solicitud_UpdateView/(?P<pk>[0-9]{1})$", login_required(Solicitud_UpdateView.as_view()), name="SolicitudUpdateView" ),
    re_path(r"^Solicitud_DeleteView/(?P<pk>[0-9]{1})$", login_required(Solicitud_DeleteView.as_view()), name="SolicitudDeleteView" )
]; 