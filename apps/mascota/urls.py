from django.urls import path, re_path, include
from apps.mascota.views import indexMascota, formulario_Mascota, mascotaList, mascotaEdit, macostaDelete, mascotaEdit, mascotaListView, mascotaCreateView, mascotaEditView, mascotaDeleteView

urlpatterns = [
    path('', indexMascota, name='index'),
    path('mainForm', formulario_Mascota, name='mascota_crear'),
    path('Allpets', mascotaList, name='mascota_list'),
    re_path(r'^EditPets/(?P<id_mascota>[0-9]{1})/$', mascotaEdit, name='mascota_edit'),
    re_path(r'^DeletedPet/(?P<id_mascota>[0-9]{1})/$', macostaDelete, name='mascota_delete'),
    path('AllPetsView', mascotaListView.as_view(), name='mascota_list_view'),
    path('mainFormView', mascotaCreateView.as_view(), name='mascota_create_view'),
    re_path(r'^EditPetsView/(?P<pk>[0-9]{1})/$', mascotaEditView.as_view(), name='mascota_edit_view'),
    re_path(r'^DeletedPetView/(?P<pk>[0-9]{1})/$', mascotaDeleteView.as_view(), name='mascota_delete_view'),
]