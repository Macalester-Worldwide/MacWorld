from Couches.forms import CouchesProfileForm
from Couches.models import CouchesProfile, Couch
from django.views.generic import DetailView, CreateView, UpdateView, ListView


class CouchesHomeView(ListView):
    model = Couch
    paginate_by = 10
    template_name = 'couch/list.html'
    context_object_name = 'couches'


class ProfileByUsernameMixin:
    slug_field = 'user__username'
    slug_url_kwarg = 'username'


class ProfileDetailView(ProfileByUsernameMixin, DetailView):
    model = CouchesProfile
    context_object_name = 'user_profile'
    template_name = 'user_profile/detail.html'


class ProfileUpdateView(ProfileByUsernameMixin, UpdateView):
    model = CouchesProfile
    form_class = CouchesProfileForm
    template_name = 'user_profile/update.html'