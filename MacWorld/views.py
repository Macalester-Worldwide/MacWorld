from django.views.generic import TemplateView
from Couches.models import Couch


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['couches'] = Couch.objects.all()
        return context

class AuthHomeView(TemplateView):
    template_name = 'auth/home.html'