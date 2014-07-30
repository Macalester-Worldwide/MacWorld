from Couches.models import User, Couch
from django.forms import ModelForm
from django.forms.widgets import HiddenInput


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['description', 'contact_information', 'graduation_year', 'profile_picture']


class CouchForm(ModelForm):
    class Meta:
        model = Couch
        exclude = ['owner']
        widgets = {'latitude': HiddenInput, 'longitude': HiddenInput, 'address': HiddenInput}