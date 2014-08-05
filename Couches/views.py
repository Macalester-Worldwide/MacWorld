from Couches.forms import CouchForm, ProfileForm, UserContactForm, CouchSearchForm
from Couches.models import User, Couch
from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMessage
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from guardian.mixins import PermissionRequiredMixin as PermReq, LoginRequiredMixin as LoginReq
from guardian.shortcuts import assign_perm, remove_perm
from django.contrib import messages
from allauth.account.decorators import verified_email_required


class CouchesHomeView(LoginReq, ListView):
    model = Couch
    paginate_by = 10
    template_name = 'couch/list.html'
    context_object_name = 'couches'


class CouchDetailView(LoginReq, DetailView):
    model = Couch
    template_name = 'couch/detail.html'
    context_object_name = 'couch'


class CouchSearchRedirect(FormView):
    form_class = CouchSearchForm
    template_name = 'couch/search.html'


    def form_valid(self, form):
        clean_data = form.cleaned_data
        return redirect(
            reverse_lazy(
                'couches:couch.search',
                kwargs={
                    'latitude': clean_data['latitude'],
                    'longitude': clean_data['longitude'],
                    'address': clean_data['address'],
                    #'tolerance': clean_data['tolerance'],
                }
            )
        )


class CouchSearchView(LoginReq, ListView):
    model = Couch
    template_name = 'couch/search_results.html'
    context_object_name = 'couches'
    DEFAULT_TOLERANCE = 0.5

    def get_queryset(self):
        latitude = float(self.kwargs['latitude'])
        longitude = float(self.kwargs['longitude'])
        tolerance = self.DEFAULT_TOLERANCE if not self.kwargs['tolerance'] else float(self.kwargs['tolerance'].strip('/'))
        latitude_range = (latitude - tolerance, latitude + tolerance)
        longitude_range = (longitude - tolerance, longitude + tolerance)
        return Couch.objects.filter(latitude__range=latitude_range, longitude__range=longitude_range)

    def get_context_data(self, **kwargs):
        context_data = super(CouchSearchView, self).get_context_data(**kwargs)
        context_data.update({'address': self.kwargs['address'].strip('/')})
        return context_data


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


class CouchUpdateView(LoginReq, PermReq, UpdateView):
    permission_required = 'Couches.change_couch'
    model = Couch
    form_class = CouchForm
    template_name = 'couch/edit.html'

    def get_context_data(self, **kwargs):
        context_data = super(CouchUpdateView, self).get_context_data(**kwargs)
        context_data.update({'couch': self.object})
        return context_data


class CouchDeleteView(LoginReq, PermReq, DeleteView):
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


class ProfileEmailFormView(LoginReq, SuccessMessageMixin, FormView):
    form_class = UserContactForm
    template_name = "user/email.html"
    success_message = "This user was e-mailed successfully."

    def form_valid(self, form):
        message = "Hi! The user: "+self.request.user.username+" ("+ self.request.user.email+") has sent you a message at MacWorld."
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        message += "\n\n Reply to this message to send him an e-mail."
        user = User.objects.get(username=self.kwargs['username'])
        email = EmailMessage(
            "Contact from " + self.request.user.username + " on MacWorld",
            message,
            'info@macworld.com',
            [user.email],
            headers = {'Reply-To': self.request.user.email})
        email.send(fail_silently=False)
        return super(ProfileEmailFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('couches:profile.detail', kwargs={'username': self.kwargs['username']})

    def get_context_data(self, **kwargs):
        context_data = super(ProfileEmailFormView, self).get_context_data(**kwargs)
        context_data.update({'username': self.kwargs['username']})
        return context_data
