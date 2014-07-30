from Couches.forms import CouchForm, ProfileForm
from Couches.models import User, Couch
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from guardian.mixins import PermissionRequiredMixin as PermReq, LoginRequiredMixin as LoginReq
from guardian.shortcuts import assign_perm, remove_perm


class CouchesHomeView(LoginReq, ListView):
    model = Couch
    paginate_by = 10
    template_name = 'couch/list.html'
    context_object_name = 'couches'


class CouchDetailView(DetailView):
    model = Couch
    template_name = 'couch/detail.html'
    context_object_name = 'couch'


class CouchCreateView(CreateView):
    model = Couch
    template_name = 'couch/edit.html'
    form_class = CouchForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        assign_perm('change_couch', self.object.owner, self.object)
        assign_perm('delete_couch', self.object.owner, self.object)
        return super(CouchCreateView, self).form_valid(form)


class CouchUpdateView(PermReq, UpdateView):
    permission_required = 'Couches.change_couch'
    model = Couch
    form_class = CouchForm
    template_name = 'couch/edit.html'


class CouchDeleteView(PermReq, DeleteView):
    permission_required = 'Couches.delete_couch'
    model = Couch
    template_name = 'couch/delete.html'
    success_url = reverse_lazy('couches:home')

    def dispatch(self, request, *args, **kwargs):
        return super(CouchDeleteView, self).dispatch(request, *args, **kwargs)


class ProfileDetailView(LoginReq, DetailView):
    model = User
    context_object_name = 'couches_profile'
    template_name = 'old/couches_profile/detail.html'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

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


class ProfileUpdateView(PermReq, UpdateView):
    permission_required = 'Couches.change_user'
    model = User
    form_class = ProfileForm
    template_name = 'old/couches_profile/edit.html'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'