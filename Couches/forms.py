from Couches.models import User, Couch
from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput, TextInput, Textarea


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'description', 'contact_information', 'graduation_year', 'profile_picture', 'email_visible']
        widgets = {'description' : Textarea, 'contact_information' : Textarea, }

    def signup(self, request, user):
        for field in self.Meta.fields:
            setattr(user, field, self.cleaned_data[field])
        user.save()


class CouchForm(ModelForm):
    class Meta:
        model = Couch
        exclude = ['owner']
        widgets = {'latitude': HiddenInput, 'longitude': HiddenInput, 'formatted_address': HiddenInput, 'address': TextInput(attrs={'class': 'form-control',})}

class UserContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)