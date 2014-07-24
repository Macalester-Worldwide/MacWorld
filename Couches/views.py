from Couches.models import Location
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class LocationDetail(DetailView):
    model = Location
    template_name = 'location_detail.html'


class LocationCreate(CreateView):
    model = Location
    template_name = 'location_edit.html'


class LocationUpdate(UpdateView):  # TODO: this should have a custom widget that uses a map
    model = Location
    template_name = 'location_edit.html'

    def get_object(self, queryset=None):
        obj = super(LocationUpdate, self).get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied()
        else:
            return obj


class LocationDelete(DeleteView):
    model = Location
    template_name = 'location_delete.html'
    success_url = reverse_lazy('couches-home')

    def get_object(self, queryset=None):
        obj = super(LocationDelete, self).get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied()
        else:
            return obj