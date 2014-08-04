from Couches.models import User, Couch
from django.forms import ModelForm, Form, CharField, FloatField
from django.forms.widgets import HiddenInput, TextInput, Textarea
from django.utils.translation import ugettext as _


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'description', 'contact_information', 'graduation_year', 'profile_picture', 'email_visible']
        widgets = {
            'name' : TextInput({'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': _('Description'), 'class': 'form-control'}),
            'contact_information': Textarea(attrs={'placeholder': _('Contact Information'), 'class': 'form-control'}),
            'name': TextInput(attrs={'placeholder': _('Full Name'), 'class': 'form-control'}),
        }

    def signup(self, request, user):
        for field in self.Meta.fields:
            setattr(user, field, self.cleaned_data[field])
        user.save()

    def __init__(self, *args, **kw):
        super(ProfileForm, self).__init__(*args, **kw)
        if 'username' in self.fields: # If username is one of the fields, it is because it is the signup form. Therefore, chang the order of the fields
            self.fields.keyOrder = ['username', 'email', 'name', 'password1', 'password2', 'graduation_year', 'profile_picture','description', 'contact_information' ]            

class CouchForm(ModelForm):
    class Meta:
        model = Couch
        exclude = ['owner']
        widgets = {'latitude': HiddenInput, 'longitude': HiddenInput, 'formatted_address': HiddenInput,
                   'address': TextInput(attrs={'class': 'form-control', })}


class UserContactForm(Form):
    message = CharField(widget=Textarea)