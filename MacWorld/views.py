from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class AuthHomeView(TemplateView):
    template_name = 'auth/home.html'

    def get_context_data(self, **kwargs):
        return {}