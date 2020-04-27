from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
from apps.adopcion.models import solicitud, Persona
from apps.adopcion.forms import SolicitudForm, PersonaForm
from django.urls import reverse_lazy

def index(request):
    return render(request, 'adopcion/index.html');


class Solicitud_ListView(ListView):

    model = solicitud; #Solicitud
    template_name = 'adopcion/adopcionList.html';
    
class Solicitud_CreateView(CreateView):

    model = solicitud; #Solicitud
    template_name = "adopcion/adopcionFormView.html"
    form_class =  SolicitudForm;
    second_form_class = PersonaForm;
    success_url = reverse_lazy("adopcion:SolicitudListView");

    def get_context_data(self, **kwargs):
        context = super(Solicitud_CreateView, self).get_context_data(**kwargs)

        if 'form'not in context:
            context['form'] = self.form_class(self.request.GET);
        
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)        
       
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST);
        form2 = self.second_form_class(request.POST);

        if form.is_valid() and form2.is_valid():
            
            solicitud = form.save(commit=False);
            solicitud.persona = form2.save();
            solicitud.save();
            return HttpResponseRedirect(self.get_success_url());
        else:
            return self.render_to_response(self.get_context_data, form=form, form2 = form2);
    

class Solicitud_UpdateView(UpdateView):
    model = solicitud;
    second_model = Persona;
    template_name = 'adopcion/adopcionFormView.html';
    form_class  = SolicitudForm;
    second_form_class = PersonaForm;
    success_url = reverse_lazy("adopcion:SolicitudListView")

    def get_context_data(self, **kwargs):
        context = super(Solicitud_UpdateView, self).get_context_data(**kwargs);

        pk = self.kwargs.get("pk", 0);
        solicitud = self.model.objects.get(id=pk);
        persona = self.second_model.objects.get(id=solicitud.persona_id);

        if 'form' not in context:
            context['form'] = self.form_class();
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona);

        context['id'] = pk;

        return context;
    
    def post(self, request, *args, **kwargs):
        self.object =  self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)

        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)

        if form.is_valid() and form2.is_valid():
            
            form.save();
            form2.save();

            return HttpResponseRedirect(self.get_success_url());
        else:
            return HttpResponseRedirect(self.get_success_url());


class Solicitud_DeleteView(DeleteView):
    model = solicitud;
    template_name = "adopcion/adopcion_delete.html";
    success_url = reverse_lazy("adopcion:SolicitudListView");


