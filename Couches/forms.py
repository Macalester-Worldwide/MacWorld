from Couches.models import CouchesProfile, Couch
from django.forms import ModelForm


class CouchesProfileForm(ModelForm):
    class Meta:
        model = CouchesProfile
        fields = ['description', 'contact_information', 'graduation_year']


class CouchForm(ModelForm):
    class Meta:
        model = Couch
        fields = ['owner', 'lon', 'lat']