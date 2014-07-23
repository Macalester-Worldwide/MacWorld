from django.shortcuts import render
from Couches.models import Couch
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView, DeleteView

def index(request):
    return render(request, 'index.html', {'couches' : Couch.objects.all()})

class CouchCreate(CreateView):
    model = Couch
    template_name = 'couch_create.html'
    success_url = reverse_lazy('couches-home')

class CouchUpdate(UpdateView):  # TODO: this should have a custom widget that uses a map
    model = Couch
    template_name = 'couch_edit.html'
    success_url = reverse_lazy('couches-home')

class CouchDelete(DeleteView):
    model = Couch
    template_name = 'couch_delete.html'
    success_url = reverse_lazy('couches-home')