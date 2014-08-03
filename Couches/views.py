from Couches.forms import CouchForm, ProfileForm, UserContactForm
from Couches.models import User, Couch
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from guardian.mixins import PermissionRequiredMixin as PermReq, LoginRequiredMixin as LoginReq
from guardian.shortcuts import assign_perm, remove_perm
from django.contrib import messages


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
        return reverse_lazy('couches:profile.detail', kwargs={'username': self.request.user.username})


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
        return reverse_lazy('couches:profile.detail', kwargs={'username': self.request.user.username})


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
    slug_field = 'username'
    slug_url_kwarg = 'username'

class ProfileEmailFormView(SuccessMessageMixin, FormView):
    form_class = UserContactForm
    template_name = "user/email.html"
    success_message = "This user was e-mailed successfully."

    def form_valid(self, form):
        message = "\n\n{0}".format(form.cleaned_data.get('message'))
        user = User.objects.get(username=self.kwargs['username'])
        send_mail(
            subject="Contact from "+self.request.user.username+" on MacWorld",
            message=message,
            from_email='info@macworld.com',
            recipient_list=[user.email],
        )
        return super(ProfileEmailFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('couches:profile.detail', kwargs={'username': self.kwargs['username']})

    def get_context_data(self, **kwargs):
        context_data = super(ProfileEmailFormView, self).get_context_data(**kwargs)
        context_data.update({'username': self.kwargs['username']})
        return context_data
