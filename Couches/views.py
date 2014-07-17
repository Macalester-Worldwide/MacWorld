from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView, RedirectView
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):  # called if the entered username and password are valid
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):  # called when the entered username and password are invalid
        return HttpResponse("Oh my, you've really gone and done it now.")


class LogoutView(RedirectView):
    permanent = False
    url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).dispatch(request, *args, **kwargs)