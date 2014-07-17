from Couches.forms import LoginForm
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        authenticate(username=form['username'], password=form['password'])
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Oh my, you've really gone and done it now.")