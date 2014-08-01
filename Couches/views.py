from Couches.forms import CouchForm, ProfileForm
from Couches.models import User, Couch
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
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


class CouchCreateView(LoginReq, CreateView):
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

    def get_success_url(self):
        return "/couches/profile/"+self.request.user.username


class CouchUpdateView(PermReq, UpdateView):
    permission_required = 'Couches.change_couch'
    model = Couch
    form_class = CouchForm
    template_name = 'couch/edit.html'

    def get_context_data(self, **kwargs):
        context_data = super(CouchUpdateView, self).get_context_data(**kwargs)
        context_data.update({'couch': self.object})
        return context_data


class CouchDeleteView(PermReq, DeleteView):
    permission_required = 'Couches.delete_couch'
    model = Couch
    template_name = 'couch/delete.html'
    success_url = reverse_lazy('couches:home')

    def dispatch(self, request, *args, **kwargs):
        return super(CouchDeleteView, self).dispatch(request, *args, **kwargs)
    def get_success_url(self):
        return "/couches/profile/"+self.request.user.username


class ProfileDetailView(LoginReq, DetailView):
    model = User
    context_object_name = 'couches_profile'
    template_name = 'user/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class ProfileUpdateView(PermReq, UpdateView):
    permission_required = 'Couches.change_user'
    model = User
    form_class = ProfileForm
    template_name = 'user/edit.html'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'