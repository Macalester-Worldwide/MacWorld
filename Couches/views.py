from Couches.models import Couch
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


def index(request):
    return render(request, 'index.html', {'couches': Couch.objects.all()})


class CouchDetail(DetailView):
    model = Couch
    template_name = 'couch_detail.html'


class CouchCreate(CreateView):
    model = Couch
    template_name = 'couch_edit.html'


class CouchUpdate(UpdateView):  # TODO: this should have a custom widget that uses a map
    model = Couch
    template_name = 'couch_edit.html'

    def get_object(self, queryset=None):
        obj = super(CouchUpdate, self).get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied()
        else:
            return obj


class CouchDelete(DeleteView):
    model = Couch
    template_name = 'couch_delete.html'
    success_url = reverse_lazy('couches-home')

    def get_object(self, queryset=None):
        obj = super(CouchDelete, self).get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied()
        else:
            return obj