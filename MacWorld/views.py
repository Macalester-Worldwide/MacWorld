from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView, CreateView, RedirectView


class HomeView(TemplateView):
    template_name = 'home.html'


class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'user/detail.html'


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'

    def get_success_url(self):
        return reverse_lazy('user-detail', args=(self.object,))


class UserPasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'user/password_change.html'


class LoginView(FormView):  # TODO: add support for ?next=x
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):  # called if the entered username and password are valid
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    permanent = False
    url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).dispatch(request, *args, **kwargs)