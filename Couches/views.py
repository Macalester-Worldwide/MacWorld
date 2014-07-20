from Couches.forms import ProfileForm
from Couches.models import UserProfile
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, RedirectView, DetailView, TemplateView, UpdateView, CreateView


class HomeView(TemplateView):
    template_name = 'home.html'







class ProfileByUsernameMixin:
    slug_field = 'user__username'
    slug_url_kwarg = 'username'


class ProfileDetailView(ProfileByUsernameMixin, DetailView):
    model = UserProfile
    context_object_name = 'user_profile'
    template_name = 'user_profile/detail.html'


class ProfileUpdateView(ProfileByUsernameMixin, UpdateView):
    model = UserProfile
    form_class = ProfileForm
    template_name = 'user_profile/update.html'








class UserView(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'user/detail.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'


class LoginView(FormView):
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