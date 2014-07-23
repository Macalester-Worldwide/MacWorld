from Couches.forms import CouchesProfileForm
from Couches.models import CouchesProfile, Couch
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect
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

    '''
    def get(self, request, *args, **kwargs):
        try:
            return super(ProfileDetailView, self).get(self, request, *args, **kwargs)
        except Http404:
            if request.user == self.object.user:
                return redirect(to=reverse_lazy('couches-profile-create'))
            else:
                return super(ProfileDetailView, self).get(self, request, *args, **kwargs)
    '''


class ProfileCreateView(ProfileByUsernameMixin, CreateView):
    model = CouchesProfile
    form_class = CouchesProfileForm
    template_name = 'user_profile/create.html'

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['user'] = request.user.id
        return super(ProfileCreateView, self).post(request, *args, **kwargs)


class ProfileUpdateView(ProfileByUsernameMixin, UpdateView):
    model = CouchesProfile
    form_class = CouchesProfileForm
    template_name = 'user_profile/update.html'