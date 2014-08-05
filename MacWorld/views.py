from django.views.generic import TemplateView, FormView
from Couches.models import Couch
from Couches.forms import CouchSearchForm
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

class HomeView(FormView):
    template_name = 'home.html'
    form_class = CouchSearchForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['couches'] = Couch.objects.all()
        return context

    def form_valid(self, form):
        clean_data = form.cleaned_data
        return redirect(
            reverse_lazy(
                'couches:couch.search',
                kwargs={
                    'latitude': clean_data['latitude'],
                    'longitude': clean_data['longitude'],
                    'address': clean_data['address'],
                    #'tolerance': clean_data['tolerance'],
                }
            )
        )

class AuthHomeView(TemplateView):
    template_name = 'auth/home.html'