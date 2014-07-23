from Couches.models import CouchesProfile, Couch
from django.forms import ModelForm
from django.forms.widgets import HiddenInput


class CouchesProfileForm(ModelForm):
    """
    Form for creating or editing "Couches" profile
    """
    class Meta:
        model = CouchesProfile
        fields = ['user', 'description', 'contact_information', 'graduation_year']
        widgets = {'user': HiddenInput}


class CouchForm(ModelForm):
    """
    Form for creating or editing Couches
    """
    class Meta:
        model = Couch
        fields = ['owner', 'lon', 'lat']