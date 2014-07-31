from Couches.models import User, Couch
from django.forms import ModelForm
from django.forms.widgets import HiddenInput


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'description', 'contact_information', 'graduation_year', 'profile_picture']

    def signup(self, request, user):
        for field in self.Meta.fields:
            print('%s: %s' % (field, self.cleaned_data[field]))
            setattr(user, field, self.cleaned_data[field])
        user.save()


class CouchForm(ModelForm):
    class Meta:
        model = Couch
        exclude = ['owner']
        widgets = {'latitude': HiddenInput, 'longitude': HiddenInput, 'address': HiddenInput}