from Couches.forms import CouchesProfileForm, CouchForm
from Couches.models import CouchesProfile, Couch
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from guardian.decorators import permission_required


class CouchesHomeView(ListView):
    model = Couch
    paginate_by = 10
    template_name = 'couch/list.html'
    context_object_name = 'couches'


class CouchCreateView(CreateView):
    model = Couch
    template_name = 'couch/edit.html'
    form_class = CouchForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user.couches_profile
        self.object.save()
        return super(CouchCreateView, self).form_valid(form)


class CouchUpdateView(UpdateView):
    model = Couch
    form_class = CouchForm
    template_name = 'couch/edit.html'

    @method_decorator(permission_required('edit_couch', (Couch, 'pk', 'pk')))
    def dispatch(self, request, *args, **kwargs):
        return super(CouchUpdateView, self).dispatch(request, *args, **kwargs)
    # TODO: Think of a better way to accomplish the preceding three lines of code


class ProfileByUsernameMixin:
    slug_field = 'user__username'
    slug_url_kwarg = 'username'


class ProfileDetailView(ProfileByUsernameMixin, DetailView):
    model = CouchesProfile
    context_object_name = 'user_profile'
    template_name = 'user_profile/detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileDetailView, self).dispatch(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            return super(ProfileDetailView, self).get(request)
        except NotImplementedError:
            return redirect(to=reverse_lazy('couches-profile-create'), permanent=False)

    def get_object(self, queryset=None):
        try:
            return super(ProfileDetailView, self).get_object(queryset)
        except Http404 as error:
            if self.request.user.username == self.kwargs['username']:
                raise NotImplementedError()  # FIXME: better exception needed (possibly custom)
            raise error


class ProfileCreateView(ProfileByUsernameMixin, CreateView):
    model = CouchesProfile
    form_class = CouchesProfileForm
    template_name = 'user_profile/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ProfileCreateView, self).form_valid(form)


class ProfileUpdateView(ProfileByUsernameMixin, UpdateView):
    model = CouchesProfile
    form_class = CouchesProfileForm
    template_name = 'user_profile/update.html'