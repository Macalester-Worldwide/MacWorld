from Couches.models import UserProfile
from django.forms import ModelForm, Form, CharField, PasswordInput


class ProfileForm(ModelForm):  # form for creating or editing user profile
    class Meta:
        model = UserProfile
        fields = ['user', 'description', 'contact_information', 'graduation_year']


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput())


class RegisterForm(Form):  # form for user registration
    pass  # TODO: complete this


class PasswordChangeForm(Form):  # form to change an existing user's password
    pass  # TODO: complete this