from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# se importa el formulario que quiero cargar
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
# Create your views here.
def indexMascota(request):
    return render(request, 'mascota/index.html');


def formulario_Mascota(request):
    print(request.method + "esta es prueba");
    if request.method == 'POST':
        
        form = MascotaForm(request.POST);

        if form.is_valid():
            form.save();

        return redirect('mascota:index');
    
    else:   
        form = MascotaForm();

    return render(request, 'mascota/mascota_form.html', {'form': form});

def mascotaList(request):
        
    mascota = Mascota.objects.all().order_by("-id");
    contexto = {'mascotas':mascota};
    return render(request, 'mascota/mascota_list.html', contexto);

def mascotaEdit(request, id_mascota):

    mascota = Mascota.objects.get(id=id_mascota)

    if request.method == "GET":
        form = MascotaForm(instance=mascota)
    
    else:
        form = MascotaForm(request.POST, instance=mascota);

        if form.is_valid():
            form.save();
        else:
            print( form.errors);

        return redirect("mascota:mascota_list");

    return render(request, "mascota/mascota_form.html", {"form":form})

def macostaDelete(request, id_mascota):
    print(id_mascota + 'pppppp');
    print(request);
    mascota = Mascota.objects.get(id=id_mascota);
    if request.method == "POST":
        
        mascota.delete();
        return redirect('mascota:mascota_list');
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota});

class mascotaListView(ListView):
    model = Mascota;
    template_name = 'mascota/mascotaListView.html'

class mascotaCreateView(CreateView):
    model = Mascota;
    form_class = MascotaForm;
    template_name = 'mascota/mascotaCreateView.html';
    success_url = reverse_lazy('mascota:mascota_list_view');

class mascotaEditView(UpdateView):
    model = Mascota;
    form_class = MascotaForm;
    template_name = 'mascota/mascota_form.html';
    success_url = reverse_lazy('mascota:mascota_list_view');

class mascotaDeleteView(DeleteView):
    model = Mascota;
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html';
    success_url = reverse_lazy('mascota:mascota_list_view');
