from Couches.models import CouchesProfile, Couch
from django.forms import ModelForm
from django.forms.widgets import HiddenInput


class CouchesProfileForm(ModelForm):
    class Meta:
        model = CouchesProfile
        fields = ['description', 'contact_information', 'graduation_year']


class CouchForm(ModelForm):
    class Meta:
        model = Couch
        exclude = ['owner']
        widgets = {'latitude': HiddenInput, 'longitude': HiddenInput, 'address': HiddenInput}