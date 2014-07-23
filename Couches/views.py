<<<<<<< HEAD
from django.shortcuts import render
from Couches.models import Couch

def index(request):
    return render(request, 'index.html', {'couches' : Couch.objects.all()})
=======
from Couches.models import Location
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView, DeleteView


class LocationCreate(CreateView):
    model = Location
    template_name = 'location_edit.html'
    success_url = reverse_lazy('couches-home')


class LocationUpdate(UpdateView):  # TODO: this should have a custom widget that uses a map
    model = Location
    template_name = 'location_edit.html'
    success_url = reverse_lazy('couches-home')


class LocationDelete(DeleteView):
    model = Location
    template_name = 'location_delete.html'
    success_url = reverse_lazy('couches-home')
>>>>>>> 490ac4943f268805ade7847d88a6146ef705d141
